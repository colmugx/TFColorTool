import re


def verify(color):
    if (len(color) != 6 or not re.match(r'[a-fA-F0-9]', color)):
        raise Exception("Illegal color")
    return True


def listAdd(list1, list2):
    return [list2[i] + list1[i] for i in range(len(list1))]


def listDec(list1, list2):
    return [list2[i] - list1[i] for i in range(len(list1))]
