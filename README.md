# TrichromeLibrary_Remover

A python script can help you remove useless **Trichrome Library** and **Trichrome Library Beta** on Android Q+

## Description

As we know, Google uses Trichrome Library to share the same code in Chrome and Webview on Android Q+ devices to save space on the device. The Play Store will automatically install the corresponding Trichrome Library version when installing and upgrading Chrome and Webview, but will not uninstall the old version.

Unfortunately, Android does a poor job of shared library management. Trichrome Library cannot be displayed in the application list like a normal application (because it is a shared library), nor can use `adb shell pm list libraries` to query installed libraries version on the device.

The good news is we can use `adb shell pm uninstall com.google.android.trichromelibrary*_version_code` to uninstall it completely. For root users, they can find installed Trichrome Library in `/data/system/packages.*` or `/data/app/*/*trichromelibrary*`. For non-root users, I didn't find a good way to query the version of the shared library.

So I wrote this python script, which enumerates the version codes of all stable and beta versions to ensure Trichrome Library can be completely uninstalled.

## Usage

1. Install Python
2. Install ADB environment on your system
3. [Download](TrichromeLibrary_Remover.py?raw=true) `TrichromeLibrary_Remover.py`
4. Open shell window and type `adb devices`, make sure your phone is the only ADB device connecting to the computer.
5. Type `python TrichromeLibrary_Remover.py` and wait patiently.

## Useful Link

- [Android Chrome Release History](https://chromiumdash.appspot.com/releases?platform=Android)
- [Android Chrome Old Version Code](https://source.chromium.org/chromium/chromium/src/+/refs/tags/80.0.3987.162:build/util/android_chrome_version.py) (75~80)
- [Android Chrome New Version Code](https://source.chromium.org/chromium/chromium/src/+/master:build/util/android_chrome_version.py) (Since 81)

## Creadits

- CoolApk@涅普迪努 ([Link](https://www.coolapk.com/feed/25329577?shareKey=MGM5ZjZjMjY3NGI2NjA0NTIxZTQ~))
- CoolApk@EdXposed ([Link](https://www.coolapk.com/feed/25337884?shareKey=ZmRhZmU4NTZkNGNkNjA0NTI3ODI~))
