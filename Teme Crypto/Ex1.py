
def generate_numbers():

    digit_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    number_list = []

    for i in range(0, 9):

        aux = [x for x in digit_list[:len(digit_list) - i]]
        second_aux = []
        number_size = i

        while number_size:
            for j in range(0, len(aux)):
                for k in range(aux[j] % 10, len(digit_list) - number_size + 1):
                    second_aux.append(aux[j] * 10 + digit_list[k])
            aux = [x for x in second_aux]
            second_aux.clear()
            number_size -= 1

        number_list += aux

    print(number_list)
    return number_list


def apply_algorithm(number_list):

    dictionary = {}

    for i in number_list:
        i *= 999
        s = 0

        while i:
            s += i % 10
            i //= 10

        if s in dictionary.keys():
            dictionary[s] += 1
        else:
            dictionary = {s: 1}

    print("Result dictionary: " + str(dictionary))


def main_function():
    result = generate_numbers()
    print("Length of number array: " + str(len(result)))
    apply_algorithm(result)

