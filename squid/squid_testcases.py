import sys
sys.path.append('..')
from testcase import TestCase 
import subprocess

APP = 'squid'
PROG = './fetch.sh' 
RES  = './fetch.res'

class FetchTestCase(TestCase):
    def __init__(self, url):
        TestCase.__init__(self, APP, PROG, RES)
        self.url = url

    def runtest(self):
        subprocess.call(['bash', self.tprog, self.url])

    def oracle(self):
        fl = open(self.res).readline().strip()
        if 'HTTP/1.1 200 OK' not in fl:
            return False
        else:
            return True

    def tostr(self):
        return self.appid, self.tprog, self.url

#urls for testing
urls = ['http://www.google.com', 
        'http://www.sina.com',
        'http://www.baidu.com']
        #'http://www.facebook.com/']

def generateFetchTestCases():
    tcs = []
    for i in range(3):
        for url in urls:
            tcs.append(FetchTestCase(url))
    return tcs

