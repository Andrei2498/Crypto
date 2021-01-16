import itertools


def create_new_lists(base_list):
    result_list = []
    for i in range(0, len(base_list)):
        for j in range(i, len(base_list)):
            if base_list[i] + base_list[j] > base_list[-1]:
                aux = [x for x in base_list]
                aux.append(base_list[i] + base_list[j])
                result_list.append(aux)
    return result_list


def find_chain(length):
    base_list = [[1, 2]]
    result_list = []
    size = 1
    while size < length:
        for i in base_list:
            aux = create_new_lists(i)
            for j in aux:
                result_list.append(j)
        base_list = [x for x in result_list]
        size += 1

    result_list.sort()
    return list(result_list for result_list, _ in itertools.groupby(result_list))


def check_if_solution(list_to_look):
    count = 0
    for i in list_to_look:
        if i[-1] == 81:
            count += 1
            print(i)
    if count == 0:
        print(False)
    else:
        print("Number of solutions: " + str(count))


# print(find_chain(7))
check_if_solution(find_chain(8))
