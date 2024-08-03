'''
1*1=1
1*2=2 2*2=4
'''

for i in range(9):
    for j in range(i + 1):
        print('%d*%d=%d' % (j + 1, i + 1, (j + 1) * (i + 1)), end=' ')
    print()
