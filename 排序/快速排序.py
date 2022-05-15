'''
1.从数列中挑出一个元素，称为”基准”（pivot），
2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
  在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
3.递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

时间复杂度为O(nlog(n))
最坏时间复杂度为O(n^2)
不稳定
'''


def quick_sort(the_list, start, end):
    if start < end:
        m = start
        n = end
        point_key = the_list[m]

        while m < n:
            while m < n and the_list[n] >= point_key:
                n -= 1
            the_list[m] = the_list[n]
            while m < n and the_list[m] <= point_key:
                m += 1
            the_list[n] = the_list[m]
        the_list[m] = point_key
        quick_sort(the_list, start, m - 1)
        quick_sort(the_list, n + 1, end)

    return the_list


if __name__ == '__main__':
    the_list = [10, 1, 18, 30, 23, 12, 7, 5, 18, 17]
    start = 0
    end = len(the_list) - 1
    print(the_list)
    print(quick_sort(the_list, start, end))
