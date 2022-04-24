ORD_A = ord('a')
ALPHABET_LENGTH = ord('z') - ORD_A + 1 

def caesar_cipher_breaker(message_encoded, decoded_substring):
    """
    Breaks the Caesar cipher using the alphabet a-z and a known deciphered substring
    :param str message_encoded: Encrypted message, can contain extra characters that are not in the encoding alphabet
    :param str decoded_substring: Small part of the decrypted message
    :rtype: (str)
    :return: A string with the decrypted message
    """
    message_output = "invalid message"

    for shift in range(ALPHABET_LENGTH):

        message_decoded = ""

        for letter in message_encoded:

            idx = ord(letter) - ORD_A

            if 25 < idx or 0 > idx:
                continue

            idx = idx + shift
            idx = idx % ALPHABET_LENGTH
            letter = chr(idx + ORD_A)
            message_decoded = message_decoded + letter

        if decoded_substring in message_decoded:
            message_output = message_decoded
            break

    return message_output

if __name__ == "__main__":
    message = ',ew785dbk785Hweh./,gmFral2C745kadf785wbXkak.///,.axj785m'
    known_substring = 'pou'
    print('Zasifrovana zprava je:', message)

    message_deciphered = caesar_cipher_breaker(message, known_substring)

    print('Rozsifrovana zprava je:', message_deciphered)
