def roman_to_arabic(roman):
    r2a = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
    }
    arabic = 0
    for i in range(len(roman)):
        if roman[i] not in r2a:
            raise ValueError(f"Invalid character '{roman[i]}'")
        if i == len(roman) - 1:
            arabic += r2a[roman[i]]
            break

        if roman[i+1] not in r2a:
            raise ValueError(f"Invalid character '{roman[i+1]}'")

        if r2a[roman[i]] < r2a[roman[i+1]]:
            arabic -= r2a[roman[i]]
        else:
            arabic += r2a[roman[i]]

    return arabic
