num = int(input("Enter the number to get the sum"))

sum = 0
i = 1

while i<=num:
  sum = sum+i
  i = i + 1 
  print (sum)
print("Total sum = ", sum)

print("============================================")
print("Now we will get reverse counting of a number.")

print("============================================")

num = int(input("Enter the number for reverse counting.."))

while num>0:
  num = num-1
  print(num)
