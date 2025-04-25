
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 25
        self.spacing = 15

        self.add_widget(Label(
            text='حامي الخصوصية',
            font_size='28sp',
            bold=True,
            color=(0, 0, 0, 1),
            halign='center',
            size_hint=(1, None),
            height='60dp'
        ))

        buttons = {
            'فحص التطبيقات المثبتة': self.show_installed_apps,
            'كشف الأذونات الخطيرة': self.show_dangerous_permissions,
            'كشف نشاطات التجسس': self.spy_activity,
            'تنبيهات الحماية': self.show_alerts
        }

        for text, callback in buttons.items():
            btn = Button(
                text=text,
                size_hint=(1, None),
                height='55dp',
                background_color=(0.1, 0.6, 0.8, 1),
                color=(1, 1, 1, 1),
                font_size='17sp'
            )
            btn.bind(on_press=callback)
            self.add_widget(btn)

    def show_installed_apps(self, instance):
        apps = [
            "واتساب", "انستغرام", "كاميرا النظام", 
            "مدير الملفات", "تطبيق مشبوه: SpyEye", 
            "تطبيق مجهول: HiddenLog"
        ]
        self.show_popup("التطبيقات المثبتة", "\n".join(apps))

    def show_dangerous_permissions(self, instance):
        perms = [
            "الوصول إلى الكاميرا", 
            "الوصول إلى الميكروفون", 
            "قراءة سجل المكالمات", 
            "الوصول إلى الموقع الجغرافي"
        ]
        self.show_popup("أذونات خطيرة", "\n".join(perms))

    def spy_activity(self, instance):
        info = "لا توجد نشاطات تجسس حالياً (محاكاة)."
        self.show_popup("نشاطات التجسس", info)

    def show_alerts(self, instance):
        alerts = "جهازك آمن حالياً ولا توجد تهديدات مكتشفة."
        self.show_popup("تنبيهات الحماية", alerts)

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message, halign='right'),
                      size_hint=(0.9, 0.6))
        popup.open()

class PrivacyApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    PrivacyApp().run()
