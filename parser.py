from configstore import ConfStore

class Parser:
    """
    The basic class of all the parsers
    """
    def parse(self, filepath):
        print "[error] The parse() in the Parser class should never be called!"
        return None

    def write2file(self, confstore):
        print "[error] The tofile() in the Parser class should never be called!"
        pass


class SimpleKVParser:
    """
    Parser for key-value formatted files
    Should be able to work with Squid, PostgreSQL, VSFTPD, etc
    """
    def __init__(self, d=' ', c = '#', b='\\'):
        self.delim = d
        self.linebrk = b

    def parse(self, conffile):
        confstore = ConfStore()
        #TODO support line breakers
        f = open(conffile, 'r')
        for l in f:
            l = l[:l.find('#')].strip()
            if len(l) == 0:
                continue
            brk = l.find(self.delim)
            k = l[:brk]
            v = l[brk+1:]
            confstore.add('', k, v)
        return confstore

    def write2file(self, confstore, destf):
        f = open(destf, 'w')
        cstore = confstore.get_confstore()
        for sec in cstore:
            kvstore = cstore[sec]
            for k, v in kvstore:
                cl = k + self.delim + v + '\n'
                f.write(cl)
        f.close()


class HadoopParser:
    """
    Parser for Hadoop systems such as MR, Yarn, HDFS, ZK, etc
    """
    def parse(self, xmlfile):
        confstore = ConfStore()
        tree = etree.parse(open(xmlfile))
        ppts = tree.xpath('//property')
        for ppt in ppts:
            #There's always a name
            value = None;
            desc = None;
            #name
            n = ppt.xpath('./name')
            for x in n: name = x.text.strip()
            #value
            v = ppt.xpath('./value')
            for y in v: 
                value = y.text
            if value == None:
                value = ''
            #desc (useless to us)
            #d = ppt.xpath('./description')
            #for z in d: 
            #    desc = z.text
            #if desc == None:
            #    desc = ''
            confstore.add('', name, value)
        return confstore

    def write2file(self, confstore):
        #TODO
        pass


#testing
skvp = SimpleKVParser()
cstore = skvp.parse('/home/tianyin/conquid/app/squid-3.4.8/build/etc/squid.conf')
cstore.inject('http_port')
cstore.print_confstore()
skvp.write2file(cstore, '/home/tianyin/conquid/app/squid-3.4.8/build/etc/squid.conf.gen')
