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

#This can be used for self-testing
CORRECT_CONFFILE = '/home/tianyin/conquid/app/squid-3.4.8/build/etc/squid.conf.org'

CONFFILE_LOC = '/home/tianyin/conquid/app/squid-3.4.8/build/etc/squid.conf'


#Generate a bunch of errorneous configuration files for testing

#for cfile in configfiles:
#    cfile.store(CONFFILE)

def injtest():
    #TODO: generate a bunch of erroneous files in a tmp dir (e.g., somewhere in /tmp)
    ecfiles = []
    for ecf in ecfile:
        #move to the location
        if ctest() == True:
            print 'pass the tests'
        else:
            print 'fail the tests'


def selftest():
    #TODO: make sure the right file is in the location
    conffile = CORRECT_CONFFILE
    if ctest() == False:
        print '[error] self test fails'
        return False
    else:
        return True


def ctest():
    """
    return
    True: passed the testcases
    False: faile to pass
    """
    server = ServerBundle(APP, STARTSRPT, STARTARGS, STOPSRPT, STOPARGS, LOGDIR, CONFFILE)
    #make sure the start and stop works
    #server.self_test()
    testcases = squid_testcases.generateFetchTestCases()
    return server.ctest(testcases)


if __name__ == '__main__':
    if selftest() == True:
        print 'Pass self testing'
    else:
        print 'Fail to pass self testing'

