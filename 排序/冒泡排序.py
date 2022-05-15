def button_sort(alist):
    n = len(alist)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


if __name__ == '__main__':
    li = [17, 226, 93, 54, 77, 31, 44, 55, 20]
    print(li)
    button_sort(li)
    print(li)
