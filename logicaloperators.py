"""
Logical Operators
AND (and)
A   B   Result
F   F   F
F   T   F
T   F   F
T   T   T

OR (or)
A   B   Result
F   F   F
T   F   T
F   T   T
T   T   T
"""

p = 65
c = 23
print(p > 35 or c > 35)
print(not (p > 35))
