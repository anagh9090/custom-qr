from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from pyzbar.pyzbar import decode
from PIL import Image
import base64

class ScannerLayout(BoxLayout):

    def scan_qr(self, path):
        try:
            data = decode(Image.open(path))
            if data:
                decoded_text = base64.b64decode(data[0].data).decode()
                self.ids.result_label.text = f"Scanned: {decoded_text}"
            else:
                self.ids.result_label.text = "Invalid QR"
        except Exception as e:
            self.ids.result_label.text = str(e)

class QRScannerApp(App):
    def build(self):
        return ScannerLayout()

if __name__ == "__main__":
    QRScannerApp().run()