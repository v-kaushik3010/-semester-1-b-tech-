n= int(input("enter the number n:  "))
r= int(input("entre thr value of r:  "))

def factorial(n):
    sample = 1
    for i in range (1,n+1):
        sample=sample*i
    return(sample)

k= factorial(n)/(factorial(r)*factorial(n-r))
print(k)
