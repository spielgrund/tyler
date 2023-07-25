from PIL import Image, ImageChops, ImageFilter, ImageDraw
size = 2048
im = Image.new("RGB", (size,size),0)
rows = 12
cols = 12
xsize = int(im.size[0]/rows)
ysize = int(im.size[1]/cols)
xsizex = int(xsize)
offset = 0
versatz = True


draw = ImageDraw.Draw(im)


def tyler(offset):
    x = 1
    y = 1
    
    while x <= int(rows+1) and y <= int(cols+1):
        draw.rectangle((int(xsize*x-xsize-offset), int(ysize*y-ysize), int(xsize*x-offset), int(ysize*y)), fill=(255,255,255), outline=(128,128,128), width=(5))
        x += 1
        
        if x == int(rows+2):
            if versatz == True:
                if offset == 0:
                    offset = int(xsize/2)
                elif offset == int(xsize/2):
                    offset = 0

            x = 1
            y += 1

tyler(offset)


im.show()
im.save("tile.png")

