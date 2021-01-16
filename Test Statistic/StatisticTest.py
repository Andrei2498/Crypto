from scipy.special import gammaincc
from random import getrandbits
import itertools
import math
import secrets



class StatisticTest:
    __N = 8
    __M = 0
    __epsilon = ''
    __B = ''
    __rng = 0

    def set_N(self, value):
        self.__N = value

    def set_rng(self, value):
        self.__rng = value

    def generate_epsilon(self, n):
        bit_string = ''

        if self.__rng not in [1, 2]:
            # token = secrets.token_bytes(int(n/8))
            # bit_string = BitArray(token).bin
            bit_string = bin(secrets.randbits(n))[2:]
        elif self.__rng == 1:
            bit_string = bin(getrandbits(n))[2:]

        self.__epsilon = bit_string

    def check_if_periodic(self, string, m):
        aux = string
        for i in range(0, math.floor(m / 2)):
            aux = aux[1:] + aux[0]
            if string == aux:
                return True

        return False

    def check_if_string_is_contained(self, string_list, string):
        aux = string
        for i in range(0, len(string) - 1):
            aux = aux[1:] + aux[0]
            if aux in string_list:
                return True

        return False

    def generate_template_list(self, m):
        permutation_list = ["".join(seq) for seq in itertools.product("01", repeat=m)]
        template_list = []

        for i in permutation_list:
            if self.check_if_periodic(i, m) is False and self.check_if_string_is_contained(template_list, i) is False:
                template_list.append(i)

        length = len(template_list)
        for i in range(0, length):
            template_list.append(template_list[i][::-1])

        return template_list

    def partition_epsilon(self):
        partition_size = int(len(self.__epsilon)/self.__N)
        self.__M = partition_size
        epsilon_substrings = []
        index = 0

        for i in range(0, self.__N):
            epsilon_substrings.append(self.__epsilon[index: index + partition_size])
            index += partition_size

        return epsilon_substrings

    def search_occurences(self, epsilon_substring, m):
        index = 0
        count = 0

        while index <= len(epsilon_substring) - m:
            if epsilon_substring[index: index + m] == self.__B:
                count += 1
                index += m
            else:
                index += 1
        return count

    def compute_occurence_list(self, epsilon_substrings, m):
        occurence_list = []

        for i in epsilon_substrings:
            occurence_list.append(self.search_occurences(i, m))

        return occurence_list

    def compute_u(self, m):
        return (self.__M - m + 1)/(pow(2, m))

    def compute_sigma(self, m):
        return self.__M * (1/(pow(2, m)) - (2*m - 1)/(pow(2, 2*m)))

    def compute_x_distribution(self, occurence_list, u, sigma):
        result = 0

        for i in occurence_list:
            result += pow((i - u), 2)

        return result/sigma

    def non_overlapping_template_matching(self, m, n):
        self.generate_epsilon(n)
        template_list = self.generate_template_list(m)
        # template_list = ["00000001"]
        epsilon_substrings = self.partition_epsilon()
        u = self.compute_u(m)
        sigma = self.compute_sigma(m)

        count = 0
        min_p = 1

        for i in template_list:
            self.__B = i
            occurence_list = self.compute_occurence_list(epsilon_substrings, m)
            x_distribution = self.compute_x_distribution(occurence_list, u, sigma)
            p_value = gammaincc(self.__N/2, x_distribution/2)

            if p_value < min_p:
                min_p = p_value

            if p_value < 0.01:
                count += 1
            print("Distributie: " + str(x_distribution))
            print("P-Value: " + str(p_value))

        percentage = 100

        if count > 0:
            percentage = round(100 - (count*100)/len(template_list), 2)

        with open("Results.txt", "a") as file:
            file.write(str((count, min_p, len(template_list), percentage)) + " ")
