from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import downloader
import spin2win


Window.clearcolor = .3, .3, .3, 1


class ScreenManagement(ScreenManager):
    pass


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

    def refresh_datasets(self):
        downloader.master()

    def stats(self):
        spin2win.master('c4l')


class InputScreen(Screen):
    def add_lotto(self):
        filename = self.ids.filename.text
        url = self.ids.url.text
        downloader.add_lotto(url, filename)
        self.manager.current = 'menu'


class MainWidget(Widget):
    pass


class LottoLooker(App):
    def build(self):
        return ScreenManagement()


if __name__ == '__main__':
    LottoLooker().run()
