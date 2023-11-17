# outputs fizzbuzz if a number is divisible by 3 and 5, 
# fizz if it is divisible by 3, and buzz if it is divisible by 5.
# otherwise, it outputs the number.
# For this challenge you need to write a computer program that will display all the numbers between 1 and 100.
def fizzbuzz(number):
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)

print(fizzbuzz(100))