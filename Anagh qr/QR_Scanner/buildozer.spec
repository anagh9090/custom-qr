[app]
title = QR Scanner
package.name = qrscanner
package.domain = coding-by-anagh.neocities.org
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.0
requirements = python3,kivy,pillow,pyzbar
orientation = portrait
fullscreen = 0
#icon.filename = icon.png

# Permissions (camera/file access for scanning)
android.permissions = CAMERA,READ_EXTERNAL_STORAGE,INTERNET

# Android settings
android.api = 31
android.minapi = 21
android.arch = arm64-v8a,armeabi-v7a

# Build settings
bootstrap = sdl2
log_level = 2
