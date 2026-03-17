[app]
title = MyPygameGame
package.name = mypygame
package.domain = org.test
source.dir = game_project
source.include_exts = py,png,jpg,ttf,wav,mp3,json
source.include_patterns = assets/*,images/*

# CRITICAL: Fixes most Pygame Android crashes
requirements = python3==3.10.12,pygame==2.5.2,sdl2_ttf,sdl2_image,sdl2_mixer,android

orientation = landscape
fullscreen = 1

# Android specifics
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.skip_update = False
android.permissions = INTERNET

# CRITICAL: Stops the crash when returning from background
android.manifest.launch_mode = singleInstance

[buildozer]
log_level = 2
warn_on_root = 1
