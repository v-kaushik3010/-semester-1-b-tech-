# arm strong number 
#example:: 371 = 3**3 + 7**3 + 1**3 == 371 then arm strong number

num = int(input("enter your number::"))
length = len(str(num))
sum_of_cubes = 0
temp = num
while temp>0:
    digit = temp % 10
    sum_of_cubes += digit**length
    #or sum_of_cubes = sum_of_cubes+digit**length        
    temp //= 10
if (num == sum_of_cubes):
    print(num,"is armstrong number ")
else: 
    print(num,"is not armstrong number")