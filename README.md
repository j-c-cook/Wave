# Wave
A 2D solution to the wave equation including transverse and longitudinal views


# Convert to Gif
https://gist.github.com/dergachev/4627207

`ffmpeg -i in.mov -s 640x480 -pix_fmt rgb24 -r 10 -f gif - | gifsicle --optimize=3 --delay=3 > out.gif`


Notes on the arguments:
-r 10 tells ffmpeg to reduce the frame rate from 25 fps to 10
-s 600x400 tells ffmpeg the max-width and max-height
--delay=3 tells gifsicle to delay 30ms between each gif
--optimize=3 requests that gifsicle use the slowest/most file-size optimization
