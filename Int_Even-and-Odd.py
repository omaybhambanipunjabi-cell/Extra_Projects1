n = int(input("Enter how many integers you want to input: "))

numbers = []

for i in range(n):
    num = int(input("Enter integer {i+1}: "))
    numbers.append(num)


even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
