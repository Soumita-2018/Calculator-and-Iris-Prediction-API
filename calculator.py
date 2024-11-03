def calculate(operation, x, y):
    ''' 
    Operation is a variable which takes add, sub, mul, div and a and y are two numbers
    '''
    if operation == 'addition':
        return x+y
    elif operation == 'subtraction':
        if x>y:
            return x-y
        else:
            return y-x
    elif operation == 'multiplication':
        return x*y
    elif operation == 'division':
        return x//y
    
    
    