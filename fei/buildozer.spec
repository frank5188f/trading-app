[app]
title = Trading App
package.name = tradingapp
package.domain = org.tradingapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 0.1
requirements = python3,kivy==2.3.1,pandas,numpy,akshare,matplotlib

# Android specific
android.permissions = INTERNET
android.api = 34  # Android 15 API level
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.accept_sdk_license = True
android.arch = arm64-v8a

# iOS specific
ios.kivy_ios_version = 1.4.0
ios.ios_deploy_version = 1.7.0
ios.ios_deploy_method = app_store

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (string) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.1,pandas,numpy,akshare,matplotlib,pillow

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if you want to enable the Kivy inspector
inspector = 0

# (list) List of service to declare
services = 

# (list) The directory containing additional python packages
p4a.local_recipes = 

# (str) Application versioning (method 1)
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# (str) Application versioning (method 2)
# version = 1.2.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.1,pandas,numpy,akshare,matplotlib,pillow

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if you want to enable the Kivy inspector
inspector = 0

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1