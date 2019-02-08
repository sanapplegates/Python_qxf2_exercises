
""" Finding palindrome
of n numbers"
"""
num = int(input("enter a number: "))
 
temp = num
reverse = 0
while temp != 0:
	reverse = (reverse * 10) + (temp % 10)
	temp = temp // 10
 
if num == reverse:
	print("number is palindrome")
else:
	print("number is not palindrome")
