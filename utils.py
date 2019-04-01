class BeamList:
    
    def __init__(self,beam_length=10):
        self._beam_length= beam_length
        self._list = []
    
    def insert(self,elem):
        """
        return position where the elem is inserted, -1 if not
        """
        if len(self._list) == 0:
            self._list.append(elem)
            return 0
        indice = -1
        for i in range(len(self._list)):
            if(elem[0] > self._list[i][0]):
                self._list.insert(i,elem)
                indice = i
                done = True
                break
        # in case beam is not full yet
        if indice == -1 and len(self._list) < self._beam_length:
            self._list.append(elem)
            return len(self._list)
        # pop last elem if too big
        if indice != -1 and len(self._list) > self._beam_length:
            self._list.pop()
        return indice

    def get(self,indice):
        return self._list[indice]
    
    def __len__(self):
        return len(self._list)
        
def _beam_searcher_test():
    beamer = BeamList(5)
    for i in range(5):
        beamer.insert((i,"{}".format(i)))
        print(beamer._list)
    beamer.insert((12,"12"))
    print(beamer._list)
    beamer.insert((2.5,"2.5"))
    print(beamer._list)
        
