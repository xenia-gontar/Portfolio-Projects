
        
from itertools import *
import math

available_products = [18, 24, 28, 30, 42, 50, 52, 54, 60, 66, 70, 72, 76, 78, 90, 92, 96, 98, 100, 102, 110, 112, 114, 120, 124, 126, 130, 132, 138, 140, 144, 148, 150, 152, 154, 160, 162, 168, 170, 172, 174, 176, 180, 182, 186, 188, 190, 192, 196, 198, 204, 208, 210, 212, 216, 220, 222, 228, 230, 232, 234, 238, 240, 244, 246, 250, 252, 258, 260, 264, 268, 270, 276, 280, 282, 286, 288, 292, 294, 300, 304, 306, 308, 310, 312, 316, 318, 322, 330, 332, 336, 340, 342, 344, 348, 350, 354, 356, 360, 364, 366, 370, 372, 378, 390, 392, 396, 400, 406, 408, 410, 414, 418, 420, 426, 430, 432, 438, 440, 442, 448, 450, 456, 460, 462, 468, 470, 472, 480, 486, 490, 492, 494, 496, 498, 504, 506, 510, 518, 520, 522, 528, 532, 534, 540, 546, 550, 552, 558, 560, 564, 568, 570, 572, 574, 578, 592, 594, 598, 600, 602, 608, 610, 612, 616, 620, 630, 632, 636, 638, 644, 646, 648, 650, 656, 660, 666, 670, 672, 676, 680, 682, 688, 690, 696, 700, 702, 708, 712, 714, 720, 722, 726, 730, 738, 740, 742, 748, 750, 754, 756, 760, 770, 774, 780, 782, 784, 790, 792, 798, 800, 804, 806, 810, 812, 814, 816, 828, 830, 832, 836, 840, 846, 850, 852, 858, 864, 868, 870, 874, 880, 882, 900, 902, 910, 912, 918, 924, 930, 940, 946, 954, 960, 962, 966, 972, 976, 984, 988, 990, 996, 1000, 1008, 1012, 1014, 1020, 1022, 1026, 1032, 1036, 1040, 1044, 1050, 1054, 1056, 1062, 1066, 1072, 1078, 1080, 1092, 1098, 1102, 1104, 1106, 1110, 1116, 1120, 1122, 1128, 1134, 1136, 1140, 1150, 1162, 1168, 1170, 1176, 1180, 1188, 1190, 1200, 1204, 1210, 1216, 1218, 1224, 1230, 1232, 1240, 1242, 1248, 1254, 1258, 1260, 1264, 1272, 1278, 1288, 1292, 1296, 1300, 1302, 1320, 1326, 1330, 1340, 1342, 1350, 1360, 1372, 1378, 1380, 1386, 1392, 1404, 1406, 1410, 1416, 1422, 1426, 1428, 1430, 1440, 1444, 1450, 1452, 1460, 1462, 1470, 1472, 1474, 1476, 1480, 1482, 1488, 1500, 1504, 1512, 1518, 1530, 1540, 1548, 1550, 1554, 1558, 1560, 1562, 1566, 1586, 1590, 1596, 1600, 1606, 1610, 1612, 1620, 1632, 1638, 1650, 1652, 1656, 1666, 1674, 1680, 1682, 1692, 1700, 1702, 1704, 1708, 1710, 1716, 1720, 1722, 1736, 1740, 1742, 1750, 1752, 1760, 1770, 1782, 1794, 1798, 1800, 1802, 1820, 1824, 1836, 1846, 1848, 1850, 1856, 1862, 1870, 1872, 1876, 1880, 1886, 1890, 1892, 1908, 1914, 1922, 1924, 1932, 1938, 1950, 1952, 1960, 1968, 1972, 1974, 1978, 1980, 1984, 2006, 2010, 2016, 2030, 2046, 2052, 2072, 2074, 2080, 2090, 2100, 2106, 2112, 2120, 2124, 2132, 2142, 2146, 2150, 2156, 2160, 2162, 2166, 2170, 2184, 2196, 2200, 2214, 2220, 2226, 2236, 2242, 2244, 2250, 2254, 2256, 2262, 2280, 2296, 2310, 2322, 2332, 2340, 2346, 2350, 2352]
available_sums = [11, 17, 23, 27, 29, 35, 37, 41, 47, 51, 53, 57, 59, 65, 67, 71, 77, 79, 83, 87, 89, 93, 95, 97]

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

multipliers = []

# Разобьем произведения на простые множители

def find_divisors(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(n)
   return primfac
   
for product in available_products:
    divisors = find_divisors(product)
    multipliers.append(divisors)

def find_new_multipliers(list_of_multipliers, number):
    new_multipliers = []
    super_new_multipliers = []
    for i in combinations(list_of_multipliers, number):
        new_multipliers.append(i)
    for set_of_multipliers in new_multipliers:
        product = 1
        for k in set_of_multipliers:
            product = product * k
        super_new_multipliers.append(product)
    return list(set(super_new_multipliers))
    
multi = find_new_multipliers([2,3,4,4], 3)
print(multi)

# Как строится функция нахождения двух множителей:
# Найдем само число 
# Посчитаем количество простых множителей
# Минимальное количество - 2 в одном числе
# Всего максимальное количество множителей - 8
# Поэтому возможны такие ситуации: для 3 множителей - 2 и 1, для 4 множителей - 2 и 2, для 5 множителей - 2 и 3, 
## для 6 множителей - 2 и 4, 3 и 3, для 7 множителей - 2 и 5, 3 и 4, для 8 множителей - 2 и 6, 3 и 5, 4 и 4
dictionary = {}
# ключ - число, значение - список списков спаренных множителей

for list_of_prime_multipliers in multipliers:
    number = math.prod(list_of_prime_multipliers)
    set_of_multi = []
    if len(list_of_prime_multipliers) == 3:
        multipliers_1 = find_new_multipliers(list_of_prime_multipliers, 1)
        multipliers_2 = []
        for multi in multipliers_1:
            pair_of_multipliers = []
            pair_of_multipliers.append(multi)
            pair_of_multipliers.append(number/multi)
            set_of_multi.append(sorted(pair_of_multipliers))
    elif len(list_of_prime_multipliers) == 4:
        multipliers_1 = find_new_multipliers(list_of_prime_multipliers, 2)
        multipliers_2 = []
        for multi in multipliers_1:
            pair_of_multipliers = []
            pair_of_multipliers.append(multi)
            pair_of_multipliers.append(number/multi)
            set_of_multi.append(sorted(pair_of_multipliers))
    elif len(list_of_prime_multipliers) == 5:
        multipliers_1 = find_new_multipliers(list_of_prime_multipliers, 2)
        multipliers_2 = []
        for multi in multipliers_1:
            pair_of_multipliers = []
            pair_of_multipliers.append(multi)
            pair_of_multipliers.append(number/multi)
            set_of_multi.append(sorted(pair_of_multipliers))
            
    elif len(list_of_prime_multipliers) == 6:
        multipliers_1 = find_new_multipliers(list_of_prime_multipliers, 2)
        multipliers_2 = []
        for multi in multipliers_1:
            pair_of_multipliers = []
            pair_of_multipliers.append(multi)
            pair_of_multipliers.append(number/multi)
            set_of_multi.append(sorted(pair_of_multipliers))
        multipliers_1 = find_new_multipliers(list_of_prime_multipliers, 3)
        multipliers_2 = []
        for multi in multipliers_1:
            pair_of_multipliers = []
            pair_of_multipliers.append(multi)
            pair_of_multipliers.append(number/multi)
            set_of_multi.append(sorted(pair_of_multipliers))
    
    elif len(list_of_prime_multipliers) == 7:
        multipliers_1 = find_new_multipliers(list_of_prime_multipliers, 2)
        multipliers_2 = []
        for multi in multipliers_1:
            pair_of_multipliers = []
            pair_of_multipliers.append(multi)
            pair_of_multipliers.append(number/multi)
            set_of_multi.append(sorted(pair_of_multipliers))
        multipliers_1 = find_new_multipliers(list_of_prime_multipliers, 3)
        multipliers_2 = []
        for multi in multipliers_1:
            pair_of_multipliers = []
            pair_of_multipliers.append(multi)
            pair_of_multipliers.append(number/multi)
            set_of_multi.append(sorted(pair_of_multipliers))
            
    elif len(list_of_prime_multipliers) == 8:
        multipliers_1 = find_new_multipliers(list_of_prime_multipliers, 2)
        multipliers_2 = []
        for multi in multipliers_1:
            pair_of_multipliers = []
            pair_of_multipliers.append(multi)
            pair_of_multipliers.append(number/multi)
            set_of_multi.append(sorted(pair_of_multipliers))
        multipliers_1 = find_new_multipliers(list_of_prime_multipliers, 3)
        multipliers_2 = []
        for multi in multipliers_1:
            pair_of_multipliers = []
            pair_of_multipliers.append(multi)
            pair_of_multipliers.append(number/multi)
            set_of_multi.append(sorted(pair_of_multipliers))
            
        multipliers_1 = find_new_multipliers(list_of_prime_multipliers, 4)
        multipliers_2 = []
        for multi in multipliers_1:
            pair_of_multipliers = []
            pair_of_multipliers.append(multi)
            pair_of_multipliers.append(number/multi)
            set_of_multi.append(sorted(pair_of_multipliers))
            
    dictionary[number] = set_of_multi

   

# удалим повторы
for key, value in dictionary.items():
    new_value = []
    for elem in value:
        if elem not in new_value:
            new_value.append(elem)
    dictionary[key] = new_value        


print(dictionary)    
  
# считаем суммы  
new_dictionary = dictionary

for key, value in new_dictionary.items():
    new_value = []
    sum = 0
    for each_value in value:
        for number in each_value:
            sum += number
        if sum < 100: 
                new_value.append(sum)    
    new_dictionary[key] = []        
    new_dictionary[key] = new_value         
print("Новый словарь: \n")
print(new_dictionary)       
    
            
        
        
