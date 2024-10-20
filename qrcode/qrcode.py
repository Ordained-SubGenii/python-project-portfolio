#!/usr/bin/python3
import segno
from urllib.request import urlopen

mygithub_url = "https://github.com/Ordained-SubGenii"    
qrcode = segno.make(f"{mygithub_url}\n Thank you Reading Rainbow for teaching me how to hack into the unicorn dominion.")
# url referrer to binary number display of cat walking (a gif file)
img_url = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzdmcTB3bHl3dWN6MXc4N3ZidHh4bXVxOHJoc2R5bGFyczdxcXFiaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wwg1suUiTbCY8H8vIA/giphy.gif"
bg_image = urlopen(img_url)
qrcode.to_artistic(background=bg_image,target='binarycat_qrcode.gif',dark='black',light='green',border=0,scale=4)

    
