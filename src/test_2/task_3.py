from collections import Counter
from typing import Tuple, Dict, List, Any


def process_file(filename: str) -> Tuple:
    sentences_cnt = 0
    words_dict: Dict[str, int] = {}

    with open(filename) as file:
        for line in file:
            sentences_cnt += line.count(". ") + line.count(".\n")
            for word in line.split():
                word = word.lower()
                while not word[-1].isalpha():
                    if len(word) > 1:
                        word = word[:-1]
                    else:
                        break
                if len(word) == 0:
                    continue
                if word not in words_dict.keys():
                    words_dict[word] = 1
                else:
                    words_dict[word] += 1

    return sentences_cnt, words_dict


def get_statistics(top_words_number: int = 10, filename: str = "text.txt"):
    sentences_cnt, words_dict = process_file(filename)
    with open("statistics.txt", "a") as stat_file:
        stat_file.write(f"Number of words: {len(words_dict)}\n")
        stat_file.write(f"Top {top_words_number} words:\n")
        most_common_words: List[Tuple[Any, int]] = Counter(words_dict).most_common(top_words_number)
        for elm in most_common_words:
            stat_file.write(f"{elm[0]} : {elm[1]}\n")
        stat_file.write(f"Number of sentences: {sentences_cnt}\n")
