"""
Book Title Generator

1. Create three separate databases for book titles.
    a. all words in DB should start with lowed case.
2. Create two separate databases for book authors.
3. Write a def which will join words at random to create a book title.
    a. First part of the title should be upper-cased.
    b. Output - five book titles (three composed of three words, two composed of two words)
    c. Book title should come out within ' "" '
    d. Book author both name and surname must be upper-cased
    e. Book author will start from ' - '
4. Extras: Serialize that output to file/JSON
example:
    "Red chilli peppers" - Bon Jovi
"""
from random import randint


def title_creator():
    opening_db = ["ravens", "mirrors", "ants", "races", "magical items"]
    preposition_db = ["of the", "and", "without", "within", "of"]
    closing_db = ["humans", "glyphs", "island", "peninsula", "mushrooms"]

    first_part = opening_db[randint(0, 4)].capitalize()
    preposition = preposition_db[randint(0, 4)]
    second_part = closing_db[randint(0, 4)]

    book_title = '"' + first_part + " " + preposition + " " + second_part + '"'
    print(book_title)


def author_creator():
    name_db = ["deidre", "eric", "corvin", "oberon", "benedict"]
    surname_db = ["rose", "smith", "trimmer", "white", "rodriguez"]

    name_part = name_db[randint(0, 4)].capitalize()
    surname_db = surname_db[randint(0, 4)].capitalize()

    author = ' - ' + name_part + " " + surname_db
    print(author)


class BookTitleWizardCreator:
    title_creator()
    author_creator()
