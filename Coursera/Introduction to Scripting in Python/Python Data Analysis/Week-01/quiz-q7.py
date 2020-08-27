def count_letters(word_list):
    letter_count = {}
    for word in word_list:
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    max_frequent = 0
    for letter in letter_count:
        if letter_count[letter]>max_frequent:
            max_frequent = letter_count[letter]
            max_frequent_letter = letter
    return max_frequent_letter, max_frequent

monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"

monty_words = monty_quote.split(" ")
print(count_letters(["hello", "world"]))
print(count_letters(monty_words))
