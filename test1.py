from PIL import Image

img_w=Image.open("circle.png")
img_b=Image.open("square.png")
width,height=img_w.size
img_new=Image.new("RGBA",(width,height),0x0)

for y in range(height):
    for x in range(width):
        if img_w.getpixel((x,y)) == (255,255,255) and img_b.getpixel((x,y)) == (255,255,255):
            img_new.putpixel((x,y),(255,255,255,128))
        if img_w.getpixel((x,y)) == (0,0,0) and img_b.getpixel((x,y)) == (255,255,255):
            img_new.putpixel((x,y),(128,128,128,255))
        if img_w.getpixel((x,y)) == (255,255,255) and img_b.getpixel((x,y)) == (0,0,0):
            img_new.putpixel((x,y),(255,255,255,0))
        if img_w.getpixel((x,y)) == (0,0,0) and img_b.getpixel((x,y)) == (0,0,0):
            img_new.putpixel((x,y),(0,0,0,128))

img_new.save("img.png","PNG")
