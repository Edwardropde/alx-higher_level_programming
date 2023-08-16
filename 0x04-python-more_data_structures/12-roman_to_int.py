#!/usr/bin/python3
def to_deduct(num_list):
    thesub = 0
    max_list = max(num_list)
    for m in num_list:
        if max_list > m:
            thesub += m
    return (max_list - thesub)

def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    rom_str = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    keylist = list(rom_str.keys())
    mun = 0
    romlast = 0
    numlist = [0]
    for ch in roman_string:
        for x in keylist:
            if x == ch:
                if rom_str.get(ch) <= romlast:
                    mun += to_deduct(numlist)
                    numlist = [rom_str.get(ch)]
                else:
                    numlist.append(rom_str.get(ch))
                    romlast = rom_str.get(ch)
    mun += to_deduct(numlist)
    return (mun)
