__Program__     = "MakePosible.PosibleGroups"    
__programer__   = "Themadhood Pequot"
__Date__        = "2/27/2024"
__version__     = "0.0.6"
__update__      = ""
__info__        = ""

import gc

try:
    from . import PosibleLists
    from . import GroupSet
except:
    import PosibleLists
    import GroupSet

Error = PosibleLists.Error

#st = Error.time.time()
#Error.LenTime(st)
#Error.Log(f"","Log.txt")


def PosibleByNGroups(lstOfMembers,numOfGroups,error=False):
    try:
        if numOfGroups > 0:
            size = len(lstOfMembers) // numOfGroups

        PosibleGroupsLst = PosibleLists.PosibleLists(lst = lstOfMembers,
                                                     size=size,lean=1,
                                                     error=error)
    
    except Exception as e:
        if error:
            raise
        Error.UploadError([__Program__,__version__,"","PosibleByNGroups",
                           f"",
                           e],"Functions")


def PosibleGroupSets(lstOfGroups,numberOfGroups=1,error=False):
    """
runs but takes forever
"""
    done = {"S":100000,"A":[]}
    retar = []
    try:
        group = GroupSet.Groups(lstOfGroups=lstOfGroups,
                                numberOfGroups=numberOfGroups,error=error)
        
        statesToExplore = group.ExploreStates()

        #_ExploreStates(statesToExplore=statesToExplore,done=done,error=error)

        while statesToExplore > []:
            poped = statesToExplore.pop()
            
            if poped.Complete():
                poped = poped.groups
                poped.sort()
                
                #if poped not in done:
                done["A"].append(poped)
            else:
                statesToExplore += poped.ExploreStates()
                
            del(poped)

            if len(done["A"]) >= done["S"]:
                done["S"] += 100000
                print(len(done["A"]))
                gc.collect()

        print()
        print(len(done["A"]))
        while done["A"] > []:
            poped = done["A"].pop()
            try:
                done["A"].remove(poped)
            except:
                pass
            retar.append(poped)
            #if poped not in retar:
                #retar.append(poped)
        print(len(retar))
            
    except Exception as e:
        if error:
            raise
        Error.UploadError([__Program__,__version__,"","PosibleGroupSets",
                           f"",
                           e],"Functions")
    return retar


"""
gets to 15,000,000 and lags out

def _ExploreStates(statesToExplore,done,error=False):
    if len(statesToExplore) > 1:
        mid = len(statesToExplore)//2

        left = statesToExplore[:mid]
        right = statesToExplore[mid:]

        _ExploreStates(statesToExplore=left,done=done,error=error)
        _ExploreStates(statesToExplore=right,done=done,error=error)

    else:
        try:
            state = statesToExplore.pop()
            del(statesToExplore)
            if state.Complete():
                group = state.groups
                del(state)
                group.sort()
                    
                done["A"].append(group)
            else:
                statesToExplore += state.ExploreStates()
                del(state)
                _ExploreStates(statesToExplore=statesToExplore,done=done,
                           error=error)

            if len(done["A"]) >= done["S"]:
                done["S"] += 100000
                print(len(done["A"]))
                gc.collect()

                
        except IndexError:
            pass
        except Exception as e:
            if error:
                raise
            Error.UploadError([__Program__,__version__,"","_ExploreStates",
                           f"",
                           e],"Functions")
"""
                




if __name__ == "__main__":
    nmem = 75
    size = 9
    mem = []
    for i in range(0,nmem):
        mem.append(i)

    print("members:",len(mem))

    PosibleGroupsLst = PosibleLists.PosibleLists(lst = mem,size=size,lean=1,
                                                     error=True)
    print("posible groups:",len(PosibleGroupsLst))

    resalts = PosibleGroupSets(lstOfGroups=PosibleGroupsLst,
                               numberOfGroups=nmem//size,error=True)
    
















