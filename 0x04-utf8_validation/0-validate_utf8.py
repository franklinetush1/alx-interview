#!/usr/bin/python3
""" UTF-8 Encoding Validation """


def validUTF8(data):
    """
    Determines if a given data set represents a valid
    UTF-8 encoding.
    """
    bytes = 0

    type1 = 1 << 7
    type2 = 1 << 6

    for i in data:

        mask_bytes = 1 << 7

        if bytes == 0:

            while mask_bytes & i:
                bytes += 1
                mask_bytes = mask_bytes >> 1

            if bytes == 0:
                continue

            if bytes == 1 or bytes > 4:
                return False

        else:
            if not (i & type1 and not (i & type2)):
                    return False

        bytes -= 1

    if bytes == 0:
        return True

    return False
