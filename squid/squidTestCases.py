#TODO: more urls and repeated
#urllist = ['http://www.google.com', 'http://www.sina.com']

#def fetchTC(url):
#    utils.exec_scripts(APPID, 'bash', ['./fetch.sh'] + [url])

APP = 'squid'
PROG = 
RES = 

class FetchTestCase(TestCase):
    def __init__(self, url):
        TestCase.__init__(APP, PROG, RES)
        self.url = url

    def runtest(self):
        subprocess.call(['bash', self.tprog, url])

    def oracle(self):
        fl = open(self.res).readline().strip()
        if 'HTTP/1.1 200 OK' not in fl:
            return False
        else:
            return True

#TODO: 10 urls

def generateFetchTestCases():
