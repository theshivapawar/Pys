# 2. Sum of digits of a number

number = 123

first_digit = number % 10
number //= 10

second_digit = number % 10
number //= 10

third_digit = number % 10
number //= 10

sum_of_digits = first_digit + second_digit + third_digit
print(f'Sum: {first_digit} + {second_digit} + {third_digit} = {sum_of_digits}')

number = int(input('Number: '))

sum_of_digits = 0
while number != 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

print(f'Sum: {sum_of_digits}')