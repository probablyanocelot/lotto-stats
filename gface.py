from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
import downloader


class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxLayoutExample, self).__init__(**kwargs)

    def refresh_datasets(self):
        downloader.master()


class MainWidget(Widget):
    pass


class Face1(App):
    pass


Face1().run()
