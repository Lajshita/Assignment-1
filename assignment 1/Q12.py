num = int(input("Enter the number = "))

sum_digits = 0

while num > 0 :
    sum_digits += num % 10
    num //= 10
print(f"The sum of digits is {sum_digits}")    