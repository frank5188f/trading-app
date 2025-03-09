[app]
title = Trading App
package.name = tradingapp
package.domain = org.tradingapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 0.1

# Icon and Presplash
icon.filename = %(source.dir)s/data/icon.png
presplash.filename = %(source.dir)s/data/presplash.png

# Minimal requirements for initial build success
requirements = python3,kivy

# Android specific
android.permissions = INTERNET
android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 21
android.accept_sdk_license = True
android.arch = arm64-v8a

# Bootstrap and build mode
p4a.branch = master
p4a.bootstrap = sdl2

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1