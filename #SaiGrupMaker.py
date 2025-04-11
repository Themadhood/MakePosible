#program:       SaiGrupMaker
#purpose:       
#progamer:      Madison Arndt 6/5/2023


from THEMADHOOD.Library.MakePosible import MultiplePosibleGroups as MPG
import math


def SAIMakePosibleGroups(lstOfMembers,numberOfGroups,
                         Conditions=set(),error=False):

    lean = (len(lstOfMembers) / numberOfGroups) -1
    lean = math.ceil(lean)

    #make all posible
    lst = MPG.MultiplePosibleGroups(lstOfMembers = lstOfMembers,
                                    numberOfGroups = numberOfGroups,
                                    error = error)

    print("remove empty group Vairiants")
    #remove empty group Vairiants
    RemoveGroupsWithEmptyGroup(lst,error=error)

    print("Remove uneven")
    #Remove uneven
    RemoveWithMemberGap(lst,lean,error=error)

    print("remove lsts that meet conditons")
    #remove lsts that meet conditons
    for Condition in Conditions:
        con1 = Condition.pop()
        con2 = Condition.pop()
        RemoveItemWithItem(lst,con1,con2,error=error)

    return lst


if __name__ == "__main__":
    L = [1,2,3,4,5,6,7,8,9,10]
    conditions = [{1,2},{2,8},{2,6},{5,6},{7,3},{9,10}]
    
    lst = SAIMakePosibleGroups(L,9,error=True)

    
    for l in lst:
        print(l)
