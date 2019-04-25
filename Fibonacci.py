#因为今天课很多，而且myeclipse的下载很慢，这次就用了python写的，后续会用Java完成作业
def Fibonacci(n):
    assert isinstance(n,int) , 'type erro, input is not int'
    a, b = 1, 1
    for i in range(n):
        yield b
        a, b = b, a+b

if __name__ == '__main__':
    for i in Fibonacci(200):
        print(i)