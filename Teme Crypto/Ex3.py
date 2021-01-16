from math import gcd

number_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def get_lcm():

    lcm = number_list[0]

    for i in number_list[1:]:
        lcm = lcm * i // gcd(lcm, i)

    return lcm


def check_division(number):

    for i in number_list:
        if number % i != 0:
            return False

    return True


def check_if_solution(number):

    if len(number) < 9:
        return False
    else:
        for i in number:
            if number.count(i) > 1:
                return False

        if (int(number[:3])-int(number[3:6])) % 7 != 0:
            return False

    return check_division(int(number))


def find_answer():

    lcm = get_lcm()
    answer = 0

    for j in range(100, 1500):
        if check_if_solution(str(lcm * j)) is True:
            answer = lcm * j
            print("Index: " + str(j))
            break

    print("Solution value: " + str(answer))
