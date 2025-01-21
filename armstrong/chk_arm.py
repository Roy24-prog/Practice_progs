
num = int(input("Enter a number: "))
print("num = ",num)
temp = num
check = num
dig = 0
sum = 0
power = 0
print("Now splitting the digits of num...")

while temp > 0 :
   dig = int(temp % 10)   
   temp = int(temp / 10)
   power = power + 1 

ctr = power
print("Power as num of digits: ",power)

while ctr > 0 :
   dig = int(num % 10)   
   num = int(num / 10)
   sum = sum + pow(dig,power)
   print(">>> doing iteration", ctr, "... ")
   print("dig : ", dig)
   print("num :", num)
   print("sum :", sum)
   ctr = ctr-1
  
print("Prepared value for comparison: ", sum)
check = bool(check-sum)
print("Failcheck (bool) : ", check)
if (check==False):
   print(">>>Numbers Matched!! You've found an armstrong number")
 
   
input("Press over...")