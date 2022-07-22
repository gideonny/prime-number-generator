# This code allows users to input a desired range of numbers, and then the code creates a list of prime numbers within said range
x = int(input("What number is at the beginning of your range? "))
y = int(input("What number is at the end of your range? "))
list_of_prime_numbers = []
for num in range(x,y):
    if num > 1:

        for i in range(2, num):
            if num % i == 0:
                break
        else:
            list_of_prime_numbers.append(num)
print(list_of_prime_numbers)