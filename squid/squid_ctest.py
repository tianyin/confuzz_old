import sys
sys.path.append('..')
from srvbundle import ServerBundle
from cparser import SimpleKVParser
#from parser import SimpleKVParser
from conftest import ConfTest
import squid_testcases
#import shutil


APP = 'squid-3.4.8'
STARTSRPT = 'bash' 
STARTARGS = ['./squidmgr.sh', 'start']
STOPSRPT  = 'bash'
STOPARGS  = ['./squidmgr.sh', 'stop']
LOGDIR    = '/home/tianyin/conquid/app/squid-3.4.8/build/var/logs/'
CONFFILE_LOC = '/home/tianyin/conquid/app/squid-3.4.8/build/etc/squid.conf'
PARAMETER_SET = './pset'

#This can be used for self-testing
CORRECT_CONFFILE = '/home/tianyin/conquid/app/squid-3.4.8/build/etc/squid.conf.org'

server = ServerBundle(APP, STARTSRPT, STARTARGS, STOPSRPT, STOPARGS, LOGDIR, CONFFILE_LOC)
kvparser = SimpleKVParser() 
testcases = squid_testcases.generateFetchTestCases()
conftest = ConfTest(APP, server, testcases, kvparser, CONFFILE_LOC, CORRECT_CONFFILE, PARAMETER_SET)

conftest.runtest()
