import os
from datetime import datetime

class TestCase:
    def __init__(self, aid, tcp, acclog, errlog, res):
        self.appid     = aid
        self.testprog  = tcp
        self.accesslog = acclog
        self.errorlog  = errlog
        self.respath   = res

    def oracle(self):
        return False

    def runtest(self):
        return False

    def bundle_res(self, dest):
        """
        Bundle the results and stored in dest
        """
        time = datetime.now().strftime('_%Y-%m-%d_%H-%M-%S') 
        newdir = dest + '/' + self.appid + time + '/'
        os.mkdir(newdir)
        if self.accesslog != None: 
            os.rename(self.accesslog, newdir + os.path.basename(self.accesslog))
        if self.errorlog != None:
            os.rename(self.errorlog,  newdir + os.path.basename(self.errorlog))
        if self.respath != None:
            if os.path.isdir(self.respath) == True:
                os.renames(self.respath, newdir + os.path.basename(self.respath))
            else:
                os.rename(self.respath, newdir + os.path.basename(self.respath))


class testi_bundle():
    tc = TestCase('squid', 'xxx', None, None, '/home/tianyin/conquid/app/squid-3.4.8/build/var/logs/')
    tc.bundle_res('./'); 
