#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if not sentence:
        return (0, None)
    else:
        length = len(sentence)
        return length, sentence[:1]
