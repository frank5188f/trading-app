from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
    def build(self):
        return Button(text='量化交易应用\n(简化版)')


if __name__ == '__main__':
    TestApp().run() 