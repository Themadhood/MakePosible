__Program__     = "MakePosible.MakePosibleGroups"    
__programer__   = "Themadhood Pequot"
__Date__        = "4/3/2024"
__version__     = "0.0.4"
__update__      = ""
__info__        = ""


import Error



class Groups():    
    
    def __init__(self,lstOfGroups,numberOfGroups=1,error=False):
        self._Error = error

        self._lstOfGroups = lstOfGroups.copy()
        self._NGroups = numberOfGroups
        self.groups = []
        

    def Clone(self):
        try:
            clone = Groups(self._lstOfGroups,self._NGroups)
            clone.groups = self.groups.copy()
        except Exception as e:
            if error:
                raise
            Error.UploadError([__Program__,__version__,"","",
                       f"failed to make posible lists from {lstOfContents}",
                           e],"Functions")
        return clone

    def Complete(self):
        #print(len(self.groups))
        if self._lstOfGroups == [] and len(self.groups) >= self._NGroups:
            return True
        return False

    def AddGoup(self,group):
        try:
            self.groups.append(group)
            self._lstOfGroups.remove(group)
            
            temp = self._lstOfGroups.copy()
            while temp > []:
                poped = temp.pop()
                for member in group:
                    if member in poped:
                        self._lstOfGroups.remove(poped)
                        break
        except Exception as e:
            if error:
                raise
            Error.UploadError([__Program__,__version__,"","",
                       f"failed to make posible lists from {lstOfContents}",
                           e],"Functions")
    
    def ExploreStates(self):
        retar = []
        try:
            for group in self._lstOfGroups:
                clone = self.Clone()
                clone.AddGoup(group)
                retar.append(clone)
                #del(clone)
        except Exception as e:
            if error:
                raise
            Error.UploadError([__Program__,__version__,"","",
                       f"failed to make posible lists from {lstOfContents}",
                           e],"Functions")
        return retar

    

#Error.Log(f"sub set runtime: {Error.LenTime(tst)}","Log.txt")
#st = Error.time.time()




if __name__ == "__main__":
    gr = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

    def P(s):
        print("\n\n")
        for g in s:
            print(g.groups)



    
    g = Groups(lstOfGroups=gr,numberOfGroups=2,error=True)
    s = g.ExploreStates()
    P(s)

    done = []
        



    def pop(done,s):
        print(len(s))
        poped = s.pop()
        if poped.Complete():
            done.append(poped)
        else:
            s += poped.ExploreStates()
        P(s)
        print("pop(done,s)")


    pop(done,s)












