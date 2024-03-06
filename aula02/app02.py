def main():
    n = int(input())
    while n > 46 or n < 0:
        n = entrada()
    initial = [0,1]
    initial = fibonacci(initial,n, 0)
    imprime(initial,n)

def entrada():
    return input()

def fibonacci(initial,n,index):
    if(n != 2):
        initial.append(initial[index] + initial[index + 1])
        fibonacci(initial,n-1,index+1)
    return initial


def imprime(initial,n):
    for num in initial:
        if(initial.index(num) == n-1):
            print(f'{num}')
        else:
            print(f'{num}',end=" ")

main()