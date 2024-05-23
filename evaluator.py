import re

def evaluate_expression(expression, variables, values):
    var_dict = {variables[i]: values[i] for i in range(len(variables))} #range(len(values))
    for var in variables:
        if var in var_dict:
            expression = expression.replace(var, str(var_dict[var]))

    expression = expression.replace('+', ' or ')
    expression = expression.replace('*', ' and ')
    
    #yummy
    expression = re.sub(r'[01]*0[01]*', '0', expression, 10)
    expression = re.sub(r'1{2,}', '1', expression, 10)

    try:
        result = eval(expression) 
    except:
        result = -1
    return result

def variable_detector(input_string):
    variables = []
    for i in input_string:
        if ((i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z')) and i not in variables:
            variables.append(i)
    return variables
