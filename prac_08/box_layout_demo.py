from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build Kivy GUI"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Display greeting with name"""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_button(self):
        """Clear the names and replace output from hello name back to the original opening"""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = "Enter your name"


BoxLayoutDemo().run()
