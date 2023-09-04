from kivy.app import App
from kivy.app import Builder
from kivy.core.window import Window


class MilesConverterApp(App):
    def build(self):
        self.title = "Miles to Kilometer"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, value):
        try:
            result = float(value) * 1.60934
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass




MilesConverterApp().run()
