# max_number_to_check = 100


def is_prime(number):
    for x in range(2, number):
        if (number % x) == 0:
            return False

    return True


def prime_list(max_num):
    prime_lists = []
    for nums in range(2, max_num):
        if is_prime(nums):
            prime_lists.append(nums)

    return prime_lists


n = int(input("Find prime up to: "))
for i in prime_list(n):
    print(i)


