import math
from sympy import isprime


# Exercise 1: Calculate the area of a circle
ex1_radius = input("Enter circle radius?: ")
ex1_area = round(math.pi, 2) * (float(ex1_radius) ** 2)
print(f"Circle area = {ex1_area}")


# Exercise 2: Convert Celsius to Fahrenheit
ex2_celsius = input("Enter the temperature in Celsius?: ")
ex2_fahrenheit = round((float(ex2_celsius) * 9 / 5) + 32, 1)
print(f"{ex2_celsius} (C) = {ex2_fahrenheit} (F)")


# Exercise 3: Check whether a number is prime
ex3_num = input("Enter a number? ")
if isprime(int(ex3_num)):
    print(f"{ex3_num} is a prime number")
else:
    print(f"{ex3_num} is not a prime number")


# Exercise 4: Check whether a number is perfect
ex4_num = int(input("Enter a number? "))
ex4_divisor_sum = 0
for ex4_i in range(1, ex4_num):
    if ex4_num % ex4_i == 0:
        ex4_divisor_sum += ex4_i
if ex4_divisor_sum == ex4_num and ex4_num > 0:
    print(f"{ex4_num} is a perfect number")
else:
    print(f"{ex4_num} is a NOT perfect number")


# Exercise 5: Find a colour in a list
ex5_colors = ["White", "Black", "Blue", "Red"]
ex5_favourite_color = input("What is your favourite color? ")
if ex5_favourite_color in ex5_colors:
    print(
        f"Your color is at index {ex5_colors.index(ex5_favourite_color)} "
        "in my list"
    )
else:
    print("Sorry, I could not find your color")


# Exercise 6: Display range sequences
print("Name   | Sequence")
print("-" * 35)

print("range1:", list(range(7)))
print("range2:", list(range(1, 11, 3)))
print("range3:", list(range(5, 0, -1)))
print("range4:", list(range(6, -3, -2)))


# Exercise 7: Remove dollar signs from a price

def ex7_remove_dollar(ex7_string):
    return ex7_string.replace("$", "")


ex7_price = "$1,500.00"
ex7_clean_price = ex7_remove_dollar(ex7_price)
print(ex7_clean_price)


# Exercise 8: Extract even numbers from a list

def ex8_extract_even(ex8_list):
    return [ex8_item for ex8_item in ex8_list if ex8_item % 2 == 0]


ex8_sample_list = [1, 4, 5, -1, 10]
ex8_even_numbers = ex8_extract_even(ex8_sample_list)
print(ex8_even_numbers)


# Exercise 9: Calculate a factorial

def ex9_calculate_factorial(ex9_n):
    if ex9_n == 0:
        return 1

    ex9_factorial_result = 1
    for ex9_i in range(1, ex9_n + 1):
        ex9_factorial_result *= ex9_i
    return ex9_factorial_result


# Exercise 10: Find the divisors of a number

def ex10_get_divisors(ex10_n):
    return [ex10_i for ex10_i in range(1, ex10_n + 1) if ex10_n % ex10_i == 0]


ex10_number = 15
ex10_divisors = ex10_get_divisors(ex10_number)
print(ex10_divisors)


# Exercise 11: Calculate the distance between two points

def ex11_calculate_distance(ex11_x1, ex11_y1, ex11_x2, ex11_y2):
    return math.sqrt((ex11_x2 - ex11_x1) ** 2 + (ex11_y2 - ex11_y1) ** 2)


ex11_distance = ex11_calculate_distance(3, 4, 7, 7)
print(f"The distance is: {ex11_distance}")


# Exercise 12: Print a rectangular pattern

def ex12_print_pattern(ex12_m, ex12_n):
    for ex12_i in range(ex12_m):
        for ex12_j in range(ex12_n):
            if (
                ex12_i == 0
                or ex12_i == ex12_m - 1
                or ex12_j == 0
                or ex12_j == ex12_n - 1
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


ex12_print_pattern(4, 5)
