number_list = [1, 2, 3, 4, 5, 6]
target_value = 10


def two_sum(numbers, target):
    pairs = []
    number_dict = {}
    for index, value in enumerate(numbers):
        number_dict[value] = index

    for number in numbers:
        if target - number in number_dict:
            if (number, target - number) not in pairs and (target - number, number) not in pairs:
                pairs.append((number, target - number))

    return pairs


print(two_sum(number_list, target_value))
