#q3      


s1="nice to have it"
s2="here"
print(s1,s2)



#q4


a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])


#q5


a[0]=s1
a.append(s2)
print(a)


#q6



numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]

for a in numbers:
    if a%2==0 and a<238:
        print(a)



#q7


color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

print(color_list_1 - color_list_2)


#q8


s = input("Enter the string: ")
l = list(range(65,91))           
for i in s.upper():             
    if ord(i) in l:              
        l.remove(ord(i))        

if len(l) == 0:                  
    print(f"{s} is a Pangram.")
else:                            
    print(f"{s} is not a Pangram.")


#q9

n=input('num:')
a=int(n)
b = a*10 + a
c = a*100 + a*10 + a
print(a+b+c)

#q10

string1=eval(input("Enter string in the given fashion"))     
string1=string1.strip()
string1+=" "
num=""
x=[]
y=[]
flag=0
for i in string1:
    if(i!=" "):
        if(i!="#"):
            num+=i
        else:
            flag=1
            x.append(int(num))
            num=""
    
    else:
        if(flag==0):
            x.append(int(num))
            num=""
        else:
            y.append(int(num))
            num=""
print(x)
print(y)


#q11

a=input('enter sequence of words:').split(',') 
a.sort()                                       
print(a)


#q12

d={'student': ['rahul','kishore','vidhya','raakhi'],'Marks':[57,87,67,79]}
mx = max(d['Marks'])
i = d['Marks'].index(mx)                    
print(d['student'][i])
  



#q13

str=(input("enter the sentence"))
l=0
d=0
for i in str:
    if(i.isalpha()):
        l+=1
    if(i.isdigit()):
        d+=1
print(l,d)


#q14



d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'], 'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'], 'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
sub = input('enter the subject:')
newData = {'Name' : [], 'Subject' : [], 'Ratings' : []}
for i in range(len(d['Name'])):
    s = d['Subject'][i] 
    if s == sub:
        newData['Name'].append(d['Name'][i])
        newData['Subject'].append(d['Subject'][i])
        newData['Ratings'].append(d['Ratings'][i])
print(newData)

