import os
cwd_path = os.getcwd()

def read_data(file_name, custom_idx):
    row = []
    if os.path.isfile(file_name):
        file_path = os.path.join(cwd_path, file_name)
        with open(file_path, "r", encoding = "utf-8") as file_name:
            for index_radku, radek in enumerate(file_name):
                radek = radek.strip("\n")
                if index_radku == custom_idx:
                    row.append(radek)
                    for i in row:
                        string = i
                        string = string.lower()
                        string = string.strip(".!")
                        row = string.split()

    else:
        return None

    return row

def tokenize(row):
    seznam_prevedenych_cisel = []
    for pismeno in row:
        prvni = pismeno[0]
        prevedeno = ord(prvni)
        seznam_prevedenych_cisel.append(prevedeno)
    return seznam_prevedenych_cisel

def main():
    pass
    file_name = "famous_quotes.txt"
    result = read_data(file_name, 1)
    print(result)
    # read data
    result_2 = tokenize(result)
    print(result_2)
    # sort sequence

if __name__ == "__main__":
    main()
