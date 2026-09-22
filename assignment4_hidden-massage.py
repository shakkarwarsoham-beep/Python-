substring = input("Enter secret message: ")
string = input("Enter coded message: ")

if substring in string:
    print("Secret message found")
else:
    print("Secret message not found")