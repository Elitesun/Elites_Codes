def replace_first_occurrence_and_delete_rest(input_string, old_char, new_char):
    # Find the index of the first occurrence of old_char
    index = input_string.find(old_char)
    
    if index != -1:
        # Replace the first occurrence of old_char with new_char
        modified_string = input_string[:index] + new_char
        
        # Delete the rest of the occurrences of old_char
        modified_string += input_string[index + 1:].replace(old_char, "")
        
        return modified_string
    else:
        return input_string  # Return the original string if old_char is not found

# Example usage:
input_string = "banana"
old_char = 'a'
new_char = 'x'

result = replace_first_occurrence_and_delete_rest(input_string, old_char, new_char)
print(result)  # Output: "bxn"
