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

# Angelina Gonzalez
def decoder(encoded_password): # decodes password
  new_password = ''

  for element in encoded_password: # goes through each element
    new_num = int(element)
    new_num -= 3 # subtracts 3
  
    if new_num < 0:
      new_num += 10 # adds 10 if number becomes negative
  
    new_password += str(new_num) # adds in string
  
  return new_password # returns str


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
            print("The encoded password is ", encoded_password, ", and the original password is ", decoder(encoded_password), ".") 

        elif user_input == 3:
            break
