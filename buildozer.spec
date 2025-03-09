[app]
title = Trading App
package.name = tradingapp
package.domain = org.tradingapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 0.1

# Main module
source.include_exts = py,png,jpg,kv,atlas,ttf
source.include_patterns = assets/*,images/*,fonts/*
source.exclude_exts = spec,md
source.exclude_dirs = bin,build,dist
source.exclude_patterns = Thumbs.db

# Entry point
main.filename = main.py

# Requirements
requirements = python3==3.9,kivy==2.1.0,pillow

# Android specific
android.permissions = INTERNET
android.api = 29
android.minapi = 21
android.sdk = 29
android.ndk = 23b
android.accept_sdk_license = True
android.arch = arm64-v8a

# Basic settings
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1