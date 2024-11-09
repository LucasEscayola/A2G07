def count_string(string):
    count = 0  # Initialize count to zero
    for i in string:  # Loop through each character in the string
        if i != " ":  # Exclude spaces from the count
            count += 1  # Increment count for every non-space character
    return count
