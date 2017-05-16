def calc(a, i, j):
    if i == j:
        mi = a[i]
        ma = a[i]

    elif j - 1 == i:
        if a[i] > a[j]:
            mi = a[j]
            ma = a[i]

        else:
            mi = a[i]
            ma = a[j]

    else:
        mid = (i + j) // 2
        m1 = calc(a, i, mid)
        m2 = calc(a, mid + 1, j)

        if m1[0] < m2[0]:
            mi = m1[0]
        else:
            mi = m2[0]

        if m1[1] > m2[1]:
            ma = m1[1]
        else:
            ma = m2[1]
    return [mi, ma]


n = int(input("Enter the no. of elements in list"))
alist = []
print("Enter the elements of list")
for i in range(n):
    c = int(input())
    alist.append(c)
print(alist)
print(calc(alist, 0, n - 1))
