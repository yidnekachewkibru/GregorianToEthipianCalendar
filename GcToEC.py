def gregorianToEthiopic(_date:str, _format:str) -> str:

    _year, _month, _day = map(int, _date.split("-"))

    s = (_year // 4) - ((_year - 1) // 4) - (_year // 100) + ((_year - 1) // 100) + (_year // 400) - ((_year - 1) // 400)
    t = (14 - _month) // 12
    n = 31 * t * (_month - 1) + (1 - t) * (59 + s + 30 * (_month - 3) + ((3 * _month - 7) // 5)) + _day - 1
    jdn = 1721426 + 365 * (_year - 1) + ((_year - 1) // 4) - ((_year - 1) // 100) + ((_year - 1) // 400) + n
   
    era = 1723856
    r = (jdn - era) % 1461
    n = (r % 365) + 365 * (r // 1460)

    _year = 4 * ((jdn - era) // 1461) + (r // 365) - (r // 1460)
    _month = (n // 30) + 1
    _day = (n % 30) + 1

    _format = _format.replace("Y", str(_year)).replace("M", str(_month)).replace("D", str(_day))
    return _format

print(gregorianToEthiopic("1960-01-01", "Y-M-D"), "E.C")
