from kivy.app import App
from kivy.app import Builder

MILES_TO_KM = 1.609344
ERROR_VALUE = 0.0


class MilesConverterApp(App):
    def build(self):
        self.title = "Miles to Kilometer"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, change):
        value = self.get_valid_miles() + change
        self.root.ids.input_label.text = str(value)

    def handle_conversion(self):
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def get_valid_miles(self):

        try:
            value = float(self.root.ids.input_label.text)
        except ValueError:
            value = ERROR_VALUE
        return value


MilesConverterApp().run()
