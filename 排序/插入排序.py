'''
1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素序列中从后向前扫描
3.如果该元素（已排序）大于新元素，将该元素移到下一位置
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5.将新元素插入到该位置后
6.重复步骤2~5


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
