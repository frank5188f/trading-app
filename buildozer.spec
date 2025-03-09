[app]

# (str) Title of your application
title = Trading App

# (str) Package name
package.name = tradingapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.tradingapp

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*,fonts/*

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 28

# (int) Minimum API your APK will support.
android.minapi = 21

# (list) The Android archs to build for
android.archs = arm64-v8a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2