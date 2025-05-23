def factorial(num):
    if num==0 or num==1:
        return 1
    else:

        return (num)*factorial(num-1)


print(factorial(3))
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))

def fibonnaci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)
n=int(input("Enter the value of n:"))
print("Result",fibonnaci(n))