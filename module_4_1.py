from true_math import divide as true_dvd_1
from fake_math import divide as fake_dvd

result1 = fake_dvd(69, 3)
result2 = fake_dvd(3, 0)
result3 = true_dvd_1(49, 7)
result4 = true_dvd_1(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
