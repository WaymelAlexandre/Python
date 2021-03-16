

#Write a program that asks the user for their name, checks if their name is either "frank" or "george" and if it is, greet them by their name.

# name = input("Hi there what is you name pleas? \n")

# if name == "frank" or name == "george":
#     print(f"Hello {name}")
# else:
#     print(f"Hello {name}")

#Write a program that asks the user for their year of birth, checks if they are of legal drinking age, and tells the user to come into the bar. Example:



# Year = int(input("What is tou Year Of Birth"))
# totalAge = 2121 - Year 

# if totalAge < 18 :
#     print("\n Come in and have a drink! \n ")
# else:
#     print("Go away. Child.")

# # Write a program that could be used for an (unsecure) login, with a username and password. For example:








credenciel = [
    {
        'name': "bob",
        'passworld':  "passwoprld1234"
    },
    {
        'name': "fred",
        'passworld':  "happyPass122"
    },
    {
        'name': "lock",
        'passworld': "passwithlock44"
    }

]


search = input("What is your name?")
passworlInput = input("What is your passworld?")
for x in range(len(credenciel)):
    if search.lower() in credenciel[x]['name'].lower():
        if credenciel[x]['passworld'].lower() == passworlInput:

            print('name: ',credenciel[x]['name'])
            print('passworld: ', credenciel[x]['passworld'])
            break
else:
    print('Invalid Entry!')
 


# credenciel0 = {
#     "name": "bob",
#     "passworld": "passworld1234"
# }
# credenciel1 = {
#     "name": "fred",
#     "passworld": "passworld1234"
# }
# credenciel2 = {
#     "name": "lock",
#     "passworld": "passworld1234"
# }






# credencielList = [credenciel0, credenciel1, credenciel2]


# userNameInput = input("whatis your name? ")

# for x in credencielList:
#     for x1 in x:
#         if slice(credencielList[x1]) == slice(userNameInput): 
#             print("okokokok")
#         else:
#             print("nobody by this name ")




    # if 
    #     if credenciel["name"] == nameInput:
    #         print("ok")
    #     else:
    #         print("no name in the database ")


