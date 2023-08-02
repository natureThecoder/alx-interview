#!/usr/bin/python3
"""lockboxes challenge"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked
    """
    if len(boxes) == 0:
        return False

    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True

    # Keeping track of the opened boxes
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key >= 0 and key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
