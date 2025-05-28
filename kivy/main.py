from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        lbl = Label(text="Hello World")
        btn = Button(text="My Button")
        
        layout.add_widget(lbl)
        layout.add_widget(btn)
        
        return layout

if __name__ == '__main__':
    MyApp().run()
