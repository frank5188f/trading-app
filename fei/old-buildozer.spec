[buildozer]
# Buildozer 配置段落，包含 Buildozer 工具自身的配置

# (str) Log level (0 = error only, 1 = info, 2 = debug)
# 日志级别设置 (0 = 仅错误, 1 = 信息, 2 = 调试)。级别越高，日志输出越详细，调试时建议设置为 2。
log_level = 2

# (int) Display warning on error and stop build? (0 = yes, 1 = no)
# 错误时显示警告并停止构建？ (0 = 是, 1 = 否)。设置为 0 时，遇到错误会显示警告并停止构建，方便排查问题。
warn_on_error = 1

# (int) Cleanup the build and package directories after build? (0 = yes, 1 = no)
# 构建后清理构建和打包目录？ (0 = 是, 1 = 否)。设置为 0 时，构建完成后会自动清理 build 和 bin 目录，保持项目目录整洁。
cleanup_build = 1

# (int) Force cleaning (cleanup + full removal of bin / build)?
# 强制清理 (清理 + 完全移除 bin / build 目录)？设置为 1 时，会强制清理 bin 和 build 目录，即使可能包含重要的构建产物。通常设置为 0 即可。
force_build_cleanup = 0

# (int) Ignore Pylint errors? (0 = no, 1 = yes)
# 忽略 Pylint 错误？ (0 = 否, 1 = 是)。Pylint 是一个 Python 代码静态分析工具。设置为 0 时，Buildozer 会检查 Pylint 错误并在日志中显示。
ignore_pylint_errors = 0

# (list) requirements of the project
# 项目的 Python 依赖库列表。Buildozer 会自动下载并打包这些库到 APK 中。
requirements = kivy, pandas, numpy, akshare, matplotlib

# (str) Python interpreter to use
# Python 解释器路径。
# If set to auto, Buildozer will use the python executable from your PATH.
# 如果设置为 auto，Buildozer 将使用您 PATH 环境变量中找到的 python 可执行文件。
# python.path = auto


# -----------------------------------------------------------------------------
# Application section
# Application 配置段落，包含应用程序的基本信息

[app]

# (str) title of your application
# fxf应用程序的标题，将显示在 Android 设备的应用列表中。
title = 我的交易应用

# (str) package.name domain of your application (needed for android/ios packaging)
# 应用程序的包名域名 (Android/iOS 打包需要)。用于生成 Android 包名 (package name)。
package.name = trading_fxf_app
package.domain = org.test

# (str) source directory containing the main.py file
# 包含 main.py 文件的源代码目录。 "." 表示当前目录，即 buildozer.spec 文件所在的目录。
source.dir = .

# (str) Application versioning (method 1: fixed version)
version = 0.1  #  <--  设置您的App版本号，例如 "0.1" 或 "1.0"
# version.regex = __version__ = '([^\']*)'
# version.filename = %(source.dir)s/%(package.name)s/__init__.py

# (list) Source files to exclude from the final package
# 从最终的包中排除的源文件列表。可以使用通配符模式。
source.exclude_patterns =

# (list) Source files to copy into the package.
# 需要复制到包中的源文件列表。可以使用通配符模式。这里列出了一些常见的文件类型，确保 Python 代码、Kivy 文件、图片、字体文件等都被包含。
source.include_patterns = assets/*,bin/*,data/*,images/*,*.py,*.kv,*.atlas,*.json,*.lua,*.ogg,*.mpg3,*.mp4,*.ttf

# (list) Permissions
# Android 应用程序需要的权限列表。
android.permissions = INTERNET

#
# Android specific
# Android 平台特定配置段落

[android]

# (bool) Indicate if the apk is for debug or release
# 指示 APK 是用于 debug 还是 release 版本。
# default value is debug
# 默认值是 debug 版本。
# android.release = True

# (str) Key alias for the release key
# Release 版本签名密钥的别名。用于 release 版本 APK 的签名。
# android.key.alias = myalias

# (str) Key password for the release key
# Release 版本签名密钥的密码。
# android.key.password = mypassword

# (str) Path to debug key. default to ~/.android/debug.keystore
# Debug 版本签名密钥的路径。默认为 ~/.android/debug.keystore。
# android.key.store = ~/.android/debug.keystore

# (str) Password for the release key store
# Release 版本密钥库的密码。
# android.key.storepass = mystorepass

# (int) Android API target to use
# Android API 目标版本。指定应用程序将要运行的 Android API Level。
android.api = 34

# (int) Minimum API required for the application to run
# 应用程序运行所需的最低 Android API 版本。确保应用程序能在较旧的 Android 版本上运行。
android.minapi = 21

# (int) Android NDK API to use. This is the minimum API that your native
# Android NDK API 版本。这是您的本地代码将要编译的最低 API 版本。通常与 android.minapi 保持一致。
android.ndk_api = 21

# (str) Android SDK directory
# Android SDK 目录。**重要**: 必须修改为您的 Android SDK 实际安装路径。
# IMPORTANT: you must change this to match your environment
android.sdk_path = C:\Users\frank\AppData\Local\Android\Sdk
# !!!  fxf请将 <YOUR_ANDROID_SDK_PATH> 替换为您实际安装的 Android SDK 的路径，例如 /opt/android-sdk 或 C:\Users\frank\AppData\Local\Android\Sdk


# (str) Android NDK directory
# Android NDK 目录。**重要**: 必须修改为您的 Android NDK 实际安装路径。
# IMPORTANT: you must change this to match your environment
android.ndk_path = C:\Program Files\Android\Android Studio\plugins\android-ndk
# !!!  fxf请将 <YOUR_ANDROID_NDK_PATH> 替换为您实际安装的 Android NDK 的路径，例如 /opt/android-ndk 或 C:\Users\<用户名>\AppData\Local\Android\Sdk\ndk\<NDK版本> !!!

# (str) Java JDK directory (if not in your PATH)
# Java JDK 目录 (如果不在您的 PATH 环境变量中)。**重要**: 如果 JDK 没有添加到 PATH 环境变量，则必须修改为您的 JDK 实际安装路径。
# IMPORTANT: you must change this to match your environment if JDK is not in PATH
android.jdk_path = C:\Program Files\Eclipse Adoptium\jdk-11.0.26.4-hotspot
# !!!  fxf请将 <YOUR_JDK_PATH> 替换为您实际安装的 JDK 的路径，例如 /usr/lib/jvm/java-8-openjdk-amd64 或 C:\Program Files\Java\jdk1.8.0_XXX !!!


# (list) Android application requirements apart from python modules
# 除了 Python 模块之外的 Android 应用程序依赖项列表。用于添加额外的 jar 包。
# android.add_jars = []

# (list) Android AAR archives to add
# 需要添加的 Android AAR 归档文件列表。AAR 文件是 Android 库的归档格式。
# android.add_aars = []

# (list) Gradle dependencies to add
# 需要添加的 Gradle 依赖项列表。用于添加 Android Gradle 依赖，例如 AndroidX 库或其他第三方库。
# android.gradle_dependencies = []

# (bool) Enable Google Play Billing library
# 启用 Google Play 支付库。如果您的应用需要应用内支付功能，可以启用。
# android.billing = False

# (str) Android application theme to use
# Android 应用程序使用的主题。可以自定义应用程序的外观风格。
# android.theme = Holo.Light

# (str) Manifest application entries
# Manifest 文件 application 标签下的额外条目。用于在 AndroidManifest.xml 文件中添加自定义的 application 标签属性。
# android.manifest.application.entries =

# (str) Manifest meta-data entries
# Manifest 文件 meta-data 标签下的额外条目。用于在 AndroidManifest.xml 文件中添加自定义的 meta-data 标签。
# android.manifest.meta_data =

# (list) Manifest intent filters
# Manifest 文件 intent-filter 标签列表。用于声明应用程序可以响应的 Intent，例如启动 Activity 的 Intent。
# android.manifest.intent_filters =

# (list) Features used by your application
# 应用程序使用的 Android 功能特性列表。用于在 AndroidManifest.xml 文件中声明应用程序使用的硬件或软件功能。
# android.manifest.uses_features =

# (str) Extra XML to put in the manifest manifest node
# 放置在 manifest 节点中的额外 XML 代码。用于向 AndroidManifest.xml 文件的 manifest 根标签添加自定义 XML 代码。
# android.manifest.full_manifest_xml =

# (str) Extra XML to put in the manifest application node
# 放置在 manifest application 节点中的额外 XML 代码。用于向 AndroidManifest.xml 文件的 application 标签添加自定义 XML 代码。
# android.manifest.full_application_xml =

# (list) Manifest mergable libraries
# Manifest 文件中可合并的库列表。用于指定可以合并到主 Manifest 文件中的库。
# android.manifest.mergable_libraries =

# (list) Java classes to add as activities to the Manifest.
# 添加到 Manifest 文件中作为 Activities 的 Java 类列表。用于添加自定义的 Activity 类。
# android.add_activities =

# (str) 启动 mode to set for the main activity
# 为主 Activity 设置启动模式。用于控制 Activity 的启动行为，例如 standard, singleTop, singleTask, singleInstance。
# android.launch_mode = standard

# (list) Android service to add
# 需要添加的 Android Service 列表。用于添加自定义的 Service 组件。
# android.add_services =

# (list) Android receiver to add
# 需要添加的 Android Receiver 列表。用于添加自定义的 BroadcastReceiver 组件。
# android.add_receivers =

# (bool) Enable AndroidX compatibility (deprecated, use android_use_androidx)
# 启用 AndroidX 兼容性 (已弃用，请使用 android_use_androidx)。AndroidX 是 Android 官方推荐的库，用于替代 Support Library。
# android.enable_androidx = False

# (bool) Use AndroidX
# 使用 AndroidX 库。建议启用，以获得更好的兼容性和最新的 Android 特性。
android.use_androidx = True

# (list) AndroidX libraries to explicitly add (appcompat-v7, e.g.)
# 显式添加的 AndroidX 库列表 (例如 appcompat-v7)。如果需要特定版本的 AndroidX 库，可以在这里指定。
# android.androidx_libs = []

# (bool) Enable build cache
# 启用构建缓存。可以加速 Gradle 构建过程，但首次构建可能较慢。
# android.build_cache = False

# (str)  Keystore to use for package signing
# 用于包签名的 Keystore 文件路径。用于 release 版本 APK 的签名。
# android.keystore = release.keystore

# (str)  Alias name for the key to use when signing
# 签名时使用的密钥别名。
# android.keyalias = release

# (str)  Password for the keystore
# Keystore 文件的密码。
# android.keypass = password

# (str)  Password for the key alias
# 密钥别名的密码。
# android.alias_keypass = password

# (list) Android NDK arch to compile for (if empty, will be armeabi-v7a, arm64-v8a)
# 需要编译的 Android NDK 架构列表 (如果为空，则默认为 armeabi-v7a, arm64-v8a)。指定应用程序支持的 CPU 架构，可以减小 APK 大小，提高性能。
android.arch = arm64-v8a, armeabi-v7a

# (int) CPU cores to use to compile native kivy modules
# 用于编译本地 Kivy 模块的 CPU 核心数。-1 表示使用所有可用的 CPU 核心，可以加速编译过程。
android.native_build_cores = -1

# (list) blacklist of cpu arch to not compile for
# 不编译的 CPU 架构黑名单。用于排除某些不需要支持的 CPU 架构。
# android.cpu_blacklist =

# (list) Whitelist of CPU arch to compile for
# 编译的 CPU 架构白名单。用于只编译特定需要支持的 CPU 架构。
# android.cpu_whitelist =

# (str) Path to the Android bootstrap python application.
# Android 引导 Python 应用程序的路径。指定 Android 启动时运行的 Python 脚本。
# android.entrypoint_script = ./main.py

# (str)  Application icon (will be rescaled automatically)
# 应用程序图标 (会自动缩放)。指定应用程序的图标文件路径，Buildozer 会自动生成不同分辨率的图标。
# android.icon_filename = %(source.dir)s/data/icon.png

# (str)  Application icon name in the source dir
# 应用程序图标在源目录中的名称。
# android.icon_name = icon

# (str)  Application splash screen
# 应用程序启动闪屏。指定应用程序的启动闪屏图片路径。
# android.splash_filename = %(source.dir)s/data/splash.png

# (str)  Application splash screen name in the source dir
# 应用程序启动闪屏在源目录中的名称。
# android.splash_name = splash

# (str)  Application logo to use for branding
# 用于品牌宣传的应用程序 Logo。
# android.logo_filename = %(source.dir)s/data/logo.png

# (bool) If True, then skip trying to install the apk on the device
# 如果为 True，则跳过尝试在设备上安装 APK 的步骤。用于只构建 APK 文件，不自动安装到设备。
# android.no_apk_deploy = False

# (str)  Page displayed after the splashscreen
# 闪屏后显示的页面。通常不需要修改。
# android.entry_points = org.kivy.android.PythonActivity:.MainActivity

# (str)  Order of source folders for python import resolution
# Python 导入解析的源文件夹顺序。用于指定 Python 模块搜索路径。
# android.path_in_apk =

# (list)  List of exclusion filters to use when building the apk.
# 构建 APK 时使用的排除过滤器列表。用于排除某些不需要打包到 APK 中的资源文件。
# android.asset_filters =

# (str)  Extra arguments to pass to javac compiler
# 传递给 javac 编译器的额外参数。用于自定义 Java 代码编译选项。
# android.javac_options =

# (str)  Extra arguments to pass to dx compiler
# 传递给 dx 编译器的额外参数。dx 编译器用于将 Java bytecode 转换为 Android Dalvik bytecode。
# android.dex_options =

# (str)  Extra arguments to pass to gradle command
# 传递给 gradle 命令的额外参数。用于自定义 Gradle 构建选项。
# android.gradle_options =

# (bool)  Indicate whether the screen should stay on
# 指示屏幕是否应保持常亮。如果设置为 True，应用程序运行时屏幕将不会自动熄灭。
# android.wakelock = False

# (str)  Application Android orientation
# 应用程序的 Android 屏幕方向。portrait 表示竖屏，landscape 表示横屏。
orientation = portrait

# (int)  Copy application libs instead of making a zip
# 复制应用程序库而不是制作 zip 包。设置为 1 时，会将应用程序库复制到 APK 中，而不是压缩成 zip 包。
# android.copy_libs = 1

# (str)  Preserve venv after packaging.
# 打包后保留 venv 虚拟环境。设置为 1 时，打包后会保留 Python 虚拟环境，通常不需要启用。
# android.preserver_venv = 0

# (bool)  Patch __future__ imports
# 补丁 __future__ 导入。用于处理 Python 2 和 Python 3 的兼容性问题，通常不需要修改。
# android.patch_future = False

# (bool)  Enable multi apk builds
# 启用多 APK 构建。可以根据不同的 CPU 架构或屏幕密度生成多个 APK 文件，减小单个 APK 大小。
# android.split_apk = False

# (list)  List of Java files to add to the android project
# 添加到 Android 项目的 Java 文件列表。用于添加自定义的 Java 代码。
# android.add_java_files =

# (list)  Pymodules to add with compiled extensions
# 添加带有编译扩展的 Pymodules 列表。Pymodules 是 Python 模块的另一种打包方式。
# android.add_pymodules_files =

# (list)  Python shared libraries to add
# 添加的 Python 共享库列表。用于添加自定义的 Python C 扩展库。
# android.add_libraries_files =

# (list)  List of inclusions using pattern syntax for the python code part.
# 用于 Python 代码部分的包含模式列表。用于更精细地控制哪些 Python 代码被包含到 APK 中。
# android.include_patterns =

# (list)  List of exclusions using pattern syntax for the python code part.
# 用于 Python 代码部分的排除模式列表。用于排除某些不需要打包到 APK 中的 Python 代码。
# android.exclude_patterns =

# (str)  Custom source folders for python code
# Python 代码的自定义源文件夹。用于指定额外的 Python 代码搜索路径。
# android.extra_source_dirs =

# (list)  Third-party Python modules requirements apart from pure Python
#        modules
# 除了纯 Python 模块之外的第三方 Python 模块依赖项列表。用于添加需要本地编译的 Python 模块，例如带有 C 扩展的模块。
# android.add_native_builds =

# (str) Manifest uses-sdk element attribute minSdkVersio
# Manifest 文件 uses-sdk 元素的 minSdkVersion 属性。与 android.minapi 对应，定义应用程序兼容的最低 Android API 版本。
# android.manifest.uses_sdk.minSdkVersion = 21

# (str) Manifest uses-sdk element attribute targetSdkVersion
# Manifest 文件 uses-sdk 元素的 targetSdkVersion 属性。与 android.api 对应，定义应用程序目标 Android API 版本。
# android.manifest.uses_sdk.targetSdkVersion = 34

# (dict) Manifest uses-permission element attributes
# Manifest 文件 uses-permission 元素的属性字典。用于更详细地配置 Android 权限，例如设置权限的 protectionLevel。
# android.manifest.uses_permission = [
#    {'name': 'android.permission.ACCESS_FINE_LOCATION'},
#    {'name': 'android.permission.WRITE_EXTERNAL_STORAGE'},
#    {'name': 'android.permission.READ_PHONE_STATE'}
# ]

# (dict) Manifest uses-feature element attributes
# Manifest 文件 uses-feature 元素的属性字典。用于更详细地配置 Android 功能特性声明。
# android.manifest.uses_feature = [
#    {'name': 'android.hardware.camera', 'required': True},
#    {'name': 'android.hardware.camera.autofocus', 'required': False}
# ]

# (str) The Android NDK toolchain version to use
# 使用的 Android NDK 工具链版本。默认为 auto，Buildozer 会自动选择合适的工具链。
# android.ndk_toolchain = auto

# (str) The Android NDK compiler to use
# 使用的 Android NDK 编译器。默认为 clang，是 Android NDK 推荐的编译器。
# android.ndk_compiler = clang


# -----------------------------------------------------------------------------
# Python section
# Python 配置段落，包含 Python 相关的配置

[python]

# (str) pythonHome of python distribution
# Python 发行版的 pythonHome 目录。如果需要使用特定的 Python 发行版，可以在这里指定路径。
# python.home = /path/to/python

# (str) Site-packages dir of python distribution
# Python 发行版的 site-packages 目录。如果 pythonHome 设置了，可以指定 site-packages 目录。
# python.site-packages = /path/to/site-packages

# (str) Kivy version to use
# 使用的 Kivy 版本。
# Leave empty for current kivy version
# 留空表示使用当前 Kivy 版本。
# Or choose a Kivy version with tags/branch/commit
# 或者选择一个 Kivy 版本，可以使用 tags/branch/commit 指定。
# kivy_version = master
kivy_version = 2.3.1

# (str) Kivy git repo url
# Kivy Git 仓库 URL。如果需要使用特定分支或提交的 Kivy 版本，可以修改此项。
# kivy_git_url = https://github.com/kivy/kivy

# (str) Kivy recipes to compile, comma-separated list
# 需要编译的 Kivy recipes 列表，逗号分隔。Recipes 用于编译 Kivy 的 C 扩展模块。
# kivy_recipes =

# (list) Kivy garden requirements
# Kivy Garden 依赖库列表。如果使用了 Kivy Garden 的模块，需要在这里列出。
# kivy_garden_requirements =

# (list) Cython modules to compile
# 需要编译的 Cython 模块列表。如果项目包含 Cython 代码，可以在这里指定需要编译的模块。
# python.modules =


# -----------------------------------------------------------------------------
# General section
# General 配置段落，包含通用配置

[general]

# (str) Current working dir
# 当前工作目录。
# always use BUILD_DIR
# 始终使用 BUILD_DIR。
always_build_dir = 1

# (str) Build dir
# 构建目录。Buildozer 构建过程中的临时文件和输出文件将放在此目录。
build_dir = ./.buildozer

# (str) Binaries dir
# 二进制文件输出目录。构建生成的 APK 文件将放在此目录下的 bin 子目录中。
bin_dir = ./bin

# -----------------------------------------------------------------------------
# Presplash Section
# 启动前预加载画面配置段落，当前未使用

# not used
# 未使用