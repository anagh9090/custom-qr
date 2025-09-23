from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
import qrcode
from io import BytesIO
from kivy.core.image import Image as CoreImage

Window.clearcolor = (1, 1, 1, 1)  # white background

def encode_data(data):
    return ''.join([chr(ord(c)+3) for c in data])

class QRGenerator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.padding = 20
        self.spacing = 20

        self.input = TextInput(hint_text="Enter text", size_hint=(1, 0.2))
        self.add_widget(self.input)

        self.btn = Button(text="Generate QR", size_hint=(1, 0.2))
        self.btn.bind(on_press=self.generate_qr)
        self.add_widget(self.btn)

        self.qr_image = Image(size_hint=(1, 0.6))
        self.add_widget(self.qr_image)

    def generate_qr(self, instance):
        data = encode_data(self.input.text)
        img = qrcode.make(data)
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        self.qr_image.texture = CoreImage(buffer, ext="png").texture

class GeneratorApp(App):
    def build(self):
        return QRGenerator()

if __name__ == "__main__":
    GeneratorApp().run()
