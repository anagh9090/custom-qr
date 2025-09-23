from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import qrcode
import base64

class GeneratorLayout(BoxLayout):
    qr_image_path = StringProperty("")

    def generate_qr(self, text):
        encoded_text = base64.b64encode(text.encode()).decode()
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(encoded_text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        self.qr_image_path = "qr.png"
        img.save(self.qr_image_path)

class QRGeneratorApp(App):
    def build(self):
        return GeneratorLayout()

if __name__ == "__main__":
    QRGeneratorApp().run()