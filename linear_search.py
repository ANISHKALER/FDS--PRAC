list=[]
element=int(input("Enter the number to be found="))
m=int(input("Enter the number of element in the list="))
count=0
for i in range(0,m):
    list.append(int(input()))
for i in range(0,m):
    count+=1
    if list[i]==element:
        print("the index of element is=",i)
        print("The count for the linear search is:",count)





        