[app]
title = MyGame
package.name = mygame
package.domain = org.mygame
source.dir = .
source.include_exts = py,png,jpg,jpeg,ogg,mp3,wav,ttf,json,atlas
version = 1.0
requirements = python3==3.10.12,kivy==2.3.0,pyjnius==1.5.0,hostpython3==3.10.12,pygame
orientation = portrait
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.wakelock = True
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
