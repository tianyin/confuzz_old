import parser
from confstore import ConfStore
import copy

def conf_err_gen(p, v, ty):
    """
    p:  parameter
    v:  value
    ty: type of the parameter
    """
    #we first do the simplest one
    return 'you_are_idiot'

def err_conffile_gen(parser, cstore, cfdir):
    """
    Given a ConfStore object, generate the configuration files and put
    into cfdir
    Return:
    a list of pairs <erroneous_parameter, conf_file>
    """
    res = []
    pset = cstore.get_pset()
    for p in pset:
        #get erroneous value
        ev = conf_err_gen(p, '', '')
        #clone a new ConfStore
        ncstore = copy.deepcopy(cstore)
        #change all the values associated with p
        ncstore.change_all_p(p, ev)
        #write to file and add to results
        cfpath = cfdir + '/' + p
        parser.write2file(ncstore, cfpath)
        res.append((p, cfpath))
    return res 
