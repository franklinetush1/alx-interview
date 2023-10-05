#!/usr/bin/python3
"""Define a class Square."""


def canUnlockAll(boxes):
    """"Method that determines if all the boxes can be opened"""
    n = len(boxes)
    visited = [False] * n
    stack = [0]

    while stack:
        current_box = stack.pop()
        visited[current_box] = True

        for key in boxes[current_box]:
            if not visited[key]:
                stack.append(key)

    return all(visited)
