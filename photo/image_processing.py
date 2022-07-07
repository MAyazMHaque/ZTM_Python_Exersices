from PIL import Image, ImageFilter

img = Image.open('./pikachu.jpeg')
filtered_img = img.convert('L')
filtered_img.save('grey.png','png')

crooked_img = filtered_img.rotate(190)
crooked_img.save("grey90.png","png")

resized = img.resize((200,200))
resized.save("resized.png","png")

## crop

box = (100 , 100 , 400 , 400)
crop = img.crop(box)
crop.save('cropped.png','png')