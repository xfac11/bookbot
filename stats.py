def get_word_count(text):
    count = 0
    if len(text) == 0:
        raise Exception("text is an empty string")
    list = text.split()
    count = len(list)
    return count