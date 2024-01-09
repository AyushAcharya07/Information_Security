def perform_operations(input_string):
    result = ""
    for char in input_string:
        # Convert character to its ASCII value
        ascii_value = ord(char)

        # Perform bitwise AND and XOR operations with 127
        and_result = ascii_value & 127
        xor_result = ascii_value ^ 127

        # Convert the results back to characters and append to the result string
        result += f"Character: {char},\tASCII: {ascii_value},\t\tAND Result: {and_result},\t\tXOR Result: {xor_result}\n\n"

    return result


input_str = "\Hello-World"
output = perform_operations(input_str)
print(output)
