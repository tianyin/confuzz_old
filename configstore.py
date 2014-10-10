import errgen

class ConfStore:
    def __init__(self):
        self.confstore = {}

    def add(self, sec, p, v):
        if sec not in self.confstore:
            self.confstore[sec] = []
        pvstore = self.confstore[sec]
        pvstore.append((p, v))

    def change_value(self, sec, p, v):
        """
        Change the value given the section, parameter, and new value
        """
        if sec not in self.confstore:
            return False;
        pvstore = self.confstore[sec]
        for idx, pv in enumerate(pvstore):
            if pv[0] == p:
                pvstore[idx] = (p, v)

    def get_confstore(self):
        return self.confstore

    def inject(self, p):
        for sec in self.confstore:
            pvstore = self.confstore[sec]
            for idx, pv in enumerate(pvstore):
                if pv[0] == p:
                    pvstore[idx] = (p, errgen.conf_err_gen(p, pv[1], ''))

    def print_confstore(self):
        for sec in self.confstore:
            print sec + ':'
            pvstore = self.confstore[sec]
            for p, v in pvstore:
                print '    ', p, ',', v


def test():
    cstore = ConfStore()
    cstore.add('shit', 'a', '1')
    cstore.add('shit', 'b', '2')
    cstore.add('shit', 'c', '3')
    cstore.add('shit', 'd', '4')
    cstore.change_value('shit', 'b', 'ass')
    cstore.inject('b')
    cstore.print_confstore()
