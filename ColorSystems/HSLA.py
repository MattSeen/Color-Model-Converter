from .HSL import HSL

class HSLA(HSL):
	"""docstring for HSLA"""
	def __init__(self, h, s, l, a):
		super(HSLA, self).__init__(h, s, l)

	def getCssValue():
        return "hsl(" + str(int(round(self.h * 360))) + ", " + self.per_str(self.s) + ", " + self.per_str(self.l) + ", 1)"