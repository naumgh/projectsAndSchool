import logic
#need to deal with this little import issue later

#using online resources, conversion from infix to prefix is possible through the use
#of stacks. I am refrencing the following: 

#https://www.calcont.in/Conversion/prefix_to_infix


def convert_to_infix(prefix):
    #2. initialize and use a stack
    stack = []
    operators = ["|","&","~","==>","<==","<=>","^"]
    new_str = ""

    if len(prefix) == 1:
        return prefix

    #1. read prefix expression from right to left
    for i in range(len(prefix)-1,-1,-1):
        #if prefix is an operand, push it onto the stack
        if prefix[i] not in operators and prefix[i] != " ":
            stack.append(prefix[i])
            #print(prefix[i]) 

        elif prefix[i] == '~':
            operand1 = stack.pop()
            new_str = f"({prefix[i]}{operand1})"
            stack.append(new_str)
        #if prefix is an operator, pop everything from stack and concationate
        elif prefix[i] in operators:
            print(stack)
            operand1 = stack.pop()
            print("here is operand1 ", operand1)
            operand2 = stack.pop()
            print("here is operand2 ", operand2)
            new_str = f"({operand1}{prefix[i]}{operand2})"
            stack.append(new_str)
            #print("This is the new string ", new_str)

    print(stack)    
    return(new_str)


prefix_4 = "& & & & A D E ~F ~G"
prefix_3 = "& & & & A | B C D E & ~ F ~ G"
infix_3 = convert_to_infix(prefix_3)
print("This is the new string ", infix_3)
infix_4 = convert_to_infix(prefix_4)
print("This is the new string ", infix_4)


expr_kb = logic.expr(infix_3)
expr_alpha = logic.expr(infix_4)


#do we need to use eliminate_implications
#expr_kb = logic.expr(logic.eliminate_implications(infix_3))
#expr_alpha = logic.expr(logic.eliminate_implications(infix_4))
does_entail = logic.tt_entails(expr_kb,expr_alpha)
print("entailment tf", does_entail)


"""Output from my machine
['(~G)', '(~F)']
here is operand1  (~F)
here is operand2  (~G)
['((~F)&(~G))', 'E', 'D', 'C', 'B']
here is operand1  B
here is operand2  C
['((~F)&(~G))', 'E', 'D', '(B|C)', 'A']
here is operand1  A
here is operand2  (B|C)
['((~F)&(~G))', 'E', 'D', '(A&(B|C))']
here is operand1  (A&(B|C))
here is operand2  D
['((~F)&(~G))', 'E', '((A&(B|C))&D)']
here is operand1  ((A&(B|C))&D)
here is operand2  E
['((~F)&(~G))', '(((A&(B|C))&D)&E)']
here is operand1  (((A&(B|C))&D)&E)
here is operand2  ((~F)&(~G))
['((((A&(B|C))&D)&E)&((~F)&(~G)))']
This is the new string  ((((A&(B|C))&D)&E)&((~F)&(~G)))
['(~G)', '(~F)', 'E', 'D', 'A']
here is operand1  A
here is operand2  D
['(~G)', '(~F)', 'E', '(A&D)']
here is operand1  (A&D)
here is operand2  E
['(~G)', '(~F)', '((A&D)&E)']
here is operand1  ((A&D)&E)
here is operand2  (~F)
['(~G)', '(((A&D)&E)&(~F))']
here is operand1  (((A&D)&E)&(~F))
here is operand2  (~G)
['((((A&D)&E)&(~F))&(~G))']
This is the new string  ((((A&D)&E)&(~F))&(~G))
entailment tf True
"""

prefix_4 = "| | | | A B ~C D E"
prefix_3 = "~ & & & & ~A ~B C ~D ~E"
infix_3 = convert_to_infix(prefix_3)
print("This is the new string ", infix_3)
infix_4 = convert_to_infix(prefix_4)
print("This is the new string ", infix_4)


expr_kb = logic.expr(infix_3)
expr_alpha = logic.expr(infix_4)


#do we need to use eliminate_implications
#expr_kb = logic.expr(logic.eliminate_implications(infix_3))
#expr_alpha = logic.expr(logic.eliminate_implications(infix_4))
does_entail = logic.tt_entails(expr_kb,expr_alpha)
print("entailment tf", does_entail)


#ask prof if need be capitalized for operators
