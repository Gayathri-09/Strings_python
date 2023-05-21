#program to find missing number in given series

list1=[1,2,3,4,5,6,7,9]
#length of list
n=len(list1)+1
sum1=n*(n+1)/2
sum2=0
for i in list1:
    sum2=sum2+i
print("sum of series=",sum1)
print("sum of series with missing number:",sum2)
missing_num=sum1-sum2
print("the missing number:",missing_num)
