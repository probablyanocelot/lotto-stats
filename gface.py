from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import pickle
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


class BackButton(Widget):
    pass


class InputScreen(Screen):

    def add_lotto(self):
        if self.ids.filename.text.endswith(tuple(downloader.ext)):
            filename = self.ids.filename.text
        else:
            print('ERROR: WRONG EXTENSION')
            self.manager.current = 'input'
            return
        if len(self.ids.url.text) > 0:
            url = self.ids.url.text
        else:
            print('ERROR: CANNOT BE EMPTY; MUST BE URL')
            self.manager.current = 'input'
            return
        downloader.add_lotto(url, filename)
        if filename.split('.')[0] not in downloader.sheet_dict:
            downloader.sheet_dict[filename.split('.')[0]] = {
                'url': url, 'filename': filename}
        else:
            downloader.sheet_dict[filename].update(
                {'url': url, 'filename': filename})
        pickle.dump(downloader.sheet_dict, open('sheet_pickle.p', 'wb'))
        self.manager.current = 'menu'


class SettingScreen(Screen):
    pass

    #  NEED TO MAKE MODULAR VALIDATION FUNCTION
    # def validation(self, instance):
    #     if len(self.instance.text) > 0 & self.instance.text.endswith(tuple(downloader.ext)):   # if text is not empty
    #         continue
    #     else:
    #         print("Error: INVALID ENTRY")


class MainWidget(Widget):
    pass


class LottoLooker(App):
    def build(self):
        return ScreenManagement()


if __name__ == '__main__':
    LottoLooker().run()
