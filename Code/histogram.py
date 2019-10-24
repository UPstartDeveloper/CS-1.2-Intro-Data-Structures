import sys
import re


def get_clean_words(file_name):
    """Get a list of single-word strings from source text.
        Param: file_name(str)
        Return: words(list)
    """
    words = []
    with open(file_name, "r") as file:
        # make a list ofd words, contains non alphabetic chars
        words = file.read().split()
        # remove all occurences of non-alpha chars from data
        clean_words = []
        for word in words:
            clean_word = ([char for char in word if not (
                char == "." or
                char == "?" or
                char == "!" or
                char == "," or
                char == ":" or
                char == ";" or
                char == "(" or
                char == ")"
            )])
            clean_words.append(clean_word)
        # make a list of whole words only containing letters
        clean_words_as_str = []
        for list_of_chars in clean_words:
            whole_word = ""
            clean_words_as_str.append(whole_word.join(list_of_chars))

    return clean_words_as_str


def create_histogram_dict(words_list):
    """Return a dictionary representing a histogram of words in a list.
       Param: words_list(list): list of strings representing words
       Return: histogram(dict): each key a unique word, values are number of
               word appearances
    """
    histogram = dict()
    words = histogram.keys()
    for word in words_list:
        if word.lower() not in words:
            histogram[word.lower()] = 1
        else:
            histogram[word.lower()] += 1
    return histogram


def find_unique_words(words_list):
    """Record all unique words in a list of strings."""
    # record all unique words
    unique_words = list()
    for word in words_list:
        if word.lower() not in unique_words:
            unique_words.append(word.lower())
    return unique_words


def create_histogram_list_of_lists(words_list):
    """Return a list to represent a histogram of word frequency in a text.
       List contains a list for each unique word in the text.
       First element in the nested list is the word; and the second element is
       the number of appearances that word makes in the text.
       Param: words_list(list): list of strings representing the text
       Return: histogram(list)
    """
    histogram = list()
    unique_words = find_unique_words(words_list)
    # generate histogram
    for word in words_list:
        # if word not recorded, make a new list for it in histogram
        if word.lower() not in unique_words:
            histogram.append([word.lower(), 1])
            unique_words.append(word.lower())
        # find the list containing non-unique words, and increment appearances
        else:
            word_index = unique_words.index(word.lower())
            histogram[word_index][1] += 1
    return histogram


def create_histogram_list_of_tuples(words_list):
    """Return the equivalent of the previous function, using tuples (instead of
       lists) nested inside a list.
    """
    histogram = list()
    unique_words = find_unique_words(words_list)
    # count up appearances of each unique word, then make tuple in histogram
    for word in unique_words:
        appearances = 0
        for word_from_text in words_list:
            if word == word_from_text.lower():
                appearances += 1
        histogram.append((word, appearances))

    return histogram


def create_histogram_inverted(words_list):
    """Create a histogram of word frequency from a source text.
       Each tuple's first element is a number representing the
       appearances of a word.
       Each value is a list of words which appear that number of times.
       Param: words_list(list)
       Return: histogram(list): contains nested tuples with nested lists
    """
    histogram = list()
    unique_words = find_unique_words(words_list)


def histogram(file_name):
    """Return a histogram of the appearances of words from a .txt file.
       Param: file_name(str): name of file with source text (.txt)
       Return: histogram(dict): every key a unique word,
               and value is appearances
               of the word in the text
    """
    words_list = get_clean_words(file_name)
    # make a dict of the data
    # histogram = create_histogram_dict(words_list)
    # histogram = create_histogram_list_of_lists(words_list)
    # histogram = create_histogram_list_of_tuples(words_list)
    histogram = create_histogram_inverted(words_list)

    return histogram


def determine_hist_type(histogram):
    """Return the data type of the histogram.
       Param: histogram: dict, list of lists, or list of tuples
       Return: str
    """
    if isinstance(histogram, dict) is True:
        # determine if keys in dict are word strings or numbers
        words_or_num = list(histogram.keys())
        if isinstance(words_or_num[0], str) is True:
            return "dict_with_str_keys"
        else:
            return "dict_with_num_keys"
    elif isinstance(histogram, list) is True:
        # determine if histogram is made of lists or tuples
        return "list"


def unique_words(histogram):
    """Return total count of unique words in a source text.
       Param: histogram(dict, list of lists, or list of tuples)
       Return: int
    """
    if determine_hist_type(histogram) == "dict_with_str_keys":
        return len(list(histogram.keys()))
    elif determine_hist_type(histogram) == "dict_with_num_keys":
        pass
    elif determine_hist_type(histogram) == "list":
        return len(histogram)


def frequency(word, histogram):
    '''Returns the frequency of a word in a text.
       Param: word(str): word being analyzed
              histogram(dict, list of lists or tuples): represents source text
       Returns: int
    '''
    if determine_hist_type(histogram) == "dict_with_str_keys":
        return histogram[word]
    elif determine_hist_type(histogram) == "dict_with_num_keys":
        pass
    elif determine_hist_type(histogram) == "list":
        for i in range(len(histogram)):
            if histogram[i] == word:
                return histogram[i][1]


if __name__ == "__main__":
    # print(histogram(sys.argv[1]))
    # print(unique_words(histogram(sys.argv[1])))
    # print(frequency('newsletter', histogram(sys.argv[1])))
