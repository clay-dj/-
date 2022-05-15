'''
循环的每次选择出一个最大的数，放在数组最后

时间复杂度：O(n ^ 2)
是否为稳定：稳定
'''


def button_sort(list):
    n = len(list)

    for j in range(0, n - 1):
        for i in range(0, n - 1 - j):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]


if __name__ == '__main__':
    li = [17, 226, 93, 54, 77, 31, 44, 55, 20]
    print(li)
    button_sort(li)
    print(li)
