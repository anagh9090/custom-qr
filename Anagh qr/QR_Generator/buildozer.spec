[app]
title = QR Generator
package.name = qrgenerator
package.domain = coding-by-anagh.neocities.org
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.0
requirements = python3,kivy,pillow,qrcode
orientation = portrait
fullscreen = 0
#icon.filename = icon.png

# Permissions (none needed for generator app)
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

# Android settings
android.api = 31
android.minapi = 21
android.arch = arm64-v8a,armeabi-v7a

# Build settings
# sdl2 bootstrap is recommended for mobile GUI
bootstrap = sdl2
log_level = 2
