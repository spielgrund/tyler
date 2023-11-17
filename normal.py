from PIL import Image
from PIL import ImageFilter


img = Image.open("Lenna.png")
img = img.convert("L")
border = 2
half_border = int(border/2)
w, h = img.size
wb = w+border
hb = h+border
wbb = w+half_border
hbb = h+half_border
# 1 px Rand wird hinzugefügt für den Kernel Filter
img_copy = img.resize((wb,hb))
img_copy.paste(img, (border,border))

# Kernel Filter wird Angewendet für den Slope x und Slope y
blur = img_copy.filter(ImageFilter.GaussianBlur(radius=2))
gradient_x = blur.filter(ImageFilter.Kernel((3,3),
                     (1,2,1,0,0,0,-1,-2,-1),1,0))
gradient_y = blur.filter(ImageFilter.Kernel((3,3),
                     (1,0,-1,2,0,-2,1,0,-1),1,0))
#Ziemlich schlechter B Kanal mit weiss
blue = img.point(lambda i: i * 10)

# 1 Px Rand wird wieder abgeschnitten
gradient_x = gradient_x.crop((half_border,half_border,wbb,hbb))
gradient_y = gradient_y.crop((half_border,half_border,wbb,hbb))


# Alles wird zusammengefügt
normal = Image.merge("RGB",(gradient_x,gradient_y,blue))


#Shift von -1,1 zu 0,1 in 8 Bit
normal = normal.point(lambda i: i / 2 + 125)
normal.show()
normal.save("normal.png")
