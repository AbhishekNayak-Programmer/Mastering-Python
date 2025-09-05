def format_name(first_name, last_name) :
    first_name = first_name.title() # converts to capitalise
    last_name = last_name.capitalize() # converts to capitalise
    return f"{first_name} {last_name}"

print(format_name("abhiSHek", 'naYAk'))

# Callback Function

def function_1(text) :
    return text + text

def function_2 (text) :
    return text.capitalize()

output = function_2(function_1("Hello"))
print(output)


def format_name_2(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name_2(input("What is your first name?"), input("What is your last name?")))
