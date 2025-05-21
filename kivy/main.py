import kivy
from kivy.app import App
from kivy.uix.Label import Label
from kivy.uix.Button import Button
from kivy.uix.Widget import Widget
class MyApp (App):
    def build(self):
        wdg = widget()
        lbl = Label(text="Hello word")
        lbl.pos=(200,0)
        btn = Button(text="My Button")
        wdg.add_Widget(lbl)
        wdg.add_Widget(btn)
        return wdg

MyApp().run()