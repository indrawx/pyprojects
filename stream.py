 """
    :param original_stream (str): retezec
    :return encoded_stream (str): zakodovany retezec
    """
  def rle_encoder(original_stream):

    pocet = 1
    encoded_stream = ''
    previous_char = ''
    if not original_stream:
        return ''
    for char in original_stream:
        if char != previous_char:
            if previous_char:
                encoded_stream += previous_char + str(pocet)
            pocet = 1
            previous_char = char
        else:
                pocet += 1
    else:
            encoded_stream += previous_char + str(pocet)


    print(f"Sekvence {original_stream} odpovida zakodovane sekvenci {encoded_stream}")
    return encoded_stream


if __name__ == "__main__":
    original_stream = "aaaaaahhhoooooooojj"
    rle_encoder(original_stream)
