import sys
sys.path.append('..')
import utils
import injector

APPID = 'squid'

#TODO: more urls and repeated
urllist = ['http://www.google.com', 'http://www.sina.com']

def fetchTC(url):
    utils.exec_scripts(APPID, 'bash', ['./fetch.sh'] + [url])
    fl = open('./fetch.res').readline().strip()
    if 'HTTP/1.1 200 OK' not in fl:
        return False
    else:
        return True

def ctest():
    """
    Test a single configuration file
    """
    #Start the server
    utils.exec_scripts(APPID, 'bash', ['./squidmgr.sh', 'start'])
    if utils.exist(APPID) == False:
        print 'Server dies at the startup time'
        return
   
    #Test
    for url in urllist:
        #Oracle
        if fetchTC(url) == False:
            print 'Fail at fetching url', url
            return
        #TODO: remove the res files
        #Check server aliveness
        if utils.exist(APPID) == False:
            print 'Server dies at url', url 
            return

    #Stop
    utils.exec_scripts(APPID, 'bash', ['./squidmgr.sh', 'stop'])
    if utils.exist(APPID) == True:
        utils.kill(APPID)

if __name__ == '__main__':
    ctest()

