import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
import os

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.image = Image(source='F1-Logo.png')
        self.add_widget(self.image)

        self.label = TextInput(text="RaceRadar",font_size=190)
        self.add_widget(self.label)

        self.start_button = Button(text="Start")
        self.start_button.bind(on_press=self.on_start_click)
        self.add_widget(self.start_button)

        self.quit_button = Button(text="Quit")
        self.quit_button.bind(on_press=self.on_quit_click)
        self.add_widget(self.quit_button)

    def on_start_click(self, instance):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = dir_path+"\\subMain.py"
        os.system("python "+dir_path)

    def on_quit_click(self, instance):
        App.get_running_app().stop()

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
