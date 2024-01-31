# Part 1

prime_numbers_a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
prime_numbers_b = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

prime_sum_list = []

for a in prime_numbers_a:
    for b in prime_numbers_b:
        if a+b < 100:
            prime_sum_list.append(a+b)

new_list = [x for x in range(4, 100)]
print(set(new_list) - (set(prime_sum_list)))

# Part 2

available_sums = [11, 17, 23, 27, 29, 35, 37, 41, 47, 51, 53, 57, 59, 65, 67, 71, 77, 79, 83, 87, 89, 93, 95, 97]



prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

available_products = {}

for available_sum in available_sums:
    available_products[available_sum] = []

for a in range(2,98):
    for b in range(2,98):
            if (a in prime_numbers) & (b in prime_numbers):
                pass    
            else:
                sum = a + b
                if sum in available_sums and (a*b) not in available_products[sum]: 
                    available_products[sum].append(a*b)

print(available_products)

# удалить повторы:

all_values = []

for value in available_products.values():
    for each_value in value:
        all_values.append(each_value)


# посчитаем повторящиеся значения: 

doubled_numbers = list(dict((x, all_values.count(x)) for x in set(all_values) if all_values.count(x) > 1).keys())


for key, value in available_products.items():
    print(f"Текущий ключ - {key}")
    print(f"Текущее значение - {value}")
    list_of_num = value
    new_list = []
    for num in list_of_num:
        if num not in doubled_numbers:
            new_list.append(num)
    available_products[key] = new_list

print(available_products)  


        
