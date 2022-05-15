'''
1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3.针对所有的元素重复以上的步骤，除了最后一个。
4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。


'''
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
