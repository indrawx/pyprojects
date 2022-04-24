SPAM_KEYWORDS = [
    ('buy', 10), ('free', 5), ('call', 12), ('text', 4), ('now', 7), ('win', 19), ('winner', 19), ('claim', 13)
]
PUNCTUATION = [".", ",", "!", "?", ":", "\'"]

def remove_punctuation(stroka):
    for i in range(len(PUNCTUATION)):
        s = PUNCTUATION[i]
        stroka = stroka.replace(s, '')

    if stroka == "":
        return None

    return stroka

def string_parser(string, delimiter=' ', to_remove=('the', 'in', 'at', 'for', 'an', 'from', 'to', 'with')):
    """
    :param string: (str): chain containing words separated by a space with deleted interpunction
    :param delimiter: (str): dividing string
    :param to_remove: (tuple): n-trix words to delete
    :return: filtered_words: (list): filtered list of separate words reworked into small letters,
    """
    string = string.lower()
    words = string.split(delimiter)
    filtered_words = []
    for word in words:
        if (word not in to_remove) and (len(word) > 1):
            filtered_words.append(word)
        else:
            continue

    return filtered_words

def detect_spam(words, score_limit=15):
    spam_skore = 0
    for word in words:
        for i in SPAM_KEYWORDS:
            if word == i[0]:
                spam_skore += i[1]

    if spam_skore >= score_limit:
        return True, spam_skore
    else:
        return False, spam_skore


def main(messages, score_limit):
    spam_results = list()

    if messages == "":
        return []

    return spam_results

if __name__ == '__main__':
    with open('messages.txt', "r") as file_opener:
        message_collection = [line.rstrip('\n') for line in file_opener]

    results = main(message_collection, score_limit=15)
    print(results)
