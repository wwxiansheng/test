def compare_version(version1, version2):
    version1_list = list(map(lambda x: int(x), version1.split(".")))
    version2_list = list(map(lambda x: int(x), version2.split(".")))

    if version1_list == version2_list:
        return 0

    min_length = min(len(version1_list), len(version2_list))
    for i in range(min_length):

        if version1_list[i] > version2_list[i]:
            return 1


        elif version1_list[i] < version2_list[i]:
            return -1
        if i == min_length - 1 and version1_list[0:min_length - 1] == version2_list[0:min_length - 1]:
            if len(version1_list) < len(version2_list):
                return -1
            if len(version1_list) > len(version2_list):
                return 1


if __name__ == '__main__':
    value1 = compare_version("1.2.3", "1.2.03.1")
    value2 = compare_version("1.2.3", "1.2.03")
    value3 = compare_version("1.2.3", "1.2.01")
    value4 = compare_version("1.2.3.1", "1.2.03")
    print(value1)
    print(value2)
    print(value3)
    print(value4)
