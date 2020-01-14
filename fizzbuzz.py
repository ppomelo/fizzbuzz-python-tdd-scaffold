def FizzBuzz(num):

    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'

    if num % 3 == 0:
        return 'Fizz'

    if num % 5 == 0:
        return 'Buzz'
    
    return str(num)

if __name__ == '__main__':
    for i in range(1, 101):
        print(FizzBuzz(i))