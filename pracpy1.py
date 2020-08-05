filobj=open("recipt.txt","w")
filobj.write("Khan General stores \n")
sum=0
database=[]
while(True):
    User_Input=input("Enter the Item price or press q to quit : \n")
    database.append(User_Input)
    filobj.writelines(User_Input)
    if User_Input !="q" :
        sum+=int(User_Input)
        print(f"Your order total so far {sum}")

    else:
        print(f"Your Bill Total is {sum}.Thank you for shopping with us")
        break
