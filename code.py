from itertools import groupby
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks.sort()
        l=[]
        rounds=0
        for i,j in groupby(tasks):
            l.append(list(j))
        print(l)
        for i in l:
            length=len(i)
            if(length<2):
                return -1
            elif(length%3==0):
                rounds+=(length//3)
            else:
                while(length%3!=0):
                    length-=2
                    rounds+=1
                rounds+=(length//3)
        return rounds
