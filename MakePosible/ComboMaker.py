#program:       ComboMaker
#purpose:       
#progamer:      Themadhood Pequot 1/2/2024

_FILE = "MakePosible.ComboMaker"
_VERSION = "0.0.1"

import Error
"""
st = Error.time.time()
Error.LenTime(st)
Error.Log(f"","Log.txt")
"""

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
















