def main():
    a = int(input("a:"))
    b = int(input("b:"))
    print(power(a, b))


def power(a, b):
    """
    :param a: int
    :param b: int
    :return: int
    """
    ans = 1
    for i in range(b):
        ans *= a
    return ans


if __name__ == '__main__':
    main()
