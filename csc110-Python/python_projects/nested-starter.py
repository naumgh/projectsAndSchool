'''
Design a function that produces the following pattern:
        1, 2, 3, Stop!
        1, 2, 3, Stop!
        1, 2, 3, Stop!
        1, 2, 3, Stop!
        1, 2, 3, Stop!
'''
def pattern_1():
    for line in range(1, 6):
        print("1, 2, 3, Stop!")

    ...

'''
Design a function that produces the following pattern:
        *
        * *
        * * *
        * * * *
        * * * * *
        * * * * * *
'''
def pattern_2():
    for numbers in range(1,7):
        for astrick in range(numbers):
            print("*", end="")
        print("\t\tline:", line)

    ...

'''
Design a function that produces the following pattern:
        ^^^^v
        ^^^vv
        ^^vvv
        ^vvvv
'''
def pattern_3():
    ...

'''
Design a function that produces the following pattern:
        0, 1, 2, 3, 4,
        1, 2, 3, 4, 5,
        2, 3, 4, 5, 6,
'''
def pattern_4():
    ...

'''
Design a function that produces the following pattern:
        1
        1, 2
        1, 2, 3
        1, 2, 3, 4
'''
def pattern_5():
    ...


def main():
    pattern_1()
    pattern_2()
    pattern_3()
    pattern_4()
    pattern_5()

main()
