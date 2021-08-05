## pygame fullscreen display
to have pygame render in the console, define the following environment variables:
```
SDL_VIDEODRIVER=fbcon
SDL_NOMOUSE=1
```
you also need permission to write to the framebuffer (/dev/fb0)
the easiest way to do this under linux is to be a member of the group video

tested with pygame 1.96, not sure how to get this to work with pygame 2.x

pygame 1.9.6 dependencies
```
sudo apt-get install git python3-dev python3-numpy
libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev
libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev libfreetype6-dev
```
