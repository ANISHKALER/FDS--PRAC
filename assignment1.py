list=[]
n=int(input("Enter the number of student:"))
for i in range(0,n):
    i=int(input("Enter the number of marks: "))
    if(i<=50):
        list.append(i)
    else:
        print("you entered wrong marks\n reenter the marks")
        i=(int(input("Enter the marks of the student")))
        list.append(i)
#absent student
def absent(list):
    count=0
    for i in list:
        if(i==-1):
            count=count+1
    return count
#maximum marks
def max(list):
    max=list[0]
    for i in list:
        if(i>max):
            max=i
    return max
#minimum marks
def min(list):
    min=list[0]
    for i in list:
        if(i<min):
            min=i
    return min
#sum of marks 
def sum(list):
    sum=0
    for i in list:
        sum+=i
    sum=sum+absent(list)
    return sum
#average marks
def average(list):
    average=(sum(list)+absent(list))/(n-absent(list))
    return average
#highest frequency
def frequency(list):
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    for i in list :
        if(i>=1 and i<=10):
            count1+=1
        elif(i>=11 and i<=20):
            count2+=1   
        elif(i>=21 and i<=30):
            count3+=1
        elif(i>=31 and i<=40):
            count4+=1
        elif(i>=41 and i<=50):
            count5+=1
    return(count1,count2,count3,count4,count5)

print("Marks of the students are :",list)
print("No. of absent students are :",absent(list))
print("Maximum marks are:",max(list))
print("Minimum marks are:",min(list))
print("average marks of all student are:",average(list))
print("maximum frequency of marks is:",max(frequency(list)))
