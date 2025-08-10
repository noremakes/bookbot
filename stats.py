def get_num_words(s):
    word_count = len(s.split())
    return word_count

def string_to_char(s):
    string_lower = s.lower()
    char_counts = {}
    for char in string_lower:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_high_to_low(char_dict):
    result_list = []
    for char, count in char_dict.items():
        if char.isalpha():  # only letters
            result_list.append({"char": char, "num": count})

    # Sort list in place by 'num' from greatest to least
    result_list.sort(key=lambda x: x["num"], reverse=True)

    return result_list