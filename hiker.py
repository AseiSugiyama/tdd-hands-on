def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return n


def main():
    for i in range(1, 101):
        print(fizzbuzz(i))


if __name__ == "__main__":
    main()
