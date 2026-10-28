#选择题：1.a,5.c,6.b,7.d,9.d,13.c,14.d
#填空：2.集合，线性结构，树结构，图形结构
#7.没有，1
#8.后继结点，1，后继，有任意多个
#9.任意个
def calc(n):
    sum=0
    for i in range(1,n+1):
        sum_n=1
        for j in range(1,i+1):
            sum_n=sum_n*j
        sum+=sum_n
    return sum
n=int(input('输入n:'))
sum=calc(n)
print(f'阶乘求和为{sum}')
#时间复杂度：O（n^2)
#空间复杂度：S（1）