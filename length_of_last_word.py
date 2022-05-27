#https://ru.hexlet.io/challenges/python_lists_length_of_last_word_exercise/instance
import re


def length_of_last_word(line):
    words = re.split(r'\s+?', line.strip())
    return len(words[-1])

length_of_last_word('''
Return True if string starts with the prefix, otherwise return False. prefix can also be a tuple of prefixes to look for. With optional start, test string beginning at that position. With optional end, stop comparing string at that position.
''')
