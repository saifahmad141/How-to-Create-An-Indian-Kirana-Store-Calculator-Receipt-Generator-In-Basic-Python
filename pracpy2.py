"""
def fact():
    factorial = 1
    user_input=int(input("enter the number for factorial : \n"))
    for i in range(1,user_input+1):
        factorial=factorial*i
    print(factorial)
fact()
"""
def fact(number):
    if number==0 or number==1:
        return 1
    else:
        return number * fact(number-1)
number=int(input("enter the number : \n"))
fac=fact(number)
print(f"the factorial is {fac}")

"""
    fac=fact(number)
    count=0
    while (fac %10==0):
        count+=1
        fac=fac/10
    print(f"the factorial trailing zeros are {count}")
facs=FactTrailingZeros(number)
"""
def FactTrailingZeros(numbers):
    count=0
    i=5
    while(numbers//i!=0):
        count+=int(numbers//i)
        i=i*5
    return count
numbers=int(input("enter the number: \n"))
facs=FactTrailingZeros(numbers)
print(f"the factorial trailing zeros are {facs}")





