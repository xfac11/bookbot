def get_word_count(text):
    count = 0
    if len(text) == 0:
        raise Exception("text is an empty string")
    list = text.split()
    count = len(list)
    return count

def get_each_character_count(text):
    lowered_string = text.lower()
    character_count = {}
    for character in lowered_string:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def sort_on(items):
    return items["num"]

def create_sorted_list(characters_count):
    sorted_list = []
    for key in characters_count:
        sorted_list.append({"char": key, "num": characters_count[key]})
    
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

