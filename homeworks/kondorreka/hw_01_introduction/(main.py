# Írj egy egy multi-line kommentet "This is my first Python program" tartalommal.

"""
This is my first 
Python program
"""

# külön sorokon printelj ki egy példát az összes primitív adattípusból amit tanultunk.
# Írd mindegyik mellé kommentben a típusát is.

'0' # string
string = '0' 
print(string)
print(f'Ellenőrzés: {string} --> {type(string)}')

0 # integer
integer = 0
print(integer)
print(f'Ellenőrzés: {integer} --> {type(integer)}')

0.0 # float
float_num = 0.0
print(float_num)
print(f'Ellenőrzés: {float_num} --> {type(float_num)}')

False # boolean
boolean = False
print(boolean)
print(f'Ellenőrzés: {boolean} --> {type(boolean)}')

# Nem primitív, de fontos
None # None value, semmi
none = None
print(none)
print(f'Ellenőrzés: {none} --> {type(none)}')