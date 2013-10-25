
class RGB:
    """docstring for RGB"""
    def __init__(self, r,g,b):
        self.r = r
        self.g = g
        self.b = b

    def isValid(self):
        print("Validating RGB")
        
        if not (0 <= self.r <=255): raise ValueError("r (red) parameter must be between 0 and 255.")
        if not (0 <= self.g <=255): raise ValueError("g (green) parameter must be between 0 and 255.")
        if not (0 <= self.b <=255): raise ValueError("b (blue) parameter must be between 0 and 255.")

        return True

    def getValue(self):
        return (self.r, self.g, self.b)