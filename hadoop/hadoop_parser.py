import os
from lxml import etree
from io import StringIO, BytesIO

#if not os.path.exists(OUTPUT_DIR):
#    os.mkdir(OUTPUT_DIR) 

def parse(xmlfile):
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
        for y in v: value = y.text
        #desc
        d = ppt.xpath('./description')
        for z in d: desc = z.text
        
        """
        do your stuff
        """
        print '----------------------'
        print name
        if value != None: 
            print value
        if desc  != None: 
            print desc


def writeback():
    #TODO: generate the configuration file based on the error
    print 'hello'

if __name__ == "__main__":
    parse('./yarn-default.xml')
