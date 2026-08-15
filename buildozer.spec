[app]

title = NOVA
package.name = nova
package.domain = org.nova.assistant

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 0.1.0

requirements = python3,kivy==2.3.0,plyer==2.1.0,pyjnius,android

orientation = portrait
fullscreen = 0

android.permissions = RECORD_AUDIO,INTERNET,CAMERA,MODIFY_AUDIO_SETTINGS

android.api = 34
android.minapi = 23
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True
android.wakelock = False

[buildozer]

log_level = 2
warn_on_root = 1
