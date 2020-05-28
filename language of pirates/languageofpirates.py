#my_input = input("Enter the string: ")
my_input = "he is a good! .man"
def first_digit_to_end(my_input):
    splitted = my_input.split(" ")
    added = [item[1:] + item[:1] + "arg" for item in splitted]

    final = ""
    for item in added:
        special = ""
        alphanum = ""
        for char in item:
            if char.isalnum():
                alphanum = alphanum+char
            else:
                special = special + char
        final = final + alphanum + special + " "
    return final    

print(first_digit_to_end(my_input))