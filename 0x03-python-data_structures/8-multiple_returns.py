#!/usr/bin/python3
# task 8-multiple_returns.py


def multiple_returns(sentence):
    """Returns tuple with string length & its 1st character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
