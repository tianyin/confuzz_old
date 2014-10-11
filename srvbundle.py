import os
import time
import subprocess
import shutil

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

    def start_srv(self, waittime=1.5):
        cmd = [self.startsrpt] + self.startargs
        subprocess.call(cmd)
        time.sleep(waittime)
    
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
                print '[info] kill', pid, p
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
        if os.path.isdir(self.logdir):
            shutil.rmtree(self.logdir)
            os.mkdir(self.logdir)
