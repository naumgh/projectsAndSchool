import prolog 

def solve(source, goal_text):
    tokens = prolog.Scanner(source).tokenize()
    rules = prolog.Parser(tokens).parse_rules()
    runtime = prolog.Runtime(rules)
    
    goal = prolog.Parser(prolog.Scanner(goal_text).tokenize()).parse_terms()
    var_args = [a for a in goal.args if isinstance(a,prolog.types.Variable)]
    has_solution = False
    solutions = []
    solutions_vars = [] 
    
    for item in runtime.execute(goal):
        has_solution = True
        solutions.append(item)
        vars = {} 
        for var in var_args:
            vars[var] = str(goal.match(item).get(var))
        solutions_vars.append(vars)
    return (solutions, solutions_vars)


def print_solutions(goal_text, solutions, solutions_vars):
    print("Goal: ", goal_text)
    if len(solutions) == 0:
        print("No solution found") 
    for (s, sv) in zip(solutions, solutions_vars):
        print(s)
        for (k,v) in sv.items():
            print('\t', k, ':',  v) 



source = '''
and_gate(0, 0, 0).
and_gate(0, 1, 0).
and_gate(1, 0, 0).
and_gate(1, 1, 1).

or_gate(0, 0, 0).
or_gate(0, 1, 1).
or_gate(1, 0, 1).
or_gate(1, 1, 1).

not_gate(0, 1).
not_gate(1, 0).


human(socrates). 
mammal(X) :- human(X). 

circuit(A,B,C,Output) :-
    and_gate(A, B, X),
    not_gate(C, Y),
    or_gate(X, Y, Output).

'''

            
# starter goals 
            
goal_text = 'and_gate(0,0,0).'
(solutions, solutions_vars) = solve(source, goal_text) 
print_solutions(goal_text, solutions, solutions_vars)

goal_text = 'and_gate(0,0,1).'
(solutions, solutions_vars) = solve(source, goal_text) 
print_solutions(goal_text, solutions, solutions_vars)

goal_text = 'and_gate(0,0,X).'
(solutions, solutions_vars) = solve(source, goal_text) 
print_solutions(goal_text, solutions, solutions_vars)

goal_text = 'and_gate(0,X,0).'
(solutions, solutions_vars) = solve(source, goal_text) 
print_solutions(goal_text, solutions, solutions_vars)

goal_text = 'mammal(X).'
(solutions, solutions_vars) = solve(source, goal_text) 
print_solutions(goal_text, solutions, solutions_vars)

# Question 6 (single variable) - change goal_text appropriately 

goal_text_q6 = 'or_gate(0,1,X).'
(solutions_q6, solutions_vars_q6) = solve(source, goal_text_q6) 
print_solutions(goal_text_q6, solutions_q6, solutions_vars_q6)

# Question 7 (two variables) 

goal_text_q7a = 'and_gate(0,Y,Z).'
(solutions_q7a, solutions_vars_q7a) = solve(source, goal_text_q7a) 
print_solutions(goal_text_q7a, solutions_q7a, solutions_vars_q7a)

goal_text_q7b = 'and_gate(X,Y,1).'
(solutions_q7b, solutions_vars_q7b) = solve(source, goal_text_q7b) 
print_solutions(goal_text_q7b, solutions_q7b, solutions_vars_q7b)

# Question 8 
# source hopefully corresponds to the boolean expression
#(A AND B) OR (NOT C)
goal_text_q8a = 'circuit(1,1,0,Output).'
(solutions_q8a, solutions_vars_q8a) = solve(source, goal_text_q8a) 
print_solutions(goal_text_q8a, solutions_q8a, solutions_vars_q8a)

goal_text_q8b = 'circuit(X,Y,Z,1).'
(solutions_q8b, solutions_vars_q8b) = solve(source, goal_text_q8b) 
print_solutions(goal_text_q8b, solutions_q8b, solutions_vars_q8b)

# Question 9 write the source_factory facts and rules 
#village or city produces a factory
#factory produces tools, engines, wheels, and advanced_factory
#advanced factory produces trains, airplanes, and cars
#if x produces y, then y needs x
#if x produces y, and y needs z, then z needs x (transitive recursive case)
source_factory = ''' 
produces(factory, tools).
produces(factory, engines).
produces(factory, wheels).
produces(factory, advanced_factory).
produces(village, factory).
produces(city, factory).
produces(advanced_factory, train).
produces(advanced_factory, airplanes).
produces(advanced_factory, cars).

need(Y, X) :- produces(X, Y).
need(X, Z) :- produces(Y, X), need(Y, Z).
'''

goal_text_q9a = 'need(cars, X).'
(solutions_q9a, solutions_vars_q9a) = solve(source_factory, goal_text_q9a) 
print_solutions(goal_text_q9a, solutions_q9a, solutions_vars_q9a)

def tech_needed(product):
    ret  = []
    #need to find what is needed to produce a product
    goal_text = f'need({product},X).'
    (solutions_q9a, solutions_vars_q9a) = solve(source_factory, goal_text)
    #print_solutions(goal_text, solutions_q9a, solutions_vars_q9a)
    #where to find what is needed and return as array of strings
    
    #consists of key value pairs, so find where key = x
    for s in solutions_vars_q9a:
        #print("Here is s ", s)
        for k, v in s.items():
            #print(v)
            if v not in ret:
                ret.append(v)
   # print(needed_tech)
    return ret
    


needed_q9b = tech_needed('factory')
needed_q9c = tech_needed('cars')
print(needed_q9b) 
print(needed_q9c)

# desired output 
# ['village', 'city']
# ['advanced_factory', 'factory', 'village', 'city']    
