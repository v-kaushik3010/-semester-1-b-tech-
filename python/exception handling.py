a=[1,2,3]
try:
    print("second element=" ,(a[1]))
    print("fourth element=%d" %(a[3]))

except:
    print("an error occured")

def fun(a):
    if a<=4:

        b=a/(a-3)
    print("value of b=",b)

try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("zero  division error occured")
except NameError:
    print("name error occured")
else:
    print("it will work only if except statemenr doenot raise an error ")
finally:
    print("it wll always executed")