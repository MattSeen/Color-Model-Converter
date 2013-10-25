class HSL:
    """docstring for HSL"""
    def __init__(self, h, s, l):
        self.h = h
        self.s = s
        self.l = l
    
    def isValid():
        pass

    def getCssValue(self):
        return "hsl(" + str(int(round(self.h * 360))) + ", " + self.per_str(self.s) + ", " + self.per_str(self.l) + ")"

    def per_str(self, val):
        if val > 1:
            tmp_val = val
        else:
            tmp_val = round(val * 100)

        return str(int(tmp_val)) + "%"
