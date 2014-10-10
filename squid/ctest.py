import sys
sys.path.append('..')
import utils
import injector

#TODO
APP = 'squid'
STARTSRPT = 
STARTARGS =
STOPSRPT  = 
STOPSRPT  =
LOGDIR    = 
CONFFILE  = 

#Generate a bunch of errorneous configuration files for testing
configfiles = []

for cfile in configfiles:
    cfile.store(CONFFILE)
    server = squidServerBundle(APP, STARTSRPT, STARTARGS, STOPSRPT, STOPARGS, LOGDIR, CONFFILE)
    #make sure the start and stop works
    server.self_test()
    
    testcases = generateFetchTestCases()
    
    if server.ctest(testcases) == True:
        print 'yes, we find the hidden ones'
    else:
        print 'ooops, squid is good!'


if __name__ == '__main__':
    ctest()

