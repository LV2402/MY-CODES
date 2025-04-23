def check_consecutive_occurrence(s, char):
    # Count the occurrences of the character
    count = s.count(char)
    
    # Check if the character appears more than twice and all occurrences are consecutive
    if count > 2 and char * count in s:
        print("Yes")
    else:
        print("No")

# Example usage
input_string = "googoo"
character = "a"
check_consecutive_occurrence(input_string, character)
