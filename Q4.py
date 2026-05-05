num_string = input("Enter an integer = ")

num_int = int(num_string)
print(f"{num_int} => {type(num_string)}")

num_float = float(num_int)
print(f"{num_float} => {type(num_float)}")

num_str = str(num_int)
print(f"'{num_str}' => {type(num_str)}")