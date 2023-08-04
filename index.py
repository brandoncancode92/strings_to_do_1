"""Create a function that, given a string, returns all
of that string’s contents, but without blanks. If given
the string ' Pl ayTha tF u nkyM usi c ', return 'PlayThatFunkyMusic'."""

def lose_blanks(string):
    return string.replace(" ", "")

# print(lose_blanks(' Pl ayTha tF u nkyM usi c '))

"""Create a python function that given a string, returns the integer
made from the string’s digits. Given "0s1a3y5w7h9a2t4?6!8?0", the
function should return the number 1357924680."""

def get_numbers(string):
    numbers = ""
    for char in string:
        if char.isnumeric():
            numbers += char
    return numbers

# print(get_numbers('0s1a3y5w7h9a2t4?6!8?0'))

"""Create a function that, given a string, returns the string’s acronym
(first letters only, capitalized). Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW".
Given "Live from New York, it's Saturday Night!", return "LFNYISN"."""

def create_acronym(string):
    acronym = ''
    for word in string.split():
        first_letter = word[0].upper()
        acronym += first_letter
    return acronym

# print(create_acronym(" there's no free lunch - gotta pay yer way. "))
# print(create_acronym("Live from New York, it's Saturday Night!"))

"""Dictionaries are sometimes called maps because a key (string) maps to a value.
Given two lists, create an associative array (map) containing keys of the first,
and values of the second. For list_1 = ["abc", 3, "yo"] and list_2 = [42, "wassup", true],
return {"abc": 42, 3: "wassup", "yo": True}."""

def create_associative_array(list_one, list_two):
    associative_array = {}
    for i in range(len(list_one)):
        associative_array[list_one[i]] = list_two[i]
    return associative_array

# print(create_associative_array(["abc", 3, "yo"], [42, "wassup", True]))

"""Dictionaries are also called.
Build invertHash(assocArr) to convert hash keys to values,
and values to keys. Given {"name": "Zaphod", "charm": "high", "morals": "dicey"},
return object {"Zaphod": "name", "high":"charm", "dicey": "morals"}."""

def inverted_hash(asso_list):
    inverted_hash = {}
    for key, value in asso_list.items():
        inverted_hash[value] = key
    return inverted_hash

# print(inverted_hash({"name": "Zaphod", "charm": "high", "morals": "dicey"}))