def isComplete(assignment):
    return None not in (assignment.values())

def select_unassigned_variable(variables, assignment):
    for var in variables:
        if assignment[var] is None:
            return var

def is_consistent(assignment, constraints):
    for constraint_violated in constraints:
        if constraint_violated(assignment):
          return False
    return True

def init_assignment(csp):
    assignment = {}
    for var in csp["VARIABLES"]:
        assignment[var] = None
    return assignment

def add_constraint(csp, constraint): 
    csp['CONSTRAINTS'].append(constraint)
    
def recursive_backtracking(assignment, csp):
    if isComplete(assignment):
        return assignment
    var = select_unassigned_variable(csp["VARIABLES"], assignment)
    for value in csp["DOMAINS"]:
        assignment[var] = value
        if is_consistent(assignment, csp["CONSTRAINTS"]):
            result = recursive_backtracking(assignment, csp)
            if result != "FAILURE":
                return result
        assignment[var] = None
    return "FAILURE"


def binary_constraint(var_pair, violations):
    (v1,v2) = var_pair
    return lambda asmt: (asmt[v1], asmt[v2]) in violations
  
# add your code for CSP-based type inference as described in the notebook 
# below. The answer to the problem provided should be named result and 
# be a dictionary with a complete assignment of the variables to types 
# as returned by the CSP backtracking method. 

# Q9 ANSWER GOES HERE (modifications to CSP code and definition)  print
#csp is variables, domains, and constraints.

def unary_constraint(var, violations):
    return lambda asmt: asmt[var] in violations

def ternary_constraint(var_3pair, violations):
    (v1, v2, v3) = var_3pair
    return lambda asmt: (asmt[v1], asmt[v2],asmt[v3]) in violations
    


csp2 = {"VARIABLES": ["I", "F", "X", "Y", "Z", "W"],
        "DOMAINS": ["int", "float"],
        "CONSTRAINTS": []}

violations = {("int","float"),("float", "int"),("float","float")}

#setting variables I and F to int and float
add_constraint(csp2, unary_constraint('I', ['float']))
add_constraint(csp2, unary_constraint('F', ['int']))


#setting assignment constraints for X = I
for (v1,v2) in [("X","I")]: 
    add_constraint(csp2, binary_constraint((v1,v2), violations))

ternary_violations = violations = {("int","int","float"),("int","float","int"),("int","float","float"),("float","int","int")}
#setting additive (tertiary) constraints   viviolations
for (v1, v2, v3) in [("Y", "X", "F"), ("Z", "X", "Y"), ("W", "X", "I")]:
    add_constraint(csp2, ternary_constraint((v1, v2, v3), ternary_violations))

result = recursive_backtracking(init_assignment(csp2), csp2)
print('Result', result)
# Result {'I': 'int', 'F': 'float', 'X': 'int', 'Y': 'float', 'Z': 'float', 'W': 'int'}
    
    