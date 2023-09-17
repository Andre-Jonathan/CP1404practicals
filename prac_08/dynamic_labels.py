from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetsApp(App):
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = {"Azure Aqua", "Bob Brown", "Cat Cyan", "Oren Ochre", "Ruby Red"}

    def build(self):
        """Build Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create Label from list and display it in the GUI"""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicWidgetsApp().run()
