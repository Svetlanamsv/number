print("Enter two-digit number")
a=int(input())

dezons = a//10
numbers = a%10

print(dezons)
print(numbers)

print("Enter three-digit number")
b=int(input())

b_hundreds=b//100
b_dezons=(b%100)//10
b_numbers=(b%100)%10
print(b_hundreds)
print(b_dezons)
print(b_numbers)
