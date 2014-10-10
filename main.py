import subprocess

def exec_scripts(app, startscripts, args=[]):
    cmd = [startscripts] + args
    subprocess.call(cmd)

#def stop(app, stopscripts, args=None):
#    print('stop a server in a graceful way')

def get_proc_desc(appid):
    """
    return a list of proc desc
    """
    ps  = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
    grp = subprocess.Popen(['grep', appid], stdin=ps.stdout, stdout=subprocess.PIPE)
    #awk = subprocess.Popen(['awk', '\'{print $11}\''], stdin=grp.stdout, stdout=subprocess.PIPE)
    ps.stdout.close()
    output = grp.communicate()[0]
    #print output
    
    procs = output.strip().split('\n')
    return procs

def kill(appid):
    pdesc = get_proc_desc(appid)
    for p in pdesc:
        p = p.strip().split()
        pid = p[1]
        swp = p[10]
        if swp != 'grep':
            print '[info] kill', pid
            subprocess.call(['kill', '-9', pid])
        

def exist(appid):
    pdesc = get_proc_desc(appid)
    for p in pdesc:
        p = p.strip().split()
        print p
        if p[10] != 'grep':
            return True
        else:
            continue
    return False

def test(appid,
         startscripts, startargs,
         stopscripts, stopargs):
    print ("test")
    """
    1. start the server
    2. check whether start successfully
    3. run test cases
    4. check whether test cases all finish or past
    5. check the server after each test case
    6. stop the server
    7. if stop failes, run the kill function
    """

#exec_scripts('squid', 'ps', ['aux'])
#print exist('squid')
#print kill('squid')

