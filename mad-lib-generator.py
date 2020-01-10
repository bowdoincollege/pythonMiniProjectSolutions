# Mad Libs Generator
# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

story = """The %s %s was running on the %s and found a %s %s and picked it up.
           After smelling the %s, they %s and went %s."""

words = []

print("Let's start a Mad Lib! Give me an adjective: ")
words.append(input())

print("A singular noun: ")
words.append(input())

print("A singular noun: ")
words.append(input())

print("An adjective: ")
words.append(input())

print("A singular noun: ")
words.append(input())

print("A singular noun: ")
words.append(input())

print("A intransitive verb (takes zero objects): ")
words.append(input())

print("A participle (an -ing word): ")
words.append(input())

# String format with lists: https://stackoverflow.com/questions/7568627/using-python-string-formatting-with-lists
print(story % tuple(words))


