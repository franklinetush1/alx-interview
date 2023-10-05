#!/usr/bin/python3
"""Define a class Square."""


def canUnlockAll(boxes):
    """
     a method that determines if all the boxes can be opened.
    :return: True or False
    """
    n = len(boxes)
    open_boxes = set([0])
    unopen_boxes = set(boxes[0]).difference(set([0]))
    while len(unopen_boxes) > 0:
        boxIdx = unopen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in open_boxes:
            unopen_boxes = unopen_boxes.union(boxes[boxIdx])
            open_boxes.add(boxIdx)
    return n == len(open_boxes)
