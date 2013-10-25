import sublime
import sublime_plugin
import re
import string
from  .ColorSystems.HexColor import HexColor
from .utils.ColorModelDetector import ColorModelDetector
from .utils.ColorSystemTranslator import ColorSystemTranslator

_DEBUGPRINT = True

def debugPrint(msg):
    if _DEBUGPRINT:
        print(msg)

class color_model_converterCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.edit = edit
 
        debugPrint('Starting replacement Routine')
        for region in self.view.sel():
            self.region = region
            self.word_reg = self.view.word(region)
            if not self.word_reg.empty(): self.convert_to_hsl()

    def convert_to_hsl(self):
        debugPrint('Starting conversion for word') 

        hex_word = HexColor(self.get_selected_word())

        if hex_word.isValid():
            debugPrint('word found to be a hexidecimal value')

            translator = ColorSystemTranslator(hex_word)
            hsl = translator.toHSL()

            hslCss = hsl.getCssValue()

            tmp_reg = sublime.Region(self.word_reg.begin() - 1, self.word_reg.end())

            self.view.replace(self.edit, tmp_reg, hslCss)
            
            return True
        else:
            print("The Hex value provide was not valid")

    

    def get_selected_word(self):
        full_region = sublime.Region(self.word_reg.begin() - 1, self.word_reg.end())
        word = self.view.substr(full_region)

        return word

