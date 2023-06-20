def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib

def main():
    n = int(input("Введите количество чисел Фибоначчи: "))
    sequence = fibonacci(n)
    print("Последовательность чисел Фибоначчи:")
    print(sequence)

if __name__ == '__main__':
    main()
