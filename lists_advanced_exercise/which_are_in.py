def find_substrings(substrings_data, strings_data):
    substrings_result = []
    for current_substring in substrings_data:
        for current_string in strings_data:
            if current_substring in current_string:
                substrings_result.append(current_substring)
                break
    return substrings_result


substrings = input().split(", ")
strings = input().split(", ")
result = find_substrings(substrings, strings)
print(result)