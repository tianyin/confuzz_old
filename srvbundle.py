import subprocess

class ServerBundle():
    def __init__(self, app, 
            strtsrpt, strtargs, stpsrpt, stpargs, logs, cfile):
        self.app = app
        self.startsrpt = strtsrpt
        self.startargs = strtargs
        self.stopsrpt  = stpsrpt
        self.stopargs  = stpargs
        self.logdir    = logs
        self.configfile = cfile

    #def exec_scripts(self):
    #    cmd = [startsrpt] + self.startargs
    #    subprocess.call(cmd)

    def start_srv(self):
        cmd = [self.startsrpt] + self.startargs
        subprocess.call(cmd)
    
    def stop_srv(self):
        cmd = [self.stopsrpt]  + self.stopargs
        subprocess.call(cmd)

    def get_proc_desc(self):
        """
        return a list of proc desc
        """
        ps  = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
        grp = subprocess.Popen(['grep', self.app], stdin=ps.stdout, stdout=subprocess.PIPE)
        #awk = subprocess.Popen(['awk', '\'{print $11}\''], stdin=grp.stdout, stdout=subprocess.PIPE)
        ps.stdout.close()
        output = grp.communicate()[0]
        #print output
    
        procs = output.strip().split('\n')
        return procs

    def kill(self):
        pdesc = self.get_proc_desc()
        for p in pdesc:
            p = p.strip().split()
            pid = p[1]
            swp = p[10]
            if swp != 'grep':
                print '[info] kill', pid
                subprocess.call(['kill', '-9', pid])
        

    def exist(self):
        pdesc = self.get_proc_desc()
        for p in pdesc:
            p = p.strip().split()
            #print p
            if p[10] != 'grep':
                return True
            else:
                continue
        return False

    def store_logs(self, dest):
        nlogdir = dest + '/logs/'
        if os.path.isdir(self.logdir) == True:
            os.renames(self.logdir, nlogdir)

    def clean_state(self):
        #TODO
        print 'clean state:'

    def self_test(self):
        print 'need to implement'

    def ctest(self, testcases):
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
        #Start the server
        self.start_srv()
        #utils.exec_scripts('bash', ['./squidmgr.sh', 'start'])
        if self.exist() == False:
            print '[info] Server dies at the startup time'
            return False
        else:
            print '[info] Server starts successfully'
   
        #Test
        for tc in testcases:
            #Run
            tc.runtest()
            #Oracle
            if tc.oracle() == False:
                tc.print_testcase()
                #tc.bundle_res()
                return False
        
            #remove the res files
            tc.clean_state()

            #Check server aliveness
            if self.exist() == False:
                print 'Server dies at tc:', tc.tostr() 
                return False
    
        #Clean the state
        self.clean_state()
        #Stop
        self.stop_srv()
        if self.exist() == True:
            self.kill()
        return True

#exec_scripts('squid', 'ps', ['aux'])
#print exist('squid')
#print kill('squid')

