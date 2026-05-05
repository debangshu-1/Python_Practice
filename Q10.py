number = float(input("Enter a float number = "))

integer_part = int(number)          
decimal_part = number - integer_part 

print(f"Integer part = {integer_part} and decimal part = {decimal_part : .6f}")