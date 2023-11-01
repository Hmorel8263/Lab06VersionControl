# Hector Morel

def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')

def encoder(password):

    new_password = ""

    for number in password:
        new_num = int(number)
        new_num -= 3

        if new_num > 9:
            new_num -= 10

        new_password += str(new_num)

    encoded_message = str(new_password)

    return encoded_message

if __name__ == '__main__':

    condition = True

    while condition:

        menu()
        user_input = int(input("Please enter an option: "))

        if user_input == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!")

        elif user_input == 2:
            print("The encoded password is ", encoded_password, ", and the original password is ", ) #Put the rest of the decoder here

        elif user_input == 3:
            break
