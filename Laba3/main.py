from TextFunctions import text_stat
from FileFunctions import text_from_file
choice = ""
while choice != "0":
    print("1. Statistics of file")
    print("0. Exit")
    choice = input("Choice: ")

    if choice == "1":
        name = input("Enter the file name with .txt: ")
        error, text = text_from_file(name)
        if error == "0":
            frequent_word, count_words, count_symbols = text_stat(text)
            print('\n')
            print("Most popular word in text: {0}\n"
                    "Amount of words in text: {1}\n"
                    "Whole number of symbols (with EndOfLine "
                    "symbol): {2}".format(frequent_word, count_words, count_symbols))
        else:
            print(error)
    elif choice != "0":
        print('You put uncorrect name')