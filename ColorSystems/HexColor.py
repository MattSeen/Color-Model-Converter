import re
import string


class HexColor:
    """docstring for Hex"""
    def __init__(self, word):
        print("Creating Hex Object")
        self.word = word

    def isValid(self):
        re_hex_color = re.compile('(#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?){1}$')
        is_hex_value = re_hex_color.match(self.word)

        return is_hex_value

    def length(self):
        print("providing length of a HexColor")
        return len(self.getValue())

    def getValue(self):
        print("providing value of a HexColor")
        return self.word[1::]