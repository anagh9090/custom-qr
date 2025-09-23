from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from pyzbar.pyzbar import decode
from PIL import Image
from kivy.uix.filechooser import FileChooserIconView

def decode_data(encoded):
    return ''.join([chr(ord(c)-3) for c in encoded])

class QRScanner(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.padding = 20
        self.spacing = 20

        self.label = Label(text="Select a QR image", size_hint=(1, 0.2))
        self.add_widget(self.label)

        self.filechooser = FileChooserIconView(size_hint=(1, 0.6))
        self.add_widget(self.filechooser)

        self.btn = Button(text="Scan QR", size_hint=(1, 0.2))
        self.btn.bind(on_press=self.scan_qr)
        self.add_widget(self.btn)

    def scan_qr(self, instance):
        if not self.filechooser.selection:
            self.label.text = "Please select an image first"
            return

        file_path = self.filechooser.selection[0]
        img = Image.open(file_path)
        decoded_objs = decode(img)
        if not decoded_objs:
            self.label.text = "No QR code found"
            return

        for obj in decoded_objs:
            try:
                data = decode_data(obj.data.decode('utf-8'))
                self.label.text = f"My QR code content: {data}"
            except:
                self.label.text = "This QR code is not from my app"

class ScannerApp(App):
    def build(self):
        return QRScanner()

if __name__ == "__main__":
    ScannerApp().run()
