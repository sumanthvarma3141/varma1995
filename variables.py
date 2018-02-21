#prime numbers
# Python program to check if the input number is prime or not

#num = 407

# take input from the user
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")

#fibonic series
# Program to display the Fibonacci sequence up to n-th term where n is provided by the user

# change this value for a different result
#nterms = 10

# uncomment to take input from the user
nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

#palindrome
    #check the number
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")





# Python program to check if the number provided by the user is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


#Display no of armstrong numbers
while True:
	print("Enter 'x' for exit.")
	print("Enter the interval (starting and ending number): ")
	start = input()
	end = input()
	if start == 'x':
		break
	else:
		lower = int(start)
		upper = int(end)
		for num in range(lower, upper+1):
			tot = 0
			temp = num
			while temp != 0:
				dig = temp % 10
				tot += dig ** 3
				temp //= 10
			if num == tot:
				print(num)
		print("\n")
