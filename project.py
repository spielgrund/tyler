from PIL import Image, ImageDraw



size = 1024
image = Image.new("RGB", (size,size),0)
rows = 10
cols = 12
xsize = float(image.size[0]/rows)
ysize = float(image.size[1]/cols)
xsizex = float(xsize)
offset = 0
versatz = True


draw = ImageDraw.Draw(image)


def tyler(offset):
    x = 1
    y = 1
    
    while x <= float(rows+1) and y <= float(cols+1):
        draw.rectangle((float(xsize*x-xsize-offset), float(ysize*y-ysize), float(xsize*x-offset), float(ysize*y)), fill=(255,255,255), outline=(128,128,128), width=(5))
        x += 1
        
        if x == float(rows+2):
            if versatz == True:
                if offset == 0:
                    offset = float(xsize/2)
                elif offset == float(xsize/2):
                    offset = 0

            x = 1
            y += 1

tyler(offset)


image.show()
image.save("tile.png")