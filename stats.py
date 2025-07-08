def get_num_words(text: str) -> int:
    return len(text.split())

def get_char_freq(text: str) -> dict[str, int]:
    freq_dict = {}
    for word in text.split():
        for char in word.lower():
            if char not in freq_dict.keys():
                freq_dict[char] = 1
            else:
                freq_dict[char] += 1
    return freq_dict

def get_sorted_list(chars: dict[str, int]) -> list[dict]:
    sorted_list = []
    for k, v in chars.items():
        temp_dict = {"char": k, "num": v}
        sorted_list.append(temp_dict)
    
    sorted_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_list

