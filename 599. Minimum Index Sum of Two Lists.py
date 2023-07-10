class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l = [list1[0]]
        mn = len(list1) + len(list2)
        for i in list1:
            if i in list2:
                ind = list1.index(i) + list2.index(i)
                if ind < mn:
                    mn = ind
                    l[0] = i
                elif ind == mn:
                    l.append(i)
        return l