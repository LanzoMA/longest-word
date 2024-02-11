from english_words import get_english_words_set


def get_longest_word(word_set: set[str], letters: set[str]) -> str:
    current_longest_word: str = ""

    for word in word_set:
        word_allowed: bool = True

        for letter in word:
            if letter not in letters:
                word_allowed = False
                break

        if word_allowed and len(word) >= len(current_longest_word):
            current_longest_word = word

    return current_longest_word


def get_long_words(word_set: set[str], letters: set[str], minimum_length: int) -> set[str]:
    long_words: set[str] = set()
    current_longest_word: str = ""

    for word in word_set:
        word_allowed: bool = True

        for letter in word:
            if letter not in letters:
                word_allowed = False
                break

        if word_allowed and len(word) >= minimum_length:
            long_words.add(word)

    return long_words


def main() -> None:
    every_word: set[str] = get_english_words_set(['web2'], alpha=True, lower=True) 

    # On the CASIO fx-83GT X calculator, you have these letters that you can input which can store arithmetic values.
    letters_1: set[str] = {'a', 'b', 'c', 'd', 'e', 'f', 'm', 'x', 'y'}

    # On the CASIO fx-991CW calculator, you have access to different leters.
    letters_2: set[str] = {'a', 'b', 'c', 'd', 'e', 'f', 'i', 'x', 'y', 'z'}

    longest_word: str = get_longest_word(every_word, letters_1)
    long_words: set[str] = get_long_words(every_word, letters_2, 6)

    print(f"Longest word: {longest_word}")
    

if __name__ == "__main__":
    main()
