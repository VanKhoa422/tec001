p_list=[]
num=int(input("Enter the number: "))
for i in range (1, num):
    if num%i==0:
        p_list.append(i)
p_list.append(num)
if len(p_list)<=2:
    print(num, "is a prime number!")
else:
    print(num, "is not a prime number and divisible to ", p_list)