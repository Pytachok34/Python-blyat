import os


def text_from_file(filename):
    error = "0"
    text = ""
    if os.path.exists(filename) and os.path.isfile(filename):
        if filename.endswith(".txt"):
            try:
                file = open(filename, "r")
                text = file.read()
                file.close()
            except:
                error = "File not opened"        
        else:
            error = "Wrong file name!"
    else:
        error = "There are no file with that name!"

    return error, text
