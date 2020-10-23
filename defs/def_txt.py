"""文本处理函数库"""

def watch_txt(filename):
    """watch txt and read"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        message = "Sorry, the file " + filename + " does not exist."
        print(message)
    else:
        print(contents)


def word_time(filename):
    """read one word of all time"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        message = "Sorry, the file " + filename + " does not exist."
        print(message)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about" + str(num_words) +
            " words.")


def one_word_time(filename, word):
    """read one word of all time"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        message = "Sorry, the file " + filename + " does not exist."
        print(message)
    else:
        word_time = contents.lower().count(str(word))
        print("The word '" + str(word) + "' in the file '" + filename + "' has about " + 
            str(word_time) + " time.")