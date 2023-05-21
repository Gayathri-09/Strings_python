# program to remove the duplicates from the given list

list=[1,2,3,4,1,2,5,6,3,7]
result=[]
count=0
for num in list:
    if num not in result:
        result.append(num)
    else:
        count=count+1
print("the original list=",list)
print("the list without duplicates=",result)
print("no of duplicates=",count)
        
