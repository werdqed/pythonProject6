from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock


class RootWidget(FloatLayout):

    def calculate_sqrt(self, dt):
        result = float(self.input.text)**0.5
        self.lbl.text = "Result: " + str(result)

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.input = TextInput(text='', size_hint=(.4, .1), pos_hint={'x': .3, 'y': .7})
        self.add_widget(self.input)
        self.lbl = Label(text="Result: ", size_hint=(.4, .1), pos_hint={'x': .3, 'y': .5})
        self.add_widget(self.lbl)
        self.btn = Button(text='Calculate', size_hint=(.4, .1), pos_hint={'x': .3, 'y': .3}, on_press=self.calculate_sqrt)
        self.add_widget(self.btn)
        Clock.schedule_once(self.calculate_sqrt, 3)


class MyApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MyApp().run()