def mult(a, b):
    """
    Returns the product of two numbers
    """
    return a * b

def div(a, b):
    """
    Returns the quotient of two numbers
    """
    try:
        return a / b
    except Exception as e:
        return "Can't divide by zero"

def add(a,b):
	print (a+b)

def sub(a,b):
	print (a-b)
