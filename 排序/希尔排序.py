'''
插入排序的另外一种，



'''

def shel_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for j in range(gap, n):
            i = j
            while i > gap:
                if alist[i - gap] > alist[i]:
                    alist[i - gap], alist[i] = alist[i], alist[i - gap]
                i -= gap
        gap = gap // 2
    # for i in range(0, n - 1):
    #     while i > 0:
    #         if alist[i] > alist[i + 1]:
    #             alist[i], alist[i + 1] = alist[i + 1], alist[i]
    #         i -= 1


if __name__ == '__main__':
    li = [17, 226, 93, 54, 77, 31, 44, 55, 20]
    print(li)
    shel_sort(li)
    print(li)
