'''

1.在未排序序列中找到最小元素，存放到排序序列的起始位置，
2.再从剩余未排序元素中继续寻找最小元素，然后放到已排序序列的末尾。
3.重复第二步，直到所有元素均排序完毕。


时间复杂度为O(n^2)
不稳定排序：希尔、选择、快排、堆
'''


def select_sort(alist):
    n = len(alist)
    for j in range(0, n):
        min_index = j
        for i in range(j + 1, n):
            if alist[i] < alist[min_index]:
                min_index = i
        alist[min_index], alist[j] = alist[j], alist[min_index]


if __name__ == '__main__':
    li = [17, 226, 93, 54, 77, 31, 44, 55, 20]
    print(li)
    select_sort(li)
    print(li)
