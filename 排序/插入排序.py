'''
把第一个元素看作有序序列，然后把后面的元素与前面的元素做比较，如果比他大，则继续往后，如果比他小，则交换位置，
然后再与前面的数字比较大，重复该过程，把他们放入合适的位置，使得前面的序列一直为有序的序列。


时间复杂度为 O(n^2),
最好时间复杂度为O(n)
'''




def insert_sort(alist):
    for j in range(1, len(alist) - 1):
        i = j
        while i >= 0:
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                i -= 1
            else:
                break


if __name__ == '__main__':
    li = [56, 226, 93, 54, 77, 31, 44, 55, 20]
    print(li)
    insert_sort(li)
    print(li)
