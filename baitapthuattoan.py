import re 
str_name="OK - PON Temp #PON1: 34. PON2: 35. PON3: 35. PON4: 34. PON5: 36. PON6: 34. PON7: 40. PON8: 36. PON9: 36. PON10: 33. PON11: 36. PON12: 37. PON13: 34. PON14: 36. PON15: -. PON16: -."
haddler_regex = re.findall("PON\d+:\s+\d+",str_name) 
print(haddler_regex)