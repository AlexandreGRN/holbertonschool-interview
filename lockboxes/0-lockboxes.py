#!/usr/bin/python3
"""
Check if all keys are present
"""


def checkKeys(boxes, keyList):
    if len(keyList) == len(boxes):
        return True

"""
Check if all boxes can be opened
"""


def canUnlockAll(boxes):
    keyList = [0]
    newKeyList = [0]
    check = True
    while check:
        newKeyList = keyList
        check = False
        for key in keyList:
            for key in boxes[key]:
                if key < len(boxes) and key not in keyList:
                    newKeyList.append(key)
                    check = True
        if checkKeys(boxes, newKeyList):
            return True
        keyList = newKeyList
    return False
