def is_prime(n):
    list = []
    if n <= 1:
        return False
    else:
        for number in range(1, n+1):
            if n % number == 0:
                list.append(number)
            else:
                pass
        if len(list) == 2:
            return True
        else:
            # return False
            print(list)
if __name__ == '__main__':
    print(is_prime(-7))






















