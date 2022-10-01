# png2ico
Simple tool that convert multiple .PNG files to one multisize .ICO file.

# How to use
First of all, install Pillow by using this command:

`pip install Pillow`

Next, use this command to convert all your (or only one) .PNG file(s) to one .ICO file:

`python png2ico.py 16.png 32.png ...`

BTW, you don't actually need to have all of this .PNG files _(16.png, 32.png, ...)_. With `-r` flag you can convert only one .PNG file to .ICO file with 7 different sizes (from 16x16 to 255x255):

`python png2ico.py big-png-file.png -r`

Also, you can specify output .ICO filename by using `-o`:

`pyhon png2ico.py ... -o favicon.ico`

If you're on Windows, you can just use `drag&drop.cmd` in the way shown in the gif below

![drag&drop.cmd](https://i.imgur.com/jZsZDPl.gif)
