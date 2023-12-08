def sum_written_numbers(big_string):

    words = big_string.split(" ")

    number_words = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five" : 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    for word in words:
        if word in number_words:
            total_sum += number_words[word]
