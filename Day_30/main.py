## File does not found error
# with open('a_file.py', "r") as file:
#     file.read()

## KeyError: 'does_not_exist'
# a_dict = {"key": "value"}
# value = a_dict["does_not_exist"]

## Index Error
# arr = [0,1,2]
# selected = arr[4]

## Type Error
# text = "abc"
# print(text + 5)

try :
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    value = a_dict["not_exists"]
    arr = [0, 1, 2]
    selected = arr[40]
    print(selected)
except FileNotFoundError:
    print("There was an error as reading a file so creating a file")
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError :
    print("Key Error as key is not available")
except IndexError as error_message:
    print(f"Invalid index {error_message}")
else:
    print("Everything is Ok!")
    content = file.read()
    print(content)
finally:
    file.close()
    print("File is closed")
    # raise TypeError("This is the error I made!")