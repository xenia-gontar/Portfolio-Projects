prime_numbers_a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
prime_numbers_b = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

prime_sum_list = []

for a in prime_numbers_a:
    for b in prime_numbers_b:
        if a+b < 100:
            prime_sum_list.append(a+b)

new_list = [x for x in range(4, 100)]
print(set(new_list) - (set(prime_sum_list)))
        
        