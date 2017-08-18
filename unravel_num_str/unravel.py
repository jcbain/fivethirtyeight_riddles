#!/usr/bin/env python3


def digitCount(digits = [1]):
    '''
    input a list of digits and digitCount will count the number of same digits in the local sequence

    Parameters
    -------
    digits <list> :
        list of digits

    Example
    -------
    digitCount(digits = [1,2,3,3])
    >>> [1,1,1,2,2,3]
    # returns One 1, One 2, Two 3
    '''
    d = digits

    correct = d[-1] + 1
    d.extend([correct,correct])
    ran = list(range(0,len(d)))

    counter = 0
    new_ind = 0
    n = 2
    stop_condition = False
    digits_counts = []

    for i in ran:
        x = new_ind

        counter = 1
        if stop_condition:
            break


        while d[x] == d[x+1]:
            x += 1
            counter += 1
            if x > (len(d) - 2):
                stop_condition = True
                break
        new_ind = x + 1
        digits_counts.append(counter)
        digits_counts.append(d[x])

    del digits_counts[-n:]
    return digits_counts


def digitIterate(start_digit = 1, iterations = 5):
    '''
    iterates through countDigit() a set number of times passing the output of pass i
    into the input of pass i + 1

    Parameters
    -------
    start_digit <int> :
        the digit to start with. will inputed into countDigit() as [start_digit]

    iterations <int> :
        the number of iterations

    '''
    inp = [start_digit]

    for it in list(range(0,iterations)):
        inp = digitCount(inp)
        print(inp)

    return "The final result is \n{}".format(inp)

if __name__ == '__main__':
    print(digitIterate())
