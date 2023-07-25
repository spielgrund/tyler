from PIL import Image, ImageChops, ImageFilter, ImageDraw
size = 512
im = Image.new("RGB", (size,size),0)
rows = 4
cols = 4
xsize = int(im.size[0])/rows
ysize = int(im.size[1])/cols
xsizex = int(xsize)
offset = 0
versatz = False


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
                    offset = xsize/2
                elif offset == int(xsize/2):
                    offset = 0

            x = 1
            y += 1

tyler(offset)


im.show()
im.save("tile.png")

