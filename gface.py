from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import pickle
import downloader
import spin2win


Window.clearcolor = .3, .3, .3, 1


# ATTEMPT AT PUTTING BACK BUTTON ON SHEETEDITSCREEN
class Box(BoxLayout):
    def __init__(self, **kwargs):
        super(Box, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10


class ScreenManagement(ScreenManager):
    pass


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

    def refresh_datasets(self):
        downloader.master()

    def stats(self):
        spin2win.master('c4l')


# class BackButton(Widget):
#     pass


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


# class SheetButtons(Widget):
#     layout = SheetEditScreen.ids.sheet_edit_layout
#     self.create_buttons()


class SheetEditScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)
        self.create_buttons()

    def create_buttons(self):
        for sheet in downloader.sheet_dict:
            btn = (Button(text=sheet, font_size='80dp', size_hint_x=.8,))
            self.layout.add_widget(btn)


# ATTEMPT AT PUTTING BACK BUTTON ON SHEETEDITSCREEN
class BackButton2(Button):
    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)
        self.text = 'Back'
        self.font_size = '80dp'
        self.size_hint = (.8, 1)
        # self.bind(on_press=self.back)

    # btn = (Button(text=lotto))
    # box.add_widget(btn)
    # self.boxes.add_widget(box)
    # Button(text=lotto, size_hint=(.2, .1))

    # btn = [lambda x: self.add_widget(
    #     Button(text=str(lotto.split('.')[0]))) for lotto in downloader.sheet_dict]

    # on_kv_post:
    #     [self.add_widget(Label(text=str(lotto.split('.')[0])))
    #      for lotto in downloader.sheet_dict]

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
