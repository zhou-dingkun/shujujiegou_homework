'''选择题
BBABBDD
CDBDD
DCBCB
填空题
4.后两个  5.n-1'''
def ten_to_n(num,n):
    tmp=''
    while(num!=0):
        tmp=str(num%n)+tmp
        num=num//n
    return tmp
if __name__=='__main__':
    nums=int(input("十进制整数："))
    n=int(input("目标进制："))
    if n>=10 or n<2:
        print('非法输入')
    else:
        if nums<0:
            print(f'转换后的{n}进制数是-{ten_to_n(nums,n)}')
        elif nums>0:
            print(f'转换后的{n}进制数是{ten_to_n(nums,n)}')
        else:
            print(f'转换后的{n}进制数是0')