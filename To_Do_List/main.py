# Type-1:
# print("Enter a ToDo: ")
# user_text = input()
# print(user_text)

# Type-2:
# user_text = input("Enter a Todo: ")
# print(user_text)

# It is also possible to store a sentence in a variable in python.
prompt = "Enter a ToDo: "
user_text1 = input(prompt)
user_text2 = input(prompt)
user_text3 = input(prompt)

user_texts = [user_text1, user_text2, user_text3, "Hello"]  # python list

print(user_texts)

print(type(prompt))
print(type(user_texts))
