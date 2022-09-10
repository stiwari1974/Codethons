List = [5,2,3,4,1]

length = len(List)

def swapper(a,b):
  temp = List[a]
  List[a] = List[b]
  List[b]=temp


i=0
while(i<length-1):
  j=i+1
  while (j<length):
    print(List[i]," ",List[j])
    if(List[i]>List[j]):
      swapper(i,j)
    j += 1 
  print("iteration ",i," ",List)
  i +=1
print(List)
