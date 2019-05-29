from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.core.window import Window

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import Clock

Key = ['q','w','1','2','3','4','5','6','7','8']

class Piano(GridLayout):

    def __init__(self, **kwargs):
        super(Piano, self).__init__(**kwargs)

        self.cols = 10
        self.make_buttons()

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        self.is_pressed()

    #Make Buttons
    def make_buttons(self):
        self.ulang=["a2","b2","c3","d3","e3","f3","g3","a3","b3","c4"]
        for text in range(len(self.ulang)):
            self.add_widget(Button(text=str(self.ulang[text]), size_hint=(0.1, 0.01)))

    #Check to clicked buttons
    def is_pressed(self):
        for child in self.children:
            child.bind(on_press=self.callback)

    #callback for pressing buttons
    def callback(self, instance):
        kunci = self.ulang.index(instance.text)
        self.Sound(int(kunci))

    #play sounds
    def Sound(self, index):
        sound = SoundLoader.load('audio/%d.wav' %index)
        if sound:
           sound.play()
        return True

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    #callback for change color of Buttons
    def my_callback(self, dt):
        for child in self.children:
            child.background_color = [1, 1, 1, 1]

    #event when we push keyboard keys
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        for index, item in enumerate(Key):
            if keycode[1] == item:
               self.children[-index - 1].background_color = (0, 2, 2, 1)
               self.Sound(index)
               Clock.schedule_once(self.my_callback, 0.2)

class PianoApp(App):
     def build(self):
         return Piano()

if __name__ == '__main__':
    PianoApp().run()