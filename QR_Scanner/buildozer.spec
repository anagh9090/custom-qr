[app]

# (str) Title of your application
title = QR Scanner

# (str) Package name
package.name = qrscanner

# (str) Package domain
package.domain = coding-by-anagh.neocities.org

# (str) Source code where main.py is located
source.dir = .

# (str) Main entry point
source.main = scanner_app.py

# (list) Application requirements
requirements = python3,kivy,pillow,pyzbar

# (str) Icon of your app (optional)
#icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the app should be fullscreen
fullscreen = 0

# (str) Android permissions
android.permissions = CAMERA,INTERNET

# (str) Version
version = 1.0

# (bool) Presplash
#presplash.filename = %(source.dir)s/presplash.png

# (str) Package format
android.arch = armeabi-v7a
