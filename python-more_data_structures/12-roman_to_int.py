#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    rom_val = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    totaal = 0
    vorige_waarde = 0

    for char in reversed(roman_string):
        waarde = rom_val[char]
        if waarde >= vorige_waarde:
            totaal += waarde
        else:
            totaal -= waarde
        vorige_waarde = waarde
    return totaal
