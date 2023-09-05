from kivy.app import App
from kivy.app import Builder


class MilesConverterApp(App):
    def build(self):
        self.title = "Miles to Kilometer"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, change):
        value = self.get_miles() + change
        self.root.ids.input_label.text = str(value)

    def handle_conversion(self, value):
        value = float(self.root.ids.input_label)
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)

    def get_miles(self):
        value = float(self.root.ids.input_label.text)
        return value
MilesConverterApp().run()
