'''num_rows = int(input("enter number of rows::"))
for i in range(0,num_rows+1):
    print("*" * i)'''




'''#reverse pyramid
num_rows = int(input("enter number of rows::"))
for i in range(num_rows, 0, -1):
    print("*" * i)'''

'''n = int(input("no of rows:: "))
for row in range (1,n+1):
  for col in range (1,row+1):
      print('*',end='')
  print()'''


n = int(input("enter the number of rows:: "))
for  row in range(1,n+1):
    for space in range(1,n-row+1):
      print(" ",end = " ")
    for star in range(n-row+1, n+1):
       print("*", end=" ")
    print()
