from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # Label judul
        self.label = Label(text="Silakan Login", font_size='20sp')
        self.add_widget(self.label)

        # Input email
        self.email_input = TextInput(hint_text='Email', multiline=False)
        self.add_widget(self.email_input)

        # Input password
        self.password_input = TextInput(hint_text='Password', multiline=False, password=True)
        self.add_widget(self.password_input)

        # Tombol login
        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.on_login_click)
        self.add_widget(self.login_button)

        # Label hasil
        self.result_label = Label(text="")
        self.add_widget(self.result_label)

    def on_login_click(self, instance):
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()
        if email and password:
            self.result_label.text = "Login berhasil!"
        else:
            self.result_label.text = "Email dan password tidak boleh kosong."

class LoginApp(App):
    def build(self):
        return LoginLayout()

if __name__ == '__main__':
    LoginApp().run()
