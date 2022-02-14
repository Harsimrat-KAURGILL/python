#q1
string=input('Enter a string:')
character=input('Enter the character to check its frequency:')
count=0
for i in string:
    if i==character:
        count+=1
print(character,'occurs',count,'times')
    

#Q2
[23:45, 14/02/2022] Simrat Gill: Day = int(input("enter day "))
Month = int(input("enter month "))
Year = int(input("enter year "))

if 1<=Day<30 and Month != 2:
    date = Day +1
    print("Next Date is:",date,"/",Month,"/",Year)
elif Day == 31 and Month == 12:

    date = 1
    mon = 1
    yr = Year +1
    print("Next Date is:",date,"/",mon,"/",yr)
elif Day == 30 and Month == 4 or 6 or 9 or 11:
    date = 1
    mon = Month +1
    print("Next Date is:",date,"/",mon,"/",Year)
elif Day == 28 and Month == 2:
    if Year%4 != 0:
        date = 1
        mon = Month +1
        
    else:
        if Day == 28:
            date = 29
            print("Next Date is:",date,"/",Month,"/",Year)
        else:
            date = 1
            mon = Month +1
            print("Next Date is:",date,"/",mon,"/",Year)
        
    


else:
    date = 1
    mon = Month + 1
    print("Next Date is:",date,"/",mon,"/",Year)

#q3
list1=[2,5,9]
new_list=[]
for i in list1:
    new_tup=(i,i**2)
    new_list.append(new_tup)
print(new_list)

#q4
points=int(input('Enter your points:'))
if (points==10):
    grade='A+'
    perf='Outstanding'
elif(points==9):
    grade='A'
    perf='Excellent'
elif(points==8):
    grade='B+'
    perf='Very good'
elif(points==7):
    grade='B'
    perf='Good'
elif(points==6):
    grade='C+'
    perf='Average'
elif(points==5):
    grade='C'
    perf='Below Average'    
elif(points==4):
    grade='D'
    perf='Poor'
else:
    print('error')
#if anything except the given points is entered ,error will be shown
print('Your Grade is:',grade ,'and you performance is',perf)

#q5
#the pattern is upto J so range is upto 11
n=11
alphabets='ABCDEFGHIJK'
for i in range(n):
      if (i*2)<n:
        j=alphabets[:n-(i*2)]
        print(' '*i,j)


#q6
students={}
while True:
    name=input('Enter the name:')
    sid=input('Enter SID:')
    students[sid]=name
    p=input('Do you want to add more elements in the list?(Enter "Y" for yes and "N" for no)')
    if p=='Y':
        continue
    elif p=='N':
        break
#a
print('Student details=',students)
#b
a=sorted(students.items(),key=lambda x: x[1])
print(a)
#c
print('Sorted dictionary using SID:')
for i in sorted(students):
    print((i,students[i]),end=" ")
print()
sid1=input('Enter SID from dictionary to search for the corresponding names:')
print('Print name of the student using SID:',(sid1,students[sid1]))
      
#Q7
n=int(input('Enter number of terms:'))
n1=0
n2=1
sum=0
count=0
if n<0:
    print('invalid input')
elif n==1:
   print(n1)
else:
    while count<n:
        print(n1)
        nth=n1+n2
        sum=sum+n1
        n1=n2
        n2=nth
        count=count+1
print('\n')
print('average=',sum/n)
    



#Q8
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}
#A 
newset_a=(set1|set2)-(set1&set2)
print(newset_a)
#B
newset_b=(set1|set2|set3)-(set1&set2)-(set2&set3)-(set3&set1)
print(newset_b)
#C
newset_c=(set1&set2)|(set2&set3)|(set1&set3)-(set1&set2&set3)
print(newset_c)
#D for integers not in set1
set4=set()
for i in set1:
    if i>=1 and i<=10:
        set4.add(i)
    newset_d=set(list1)
    print(set4)
#E for integers not in set1 set2 and set3
set5=set()
for i in (set1|set2|set3):
    if i>=1 and i<=10:
        set5.add(i)
    print(set5)
    
      

















            
