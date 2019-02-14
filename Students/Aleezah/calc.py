class Calculator:
    '''
    functions that together make a dimple calculator including the following operations:
    addition, subtraction, multiplication, division, and clearing.
    '''
    def __init__(self, number=0):
        '''Create the calculator'''
        self.number = number
        
    def add(self, val_add):
        '''Addition funtion'''
        self.number = val_add + self.number
        return self
    
    def sub(self, val_sub):
        '''Subtraction function'''
        self.number = self.number - val_sub 
        return self 
    
    def mul(self, val_mult):
        '''Multiplication function'''
        self.number = val_mult *  self.number 
        return self 
    
    def div(self, val_div):
        '''Division function'''
        self.number = self.number / val_div
        return self 
    
    def clr(self, val_clear):
        '''Clear the calculator back to zero'''
        self.number = 0
        return self 
    
    def result(self):
        '''Return the result'''
        return self.number

def assertAlmostEqual(a, b):
    """ A function that tests the approximate equality of two floating point numbers. """
    assert round(a-b, 7) == 0, "{} is not equal to {}.".format(a, b)

c1 = Calculator()   # Create an instance of a calculator
c2 = Calculator(50) # Create another calculator, initialized with 50

# Test individual methods, and that the two instances properly
# track their own state.
c1.add(2);           assertAlmostEqual(c1.result(), 2)
c1.mul(4);           assertAlmostEqual(c1.result(), 8)
c2.add(50);          assertAlmostEqual(c2.result(), 100)
c1.div(8);           assertAlmostEqual(c1.result(), 1)
c1.sub(-3.);         assertAlmostEqual(c1.result(), 4)
c2.div(c1.result()); assertAlmostEqual(c2.result(), 25)

print ("All tests passed! You have a working calculator!")