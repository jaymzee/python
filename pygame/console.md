## pygame fullscreen display
to have pygame render in the console, define the following environment variables:
```
SDL_VIDEODRIVER=fbcon
SDL_NOMOUSE=1
```
you also need permission to write to the framebuffer (/dev/fb0)
the easiest way to do this under linux is to be a member of the group video

test this with pygame 1.96, not sure if this works with pygame 2.x
