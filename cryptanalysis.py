from helpfulFunctions import text_clean

import matplotlib.pyplot as plt

def bar_chart(text, LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    text = text_clean(text)
    frequencies = []
    message_length = len(text)

    for char in LETTERS:
      proportion = text.count(char) / message_length
      frequencies.append(proportion)

    plt.bar(list(LETTERS), frequencies)
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Frequency Analysis')

    plt.show()

def chi_squared(text, LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    text = text_clean(text)
    letter_percentage = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.0015, 0.0077, 0.040, 0.024, 0.067, 0.075, 0.019, 0.00095, 0.060, 0.063, 0.091, 0.028, 0.0098, 0.024, 0.0015, 0.020, 0.00074]
    total = 0
    
    for char in LETTERS:
        actual = text.count(char)
        expected = letter_percentage[LETTERS.find(char)] * len(text)
        partial = (expected - actual)**2 / expected
        total += partial

    return total
