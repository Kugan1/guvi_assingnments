text = input("enter a string to convert into ascii values:")
ascii_values = []
for each_char in text:
    ascii_values.append(ord(each_char))
print(ascii_values)
Sum = sum(ascii_values)
print(Sum)
