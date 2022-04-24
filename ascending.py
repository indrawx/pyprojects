def update_ascending_sequence(sequence, to_add_seq):
    """
    Returns updated number sequence in ascending order
    :param list sequence: Sequence of input numbers
    :param list to_add_seq: Randomized generated numbers to add to the input sequence
    :rtype: (list, int, bool)
    :return: A list with randomized numbers added to correct position of input sequence,
    value of middle element and True if middle element is a prime number
    """
    new_seq = []

    for j in range(0, len(to_add_seq)):
        i = 0
        while (sequence[i] < to_add_seq[j]) and (len(sequence) - 1 > i):
            i = i + 1
        k = 0
        f = 0
        for k in range(0, i):
            new_seq.append(sequence[k])
        if sequence[i] < to_add_seq[j]:
            new_seq.append(sequence[i])
            f = 1
        if (to_add_seq[j] != sequence[i]):
            new_seq.append(to_add_seq[j])
        if f == 0:
            for k in range(i, len(sequence)):
                new_seq.append(sequence[k])
        sequence = new_seq
        new_seq = []

    middle_element = int(((len(sequence) + 1) / 2) - 1)
    middle_element = sequence[middle_element]

    is_prime = 0
    d = 0
    for n in range(2, middle_element // 2+1):
        if middle_element % n == 0:
            d = d + 1
    if d <= 0:
        is_prime = True
    else:
        is_prime = False

    return sequence, middle_element, is_prime

if __name__ == "__main__":
    input_sequence = [2, 8, 10, 11, 12, 16, 20]
    print(f"Input sequence: {input_sequence}")
    to_add = [2, 10, 5, 6, 17]
    print(f"Random list: {to_add}")
    final_sequence, middle, is_middle_prime = update_ascending_sequence(input_sequence, to_add)
    print(f"Your merged list: {final_sequence} \nMiddle element {middle} is prime: {is_middle_prime}")
