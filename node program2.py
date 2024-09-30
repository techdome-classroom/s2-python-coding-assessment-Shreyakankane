def romanToInt(s: str) -> int:
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_map[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

# Example usage:
print(romanToInt("III"))    # 3
print(romanToInt("IV"))     # 4
print(romanToInt("IX"))     # 9
print(romanToInt("LVIII"))   # 58
print(romanToInt("MCMXCIV")) # 1994
