print('Q U E S T I O N  1')
# Defining tower of Hanoi function
def hanoi_twr(n , start, finish, auxiliary):
    if n==1:
     print ('Move disk 1 from ',start,'to',finish,)
     return
    
    hanoi_twr(n-1, start, auxiliary, finish)

    print ('Move disk',n,'from',start,'to',finish)

    hanoi_twr(n-1, auxiliary, finish, start)


# taking number of disk input from the user
disk=int(input('Enter number of disk in tower of Hanoi:'))

# Using the function of hanoi tower
hanoi_twr(disk,'Source Tower','Destination','Auxiliary')



print('Q U E S T I O N  2')
print('using recursive method')
n = int(input('Enter the number of rows :'))
def pascalstriangle(num):
    if num == 1:
        return [[1]]
    else:

        result = pascalstriangle(num-1)
        present_row = [1]
        previous_row = result[-1]

        for i in range(len(previous_row)-1):

            present_row.append(previous_row[i] + previous_row[i+1])

        present_row += [1]

        result.append(present_row)
    return result

for i in pascalstriangle(n):

    print((n-len(i))*"  ", end=" ")

    for j in i:

        print(j, end="   ")
    print()
print('using itlerative method')
#number of rows
n=int(input('Enter the number of rows:'))
for p in range(1, n+1):
    print('  '*(n - p), end='')

    x = 1
    for i in range(1, p+1):

        print(x, end='   ')

        x = x * (p - i) // i
    print()
print("")


print('Q U E S T I O N  3')
n1=int(input('enter a number:'))
n2=int(input('enter another number:'))
t=divmod(n1,n2)
list1=list(t)
#first element of list will be quotient
quot=list1[0]
#second element of list will be remainder
rem=list1[1]
print('the quotient after dividing',n1,'with',n2,'is:',quot)
print('the remainder after dividing',n1,'with',n2,'is:',rem)
print('part a')
#checking is the function is callable or not
c=callable(divmod(n1,n2))
if c==True:
    print('the function is callable')
else:
    print('the function is not callable')
    
print('part b')
if 0 in list1:
    print('all results are not non zero')
else:
    print('all results are non zero')
    
print('part c')
list2=[quot,rem]
list3=list()
#adding (4,5,6)to the list
for k in range (4,7):
    list2.append(k)
print('new list after adding (4,5,6)):',list2)
#creating a list with numbers greater than 4    
for i in list2:
    if i>4:
        list3.append(i)
print('new list with values greater than 4:',list3)

print('part d')
#converting list to set
set1=set()
for p in list3:
    set1.add(p)
print('previous result in set form:')
print(set1)

print('part e')
#making the set immutable
frozenset(set1)
print('the set is now immutable')

print('part f')
#finding max and hash value from the set
max_set=max(set1)
hash_set=hash(max_set)
print('maximum value of set:',max_set)
print('hash value of set:',hash_set)



print('Q U E S T I O N  4')
class Student:
    def __init__(self,name,age):
        #initializing data members
        self.name=name
        self.age=age
        print('object p1 is created')
    def __del__(self):
        print('the created object is destroyed')
    def details(self):
        print('name is:',self.name)
        print('age is:',self.age)
        #creating object p1
        #instructor __init__() called
p1=Student('john',36)
#calling details function to print name and age
p1.details()
#deleting object p1
#destructor __del__() called
del p1


print('Q U E S T I O N  5')
class employees:
    def __init__(self,name,salary):
        #initializing data members
        self.name=name
        self.salary=salary
    def __del__(self):
        print('record of employee viren is deleted')
    def details(self):
        #printing details
        print('name:',self.name)
        print('salary:',self.salary)
#creating objects p1,p2,p3
p1=employees('mehak',40000)
p2=employees('ashok',50000)
p3=employees('viren',60000)
#printing the given data
print('given details of the employees')
#calling details() to print individual details of objects p1,p2,p3
p1.details()
p2.details()
p3.details()
print('details of the employees after changes')
print('part a')
#modifying salary of employee mehak
p1.salary=70000
p1.details()
p2.details()
print('part b')
#deleting object
del p3


print('Q U E S T I O N  6')
def game(w1,w2):
    #making the words in lowercase
    w1=w1.lower()
    w2=w2.lower()
    #initialising list to store more elements
    list1=[]
    list2=[]
    for i in w1:
        list1.append(i)
    for j in w2:
        list2.append(j)
    #sorting lists in alphabetical ordere    
    list1.sort()
    list2.sort()
    #checking if they passed or failed the test
    if list1==list2:
        return True
    else:
        return False
#player names    
player1=str('barbie')
player2=str('george')
#taking input words from each player
str1=str(input(f'enter word by {player1}:'))
str2=str(input(f'enter word by {player2}:'))
#calling game()
final=game(str1,str2)
#printing the final result
if final==True:
    print('they passed the friendship test')
else:
    print('they failed the friendship test')

