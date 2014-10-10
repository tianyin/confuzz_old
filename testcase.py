import os
from datetime import datetime
import shutil

class TestCase:
    """
    Any subclass must implemenet runtest() and oracle()
    """
    def __init__(self, app, prog, re):
        self.appid = app
        self.tprog = prog
        self.res   = re

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
        #if self.accesslog != None: 
        #    os.rename(self.accesslog, newdir + os.path.basename(self.accesslog))
        #if self.errorlog != None:
        #    os.rename(self.errorlog,  newdir + os.path.basename(self.errorlog))
        if self.res != None:
            if os.path.isdir(self.res) == True:
                os.renames(self.res, newdir + os.path.basename(self.res))
            else:
                os.rename(self.res, newdir + os.path.basename(self.res))
    
    def print_testcase(self):
        print self.appid, self.tprog, self.res
    
    def clean_state(self):
        if os.path.isdir(self.res):
            shutil.rmtree(self.res)
        elif os.path.isfile(self.res):
            os.remove(self.res)

    def tostring():
        print app, prog, re
    
test_bundle():
    tc = TestCase('squid', None, '/home/tianyin/conquid/app/squid-3.4.8/build/var/logs/')
    tc.bundle_res('./'); 
