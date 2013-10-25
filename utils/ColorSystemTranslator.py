from .ColorSystems.RGB import RGB
# from .ColorSystems.HexColor import HexColor
from .ColorSystems.HSL import HSL
from .ColorSystems.HSLA import HSLA

# import re
# import string

class ColorSystemTranslator:
    """docstring for colour_system_translator"""
    def __init__(self, hex_value):
        print("Creating ColorSystemTranslator object")
        self.hex_value = hex_value
        print(self.hex_value.getValue())

    def toRGB(self):
        print("Preparing to convert to RGB")
        
        if self.hex_value.length() == 6:
            r,g,b = tuple(int(self.hex_value.getValue()[i:i+2], 16) for i in range(0, 6, 2))
        else:
            r,g,b = tuple(int(self.hex_value.getValue()[i:i+1], 16)*17 for i in range(0, 3))

        rgb = RGB(r,g,b)
        print("Fully converted to RGB")
        return rgb

    def toHSL(self):
        """ This code is based on a snippet from the following website: http://sebsauvage.net/python/snyppets/#hsl"""
        
        print("Preparing to convert to HSL")
        
        rgb = self.toRGB()
        r,g,b = rgb.getValue()

        if rgb.isValid():
            var_R = r/255.0
            var_G = g/255.0
            var_B = b/255.0

            var_Min = min( var_R, var_G, var_B )    # Min. value of RGB
            var_Max = max( var_R, var_G, var_B )    # Max. value of RGB
            del_Max = var_Max - var_Min             # Delta RGB value

            l = ( var_Max + var_Min ) / 2.0
            h = 0.0
            s = 0.0
            if del_Max!=0.0:
                if l<0.5: s = del_Max / ( var_Max + var_Min )
                else:     s = del_Max / ( 2.0 - var_Max - var_Min )
                del_R = ( ( ( var_Max - var_R ) / 6.0 ) + ( del_Max / 2.0 ) ) / del_Max
                del_G = ( ( ( var_Max - var_G ) / 6.0 ) + ( del_Max / 2.0 ) ) / del_Max
                del_B = ( ( ( var_Max - var_B ) / 6.0 ) + ( del_Max / 2.0 ) ) / del_Max
                if    var_R == var_Max : h = del_B - del_G
                elif  var_G == var_Max : h = ( 1.0 / 3.0 ) + del_R - del_B
                elif  var_B == var_Max : h = ( 2.0 / 3.0 ) + del_G - del_R
                while h < 0.0: h += 1.0
                while h > 1.0: h -= 1.0
        else:
            raise ValueError("No idea, how we got here...")

        hsl = HSL(h,s,l)

        print("Fully converted to HSL")
        return hsl

    def toHSLA(self):

        hsl = self.toHSL()

        if hsl.isValid():
            hsla = HSLA(hsl.getValue())
            return hsla
        else:
            raise ValueError("No idea, how we got here...")

