import sys
from PIL import Image, ImageDraw, ImageFilter

def main():
    parameters = get_parameters()
    image = draw_tiles(*parameters)
    normal = normalize(image)
    show_output(image, "tiles.png")
    show_output(normal, "normal.png")

def get_parameters():
    size = int(input("Size: "))
    rows = int(input("Rows: "))
    cols = int(input("Cols: "))
    if input("Versatz y/n? ").lower() == "y":
        versatz = True
    else:
        versatz = False
    return [size, rows, cols, versatz]

def draw_tiles(size=1024, rows=10, cols=10, versatz=True):
    size = size
    image = Image.new("RGB", (size,size),0)
    draw = ImageDraw.Draw(image)
    rows = rows
    cols = cols
    xsize = float(image.size[0]/rows)
    ysize = float(image.size[1]/cols)
    
    x = 1
    y = 1
    offset = 0
    
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

    return image
    ...


def normalize(image):
    img = image
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
    blur = img_copy.filter(ImageFilter.GaussianBlur(radius=3))
    gradient_x = blur.filter(ImageFilter.Kernel((3,3),(1,2,1,0,0,0,-1,-2,-1),1,offset=128))
    gradient_y = blur.filter(ImageFilter.Kernel((3,3),(1,0,-1,2,0,-2,1,0,-1),1,offset=128))
    
    #Ziemlich schlechter B Kanal mit weiss
    blue = img.point(lambda i: i * 10)

    # 1 Px Rand wird wieder abgeschnitten
    gradient_x = gradient_x.crop((half_border,half_border,wbb,hbb))
    gradient_y = gradient_y.crop((half_border,half_border,wbb,hbb))


    # Alles wird zusammengefügt
    normal = Image.merge("RGB",(gradient_x,gradient_y,blue))


    #Shift von -1,1 zu 0,1 in 8 Bit
    normal = normal.point(lambda i: i / 2 + 128)
    # Gammashift
    normal = normal.point(lambda i: ((i / 255)**2.2)*255)
    
    return normal

def show_output(i,str):
    #i.show()
    
    i.save(sys.path[0] + "\\" + str)
    #print(sys.path[0] + "\\" + str)

if __name__ == "__main__":
    main()