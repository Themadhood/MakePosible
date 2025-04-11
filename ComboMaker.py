__Program__     = "Makeposible.ComboMaker"    
__Programer__   = "Themadhood Pequot"
__Date__        = "1/2/20224"
__Version__     = "0.0.1"
__Time__        = "0000:00:00: 00:47:00"
__ErrorTab__    = ""
__Update__      = ""
__Info__        = ""
TestModual      = []

import Error
"""
st = Error.time.time()
Error.LenTime(st)
Error.Log(f"","Log.txt")
"""
#compile PYsInfo
VersionLst = [f"{__Program__}: {__Version__}: {__Time__}"]
VersionLst += Error.VersionLst

def MakeVariants(string):
    retar = [string]

    cap = string.capitalize()
    
    retar.append(string.upper())
    retar.append(string.lower())
    retar.append(cap)
    retar.append(cap.swapcase())
    
    return retar


def Conbine2StrVariants(string1,string2):
    retar = [f"{string1}{string2}",
             f"{string2}{string1}",
             f"{string1} {string2}",
             f"{string2} {string1}"]
    return retar

"""
try:
    pass

except Exception as e:
    if self._Error:
        raise
    Error.UploadError([_FILE,_VERSION,"class","def",
                                f"mesage",e],"Functions")
"""



if __name__ == "__main__":
    print(MakeVariants("love"))
















