from itertools import combinations
lst=[]
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lst=[[a,b,c]  for b in range(y+1) for c in range(z+1)   for a in range(x+1) ]

finallst=[]
for items in combinations(lst,3):
    for nums in items:
       x=sum(nums)
       if x!=n and nums not in finallst:
            finallst.append(nums)

f_finallst= (sorted(map(str,(finallst))))
print (f_finallst)
