import sys
sys.path.append('..')
from srvbundle import ServerBundle
import injector
import squid_testcases

APP = 'squid'
STARTSRPT = 'bash' 
STARTARGS = ['./squidmgr.sh', 'start']
STOPSRPT  = 'bash'
STOPARGS  = ['./squidmgr.sh', 'stop']
LOGDIR    = '/home/tianyin/conquid/app/squid-3.4.8/build/var/logs/'
CONFFILE  = '/home/tianyin/conquid/app/squid-3.4.8/build/etc/squid.conf'
#This can be used for self-testing
CORRECT_CONFFILE = '/home/tianyin/conquid/app/squid-3.4.8/build/etc/squid.conf.org'


#Generate a bunch of errorneous configuration files for testing
configfiles = [CORRECT_CONFFILE]

#for cfile in configfiles:
#    cfile.store(CONFFILE)
def ctest():
    server = ServerBundle(APP, STARTSRPT, STARTARGS, STOPSRPT, STOPARGS, LOGDIR, CONFFILE)
    #make sure the start and stop works
    #server.self_test()
    
    testcases = squid_testcases.generateFetchTestCases()
    
    if server.ctest(testcases) == True:
        print 'yes, we find the hidden ones'
    else:
        print 'ooops, tests fail to pass'


if __name__ == '__main__':
    ctest()

