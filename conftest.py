#from srvbundle import ServerBundle
from datetime import datetime
import errgen
import cparser
import os
import shutil

class ConfTest:
    def __init__(self, app, srv, tcs, parser, confloc, conforg, pset):
        self.app = app
        self.srv = srv
        self.testcases = tcs
        self.parser = parser
        self.confloc = confloc
        self.conforg = conforg
        self.pset = pset

    def clean_state(self):
        self.srv.clean_state()
        for tc in self.testcases:
            tc.clean_state()

        if self.srv.exist() == True:
            self.srv.stop_srv()
        if self.srv.exist() == True:
            self.srv.kill()
        if self.srv.exist() == True:
            print '[error] Cannot terminate the running server'
            os.exit(-1)

    def ctest(self):
        """
        ---------------------------------------------------
        The Standard Testing Process Should Be As Follows
        ---------------------------------------------------
        1. start the server
        2. check whether start successfully
        3. run each test case one by one
        4. check whether test cases all finish or fail
        5. check the server after each test case
        6. stop the server
        7. if stop failes, run the kill function
        ----------------------------------------------------
        """
        #Make sure we start from a clean system state
        self.clean_state()
        #Start the server
        self.srv.start_srv()
        #utils.exec_scripts('bash', ['./squidmgr.sh', 'start'])
        if self.srv.exist() == False:
            print '[info] Server dies at the startup time'
            return False
        else:
            print '[info] Server starts successfully'
   
        #Test
        for tc in self.testcases:
            #Run
            tc.runtest()
            #Oracle
            if tc.oracle() == False:
                tc.print_testcase()
                #tc.bundle_res()
                print 'Fail to pass the test case:', tc.tostr()
                return False
        
            #remove the res files
            tc.clean_state()

            #Check server aliveness
            if self.srv.exist() == False:
                print 'Server dies after test case:', tc.tostr() 
                return False
    
        #Clean the state
        self.srv.clean_state()
        #Stop
        self.srv.stop_srv()
        if self.srv.exist() == True:
            self.srv.kill()
        return True

    def selftest(self):
        """
        We have to first pass self testing which makes sure that the default configuration is correct
        """
        shutil.copyfile(self.conforg, self.confloc)    
        return self.ctest();

    def injtest(self):
        """
        Inject errors into different parameters and then test
        """
        cstore = self.parser.parse(self.conforg)
        cstore.addparameters(self.pset)
        
        time = datetime.now().strftime('_%Y-%m-%d_%H-%M-%S') 
        tmpcfdir = '/tmp/' + self.app + time
        os.mkdir(tmpcfdir)

        errpairs = errgen.err_conffile_gen(self.parser, cstore, tmpcfdir)
        for ep, ef in errpairs:
            shutil.copyfile(ef, self.confloc)
            if self.ctest() == True:
                print 'pass the tests'
                print 'erroneous parameter:', ep
                print '-----------------------------'
            else:
                print 'fail the tests'
    
    def runtest(self):
        """
        print '[info] start self testing...'
        for i in range(0, 5):
            if self.selftest() == False:
                print '[error] self-test fails'
                return
        print '[info] pass self testing...'
        """
        print '[info] start inj testing...'
        self.injtest()
