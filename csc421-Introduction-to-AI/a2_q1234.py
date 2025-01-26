# CSC421 ASSIGNMENT 2 - QUESTION 1

def evaluate(s):
    #when Z is B or A, then a and b will result in Z
    # for | operator, A|B only results in Z when A and B are Z.
    #when A or B are U, the result of A|B when A or B is Z is U
    # same thing above for O
    #U beats O everytime for | operation
    # For &, O beats U everytime
    #precidence goes something like the following:
    # &: Z, O, U
    # |: U, O, Z
    operator, A, B = s.split(' ')
    print(operator)
    print(A)
    print(B)

    precedence = {
        'operator': operator,
        'A': A,
        'B': B
    }

    if precedence['operator'] == '&':
        if precedence['A'] == 'Z' or precedence['B'] == 'Z':
            return 'Z'
        elif precedence['A']!= 'Z' and precedence['B'] != 'Z':
            if precedence['A'] == 'O' or precedence['B'] == 'O':
                return 'O'
            else:
                return 'U'
            
    if precedence['operator'] == '|':
        if precedence['A'] == 'U' or precedence['B'] == 'U':
            return 'U'
        elif precedence['A'] != 'U' and precedence['B'] != 'U':
            if precedence['A'] == 'O' or precedence['B'] == 'O':
                print("TRUE")
                return 'O'
            else:
                return 'Z'


# examples
e1_1 = "& Z O"
e1_2 = "| O O"
e1_3 = "| Z Z"
e1_4 = "& U U"
e1_5 = "& U Z"

res_e1_1 = evaluate(e1_1)
res_e1_2 = evaluate(e1_2)
res_e1_3 = evaluate(e1_3)
res_e1_4 = evaluate(e1_4)
res_e1_5 = evaluate(e1_5)


print(f'{e1_1} = {res_e1_1}')
print(f'{e1_2} = {res_e1_2}')
print(f'{e1_3} = {res_e1_3}')
print(f'{e1_4} = {res_e1_4}')
print(f'{e1_5} = {res_e1_5}')


# CSC421 ASSIGNMENT 2 - QUESTION 2

d = {'foo': "Z", 'b': "O"}
print(d)
e2_1 = '& Z O'
e2_2 = '& foo O'
e2_3 = '& foo b'

def evaluate_with_bindings(s,d):
    operator, A, B = s.split(' ')
    print(A)
    if A != 'Z' and A != 'U' and A != 'O':
        print(A)
        A1 = d[A]
        s = ' '.join([operator,A1,B])

        if B != 'Z' and B != 'U' and  B != 'O':
            B1 = d[B]
            s = ' '.join([operator,A1,B1])
            ans = evaluate(s)
            return ans
            #if ans == A1:
             #   return A
            #else:
            #    return B
        
        ans = evaluate(s)
        return ans
        #if ans == A1:
         #   return A
    
    return evaluate(s)


res_e2_1 = evaluate_with_bindings(e2_1,d)
res_e2_2 = evaluate_with_bindings(e2_2,d)
res_e2_3 = evaluate_with_bindings(e2_3,d)

print(f'{e2_1} = {res_e2_1}')
print(f'{e2_2} = {res_e2_2}')
print(f'{e2_3} = {res_e2_3}')


# CSC421 ASSIGNMENT 2 - QUESTIONS 3,4

def prefix_eval(input_str, d):
    input_list = input_str.split(' ')
    for x in range(0,len(input_list)):
        if input_list[x] != 'Z' and input_list[x] != 'O' and input_list[x] != 'U':
            if input_list[x] in d:
                input_list[x] = d[input_list[x]]
    print( "Here is the input list", input_list)
    res, tail = recursive_eval(input_list)
    print("the res is ", res)
    return res

def recursive_eval(l):
    head,tail = l[0], l[1:]
    if head == '~':
        val, tail = recursive_eval(tail)
        print(val)
        if val == 'Z':
            return 'O', tail
        elif val == 'O':
            return 'Z', tail
        else:
            return 'U', tail

    if head in ['&',"|"]:
        val1, tail = recursive_eval(tail)
        val2, tail = recursive_eval(tail)
        if head == '&':
            if val1 == 'Z' or val2 == 'Z':
                return 'Z', tail
            elif val1 == 'O' or val2 == 'O':
                return 'O', tail
            else:
                return 'U', tail
        if head == '|':
            if val1 == 'U' or val2 == 'U':
                return 'U', tail
            elif val1 == 'O' or val2 == 'O':
                return 'O', tail
            else:
                return 'Z', tail
    else:
        return head, tail

d = {'a': 'O', 'b': 'Z', 'c': 'U'}
e3_1 = "& a | Z O"
e3_2 = "& O | O b"
e3_3 = "| O & ~ b b"
e3_4 = "& ~ a & O O"
e3_5 = "| O & ~ b c"
e3_6 = "& ~ a & c O"
e3_7 = "& & c c & c c"

print(d)
for e in [e3_1,e3_2,e3_3,e3_4,e3_5,e3_6, e3_7]:
    print("%s \t = %s" % (e, prefix_eval(e,d)))

# EXPECTED OUTPUT
# & Z O = Z
# | O O = Z
#| Z Z = Z
# {'foo': 'Z', 'b': 'O'}
# & Z O = Z
# & foo O = Z
# & foo b = Z
# {'a': 'O', 'b': 'Z', 'c': 'U'}
# & a | Z O        = O
# & O | O b        = O
# | O & ~ b b      = O
# & ~ a & O O      = Z
# | O & ~ b c      = O
# & ~ a & c O      = Z
# & & c c & c c    = U
    




