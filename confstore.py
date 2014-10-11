class ConfStore:
    """
    Basically, we model any configuration file to be in the same format like an INI file which
    consist of section, parameter, value (checkout INI files on wiki)
    """
    def __init__(self):
        self.confstore = {}
    
    def add(self, sec, p, v):
        if sec not in self.confstore:
            self.confstore[sec] = []
        pvstore = self.confstore[sec]
        pvstore.append((p, v))

    def change_sec_p(self, sec, p, v):
        """
        Change the value given the section, parameter, and new value
        """
        if sec not in self.confstore:
            return False;
        pvstore = self.confstore[sec]
        for idx, pv in enumerate(pvstore):
            if pv[0] == p:
                pvstore[idx] = (p, v)
    
    def change_all_p(self, p, v):
        for sec in self.confstore:
            pvstore = self.confstore[sec]
            for idx, pv in enumerate(pvstore):
                if pv[0] == p:
                    pvstore[idx] = (p, v)
    
    def get_pset(self):
        pset = set()
        for sec in self.confstore:
            pvstore = self.confstore[sec]
            for p, v in pvstore:
                pset.add(p)
        return pset 

    def get_confstore(self):
        return self.confstore

    def print_confstore(self):
        for sec in self.confstore:
            print sec + ':'
            pvstore = self.confstore[sec]
            for p, v in pvstore:
                print '    ', p, ',', v

    def addparameters(self, kvpath):
        pset = self.get_pset()
        f = open(kvpath, 'r')
        for l in f:
            l = l.strip()
            if l not in pset:
                #TODO: define the format of kvpath
                self.add('', l, None)
                 
