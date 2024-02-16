def perform_operations(input_string):
    result = ""
    and_characters = ""
    xor_characters = ""
    and_binary = ""
    xor_binary = ""

    for char in input_string:
        ascii_value = ord(char)

        and_result = ascii_value & 127
        xor_result = ascii_value ^ 127

        # Converting the results back to characters and append to the result string
        result += f"Character: {char},      ASCII: {ascii_value},      AND Result: {chr(and_result)},    XOR Result: {chr(xor_result)}\n"

        and_characters += chr(and_result)
        xor_characters += chr(xor_result)

    # Converting AND and XOR results to binary
    for char in and_characters:
        and_binary += format(ord(char), '08b') + " "
    for char in xor_characters:
        xor_binary += format(ord(char), '08b') + " "

    result += f"\nCharacters after AND: {and_characters}\n"
    result += f"Characters after XOR: {xor_characters}\n"
    result += f"\nBinary results of AND: {and_binary}\n"
    result += f"Binary results of XOR: {xor_binary}\n"

    return result

print("*"*50)
input_str = r"\\Hello-World"
print("\nPerforming AND & XOR Operations on the input string with 127:\n")
print("*"*50,"\n")
output = perform_operations(input_str)
print(output)
