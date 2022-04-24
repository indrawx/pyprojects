def get_message():
    """
    Function for receiving a message from a user that he wants to encrypt or decrypt
    :return: (string) message from user
    """
    message = input("Set the text for encryption / decryption: ")
    return message

def get_key():
    """
    Function for getting the encryption key from the user
    :return: (int) the number of symbols for moving in message
    """
    while 1:
        try:
            key = int(input("Enter the key: "))
            break
        except ValueError:
            print("Something went wrong")
        else:
            print("Nothing went wrong")

    return int(key)

def make_choice():
    """
    The function asks the user what operation he wants to perform with the message
    :return: (bool) what operation user wants to do
    """
    choice = input("Which operation you want to do: ")
    while 1:
        if choice == 'sifrovat':
            return True
            break
        elif choice == 'desifrovat':
            return False
            break
        else:
            choice = input("Which operation you want to do: ")

def cipher(message, key, choice):
    """
    Function for encrypting and decrypting messages
    :param message: (str) message from user
    :param key: (int) the number of symbols for moving in message
    :param choice: (bool) what operation user wants to perform with the message
    :return: (string) encryption/decryption message
    """
    key = key % 26
    if choice == True:
        cipherText = ""
        for i in message:
            if i.isalpha():
                stay_in_alphabet = ord(i) + key
                if (ord(i) <= ord("Z") and stay_in_alphabet > ord('Z')) or (
                        ord(i) >= ord("a") and stay_in_alphabet > ord('z')):
                    stay_in_alphabet -= 26
                final_letter = chr(stay_in_alphabet)
                cipherText += final_letter
            else:
                cipherText += i

        return cipherText

    if choice == False:
        decipherText = ""
        for j in message:
            if j.isalpha():
                stay_in_alphabet = ord(j) - key
                if (ord(j) <= ord("Z") and stay_in_alphabet < ord('A')) or (
                        ord(j) >= ord("a") and stay_in_alphabet < ord('a')):
                    stay_in_alphabet += 26
                final_letter = chr(stay_in_alphabet)
                decipherText += final_letter
            else:
                decipherText += j

        return decipherText

def main():
    """
    Driver function
    :return: (string) encryption/decryption message
        """
    message = get_message()
    key = get_key()
    choice = make_choice()
    str = cipher(message, key, choice)
    print("Caesarova šifra: ", str)

    return str

if __name__ == "__main__":
    main()
