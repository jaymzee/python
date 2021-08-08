create audio loopback devices and connect a sender to a receiver
```
modprobe snd-aloop
minimodem -v 0.1 --tx --tx-carrier same --alsa=1,1
sox -q -t alsa hw:1,0,0 -t wav -c 1 - | minimodem --alsa --rx same -c 5 -f -
```
