"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Started 05/09/2023
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Andre Jonathan'
WINDOW_LENGTH = 200
WINDOW_WIDTH = 100
SQUARED_POWER = 2


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (WINDOW_LENGTH, WINDOW_WIDTH)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) ** SQUARED_POWER
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass


SquareNumberApp().run()
