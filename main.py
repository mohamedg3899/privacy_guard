
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.popup import Popup

Window.clearcolor = (1, 1, 1, 1)

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20

        self.add_widget(Label(text='حامي الخصوصية', font_size='26sp', bold=True, color=(0, 0, 0, 1), halign='center'))

        btn_scan = Button(text='فحص التطبيقات المثبتة', size_hint=(1, None), height='60dp',
                          background_color=(0.1, 0.5, 0.8, 1), color=(1, 1, 1, 1), font_size='18sp')
        btn_scan.bind(on_press=self.show_installed_apps)
        self.add_widget(btn_scan)

        other_buttons = [
            'مراقبة الأذونات',
            'كشف نشاطات التجسس',
            'تنبيهات الحماية'
        ]

        for btn_text in other_buttons:
            btn = Button(text=btn_text, size_hint=(1, None), height='60dp',
                         background_color=(0.2, 0.6, 0.86, 1), color=(1, 1, 1, 1), font_size='18sp')
            self.add_widget(btn)

    def show_installed_apps(self, instance):
        # هذه القائمة ستكون لاحقاً من نظام التشغيل
        fake_apps = [
            "واتساب", "انستغرام", "كاميرا النظام", "مدير الملفات", "تطبيق مشبوه: SpyEye", "تطبيق مجهول: HiddenLog"
        ]
        content = "\n".join(fake_apps)

        popup = Popup(title='التطبيقات المثبتة',
                      content=Label(text=content, halign='right'),
                      size_hint=(0.9, 0.6))
        popup.open()

class PrivacyApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    PrivacyApp().run()
