from PIL import Image

img_w=Image.open("circle.png").convert('L')
img_b=Image.open("square.png").convert('L')
width,height=img_w.size

img_new=Image.new('LA',(width,height),0x0)
#print(img_w.getpixel((1,1)))

for j in range(height):
    for i in range(width):
        x=img_w.getpixel((i,j))
        y=img_b.getpixel((i,j))
        g=round((x+y)/2)
        a=round((x-y)/2+128)
        img_new.putpixel((i,j),(g,a))

img_new.save("img.png","PNG")
