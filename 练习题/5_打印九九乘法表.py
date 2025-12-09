
if __name__ == '__main__':
    for i in range(1,10):
        for j in range(1,i+1):
            print(f'{j}*{i}={i*j}',end='\t')
        print('\n')


# --- 总结----
# 1、print() 函数默认参数 end='\n'。可自定义