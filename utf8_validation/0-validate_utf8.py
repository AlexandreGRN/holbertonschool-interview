#!/usr/bin/python3
"""
UTF8 Check
"""


def CharacterChecker(byteLen, numberBinary):
    """ Check if a number is an UTF-8 character """
    if len(numberBinary) != byteLen * 8:
        return False
    if byteLen == 1:
        return True

    if byteLen == 2 and \
            (numberBinary[8] == "1" and numberBinary[9] == "0"):
        return True

    if byteLen == 3 and \
            (numberBinary[8] == "1" and numberBinary[9] == "0") and \
            (numberBinary[16] == "1" and numberBinary[17] == "0"):
        return True

    if byteLen == 4 and \
            (numberBinary[8] == "1" and numberBinary[9] == "0") and \
            (numberBinary[16] == "1" and numberBinary[17] == "0") and \
            (numberBinary[24] == "1" and numberBinary[25] == "0"):
        return True

    return False


def getCharacterLenght(binary):
    """
    return lengh of the number in byte,
    return 5 if anything other than 1, 2, 3 or 4 or if invalid number header
    """
    patterns = {
        "0": 1,
        "110": 2,
        "1110": 3,
        "11110": 4,
    }

    for pattern in patterns:
        if binary.startswith(pattern):
            return patterns[pattern]
    return 5


def validUTF8(data):
    """ checks if a number is a valid utf-8 character """
    for num in range(len(data)):
        binary = bin(data[num])[2:]
        while len(binary) % 8 != 0:
            binary = "0" + binary
        if (not CharacterChecker(getCharacterLenght(binary), binary)):
            return False
    return True
