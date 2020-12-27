x=input("Please write your name:  ")
y=input("Please write your surname:  ")
z=int(input("Please write your age:  "))
c=int(input("Please write your birthyear:   "))
user_data= [x,y,z,c] 
if z>17:
    print("You can go out to the street ")
else:
    print("You can't go out because it's too dangerous.  ")
for i in (user_data):
    print(i)

    
