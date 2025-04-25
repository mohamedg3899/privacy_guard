
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.image import Image

Window.clearcolor = (1, 1, 1, 1)

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20

        self.add_widget(Label(text='حامي الخصوصية', font_size='26sp', bold=True, color=(0, 0, 0, 1), halign='center'))

        buttons = [
            'فحص التطبيقات المشبوهة',
            'مراقبة الأذونات',
            'كشف نشاطات التجسس',
            'تنبيهات الحماية'
        ]

        for btn_text in buttons:
            btn = Button(text=btn_text, size_hint=(1, None), height='60dp',
                         background_color=(0.2, 0.6, 0.86, 1), color=(1, 1, 1, 1), font_size='18sp')
            self.add_widget(btn)

class PrivacyApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    PrivacyApp().run()
