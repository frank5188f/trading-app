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
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*,fonts/*

# (list) List of exclusions using pattern matching
source.exclude_patterns = buildozer.spec,README.md,LICENSE

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy==2.1.0

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

# (str) Android NDK version to use
android.ndk = 23b

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
android.ndk_path = ~/.buildozer/android/platform/android-ndk-r23b

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
android.sdk_path = ~/.buildozer/android/platform/android-sdk

# (list) The Android archs to build for
android.arch = arm64-v8a

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (bool) Skip adb installation
android.skip_update = False

# (str) Bootstrap to use for android builds
p4a.bootstrap = sdl2

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2