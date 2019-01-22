class Calculator:
    """
    Takes a given value and performs various operations on it: 
    addition, subtraction, multiplication, division; can be 
    cleared back to zero.
    """
    def __init__(self, number=0):
        """Return a new Calculator object"""
        self.number = number
        
    def add(self, AddVal):
        """Adds a value to the number."""
        self.number = AddVal + self.number
        return self
    
    def sub(self, SubVal):
        """Subtracts a value from the number."""
        self.number = self.number - SubVal
        return self
    
    def mul(self, MulVal):
        """Multiplies a value with the number."""
        self.number = MulVal * self.number
        return self
    
    def div(self, DivVal):
        """Divides the number by a value."""
        self.number = self.number / DivVal
        return self
    
    def clr(self, ClrVal):
        """Clears the state and sets the number back to 0."""
        self.number = 0
        return self
    
    def result(self):
        return self.number