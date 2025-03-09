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

# (list) Application requirements
# Simplified requirements to ensure basic functionality first
requirements = python3,\
    kivy==2.2.1,\
    pillow,\
    numpy,\
    pandas==1.5.3,\
    matplotlib==3.5.3,\
    akshare

# Android specific
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.ndk_api = 21
android.accept_sdk_license = True
android.arch = arm64-v8a

# Build options
android.gradle_dependencies = "androidx.webkit:webkit:1.4.0"
android.enable_androidx = True
android.add_aars = androidx.webkit:webkit:1.4.0

# Bootstrap and build mode
p4a.branch = develop
p4a.bootstrap = sdl2

# Build settings
android.release_artifact = apk
android.debug = True
android.logcat_filters = *:S python:D
android.copy_libs = 1

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (bool) Skip android.sdk installation
android.skip_sdk_installation = False

# (str) Android NDK version to use
android.ndk_version = 23b

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
android.skip_update = False

# (list) Android application meta-data to set (key=value format)
android.meta_data = python.version=3

# (list) Android library project to add (will be added in the
# project.properties automatically.)
#android.library_references =

# (list) Android shared libraries which will be added to AndroidManifest.xml using <uses-library> tag
#android.uses_library =

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
bin_dir = ./bin