# GregorianToEthipianCalendar

Here is the updated `README.md` content in markdown format:

```markdown
# GregorianToEthipianCalendar

This repository contains a Python function to convert dates from the Gregorian calendar to the Ethiopian calendar.

## Description

The `gregorianToEthiopic` function takes a date in the Gregorian calendar format and converts it to the Ethiopian calendar format. The function is implemented in Python and is designed to be simple and efficient.

## Function: gregorianToEthiopic

### Parameters
- `_date` (str): The date in Gregorian format (YYYY-MM-DD).
- `_format` (str): The desired output format using "Y" for year, "M" for month, and "D" for day.

### Returns
- (str): The date in the Ethiopian calendar format as specified by `_format`.

### Example Usage
```python
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
```

## Usage

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yidnekachewkibru/GregorianToEthipianCalendar.git
    cd GregorianToEthipianCalendar
    ```

2. **Run the Python script:**
    ```sh
    python GcToEC.py
    ```

### Output
The script will output the converted Ethiopian date in the specified format.

Example:
```
print(gregorianToEthiopic("1960-01-01", "Y-M-D"), "E.C")
# Output: 1952-4-23 E.C
```

Feel free to contribute to this project by opening issues or submitting pull requests.
```
