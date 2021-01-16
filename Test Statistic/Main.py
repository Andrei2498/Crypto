from StatisticTest import StatisticTest
import secrets

if __name__ == '__main__':
    test = StatisticTest()

    # Method to set the number of partitions epsilon will be split into.
    # Default value is 8
    test.set_N(8)

    # Method to choose what option to be used in order to generate the number
    # 1 getrandbits from the random module
    # 0 or other value will use randbits from the secrets module
    # Default value is 0
    test.set_rng(0)
    test.non_overlapping_template_matching(9, 2**20)



