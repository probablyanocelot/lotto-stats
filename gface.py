from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import pickle
import downloader


Window.clearcolor = .3, .3, .3, 1


'''
Always update here if change .kv
'''
T0_SCREENS = ['settings', 'input']
T1_SCREENS = ['delete_sheet']


screen_tier = 0


class ScreenManagement(ScreenManager):
    pass


class CustomScreen(Screen):
    def __init__(self, **kwargs):
        super(CustomScreen, self).__init__(**kwargs)
        self.scrren_tier = screen_tier


class BackButton(Button):
    def __init__(self, **kwargs):
        super(BackButton, self).__init__(**kwargs)
    # back = ObjectProperty()

    def on_press(self):
        if App.get_running_app().root.current in tuple(T1_SCREENS):
            App.get_running_app().root.current = App.get_running_app().root.previous()
        else:
            App.get_running_app().root.current = 'home'


class HomeButton(Button):
    def __init__(self, **kwargs):
        super(HomeButton, self).__init__(**kwargs)
        # self.add_widget(Label(text='Back', on_press=self.on_press))

    def on_press(self):
        App.get_running_app().root.current = 'home'


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

    def refresh_datasets(self):
        downloader.master()


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

    #  NEED TO MAKE MODULAR VALIDATION FUNCTION ??
    # def validation(self, instance):
    #     if len(self.instance.text) > 0 & self.instance.text.endswith(tuple(downloader.ext)):   # if text is not empty
    #         continue
    #     else:
    #         print("Error: INVALID ENTRY")


class SettingScreen(Screen):
    pass


"""
    LOOP THROUGH downloader.sheet_dict TO DISplay FIELDs To eDIT
"""


class DeleteSheet(Screen):

    def __init__(self, **kwargs):
        super(DeleteSheet, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.layout = layout
        self.popups = []
        self.create_buttons()
        self.layout.add_widget(BackButton(
            text='Back', font_size='80dp', size_hint_x=.8, pos_hint={"center_x": .5}))
        self.add_widget(layout)

    def create_buttons(self, **kwargs):
        counter = 0
        for sheet in downloader.sheet_dict:

            layout = BoxLayout(orientation='vertical')
            popup_label = Label(text='Delete ' + sheet + ' ? (can restore in settings)',
                                size_hint=(None, None), size=(400, 400), pos_hint={'center_x': .5})

            button_layout = BoxLayout(orientation='horizontal')
            btn1 = Button(text='Cancel')
            btn2 = Button(text='Delete')

            layout.add_widget(popup_label)
            button_layout.add_widget(btn1)
            button_layout.add_widget(btn2)
            layout.add_widget(button_layout)

            popup = Popup(title=sheet, content=layout)
            self.popups.append(popup)

            btn1.bind(on_press=popup.dismiss)

            btn = Button(text=sheet, font_size='80dp',
                         size_hint_x=.8, pos_hint={"center_x": .5},)
            btn.bind(on_press=self.popups[counter].open)
            self.layout.add_widget(btn)

            counter += 1


class SheetEditScreen(Screen):
    def __init__(self, **kwargs):
        super(SheetEditScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.layout = layout


class LottoLooker(App):
    def __init__(self, **kwargs):
        super(LottoLooker, self).__init__(**kwargs)
        self.previous_screen = ""

    def build(self):
        return ScreenManagement()


if __name__ == '__main__':
    LottoLooker().run()
