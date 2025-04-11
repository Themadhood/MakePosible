__Program__     = "MakePosible.Posiblesets"    
__programer__   = "Themadhood Pequot"
__Date__        = "2/27/2024"
__version__     = "0.0.2"
__Time__        = "0000:00:05: 00:47:00"
__ErrorTab__    = ""
__update__      = ""
__info__        = ""

import Error


#compile PYsInfo
VersionLst = [f"{__Program__}: {__Version__}: {__Time__}"]
VersionLst += Error.VersionLst


def PosibleLists(lst,size=0,lean=0,cantBeInSame=[],Set=False,error=False):
    #safty
    try:
        lst = list(lst)
    except:
        return [[lst]]
    
######################## make all posible ##################################
    tst = Error.time.time()
    posible = []
    try:
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                posible.append(lst[i:j + 1])

    except Exception as e:
        if error:
            raise
        Error.UploadError([__Program__,__version__,"","PosibleLists",
                           f"failed to make posible lists from {lstOfContents}",
                           e],"Functions")
    Error.Log(f"sub set runtime: {Error.LenTime(tst)}","Log.txt")

################## remove all outside size range #####################
    st = Error.time.time()
    try:
        if size > 0:
            maxlen = size+lean
            minlen = size-lean
            temp = posible.copy()
            
            while temp > []:
                poped = temp.pop()
                ln = len(poped)
                if ln > maxlen or ln < minlen:
                    posible.remove(poped)

    except Exception as e:
        if error:
            raise
        Error.UploadError([__Program__,__version__,"","PosibleLists",
                           f"failed to remove sub sets not == size+- lean",
                           e],"Functions")
    Error.Log(f"remove < size > sub sets runtime: {Error.LenTime(st)}",
              "Log.txt")

########################## turn lsts to sets ###############################    
    st = Error.time.time()
    try:
        if Set:
            retar = []
            while posible > []:
                poped = set(posible.pop())
                retar.append(poped)
            Error.Log(f"lst to set runtime: {Error.LenTime(st)}","Log.txt")
        else:
            retar = posible

    except Exception as e:
        if error:
            raise
        Error.UploadError([__Program__,__version__,"","PosibleLists",
                           f"failed to remove sub sets not == size+- lean",
                           e],"Functions")
    
    
########################## turn lsts to sets ###############################
    st = Error.time.time()
    try:
        while cantBeInSame > []:
            cant = cantBeInSame.pop()
            temp = retar.copy()
            while temp > []:
                poped = temp.pop()
                if cant[0] in poped and cant[1] in poped:
                    retar.remove(poped)

    except Exception as e:
        if error:
            raise
        Error.UploadError([__Program__,__version__,"","PosibleLists",
                           f"failed to remove sub sets not == size+- lean",
                           e],"Functions")


        
    Error.Log(f"total sub set runtime: {Error.LenTime(tst)}","Log.txt")
    
    return retar






if __name__ == "__main__":
    L = [1,2,3]
    c = [[1,3]]
    
    #[1]
    #[1,2]
    #[1,2,3]
    #[1,3]
    #[1,3,2]
    
    #[2]
    #[2,1]
    #[2,1,3]
    #[2,3]
    #[2,3,1]
    
    #[3]
    #[3,1]
    #[3,1,2]
    #[3,2]
    #[3,2,1]
    


    lst = PosibleLists(L,cantBeInSame=c,error=True)

    for l in lst:
        print(l)
    
















