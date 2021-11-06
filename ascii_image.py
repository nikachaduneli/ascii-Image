import sys
from PIL import Image
from tkinter.filedialog import askopenfilename


# choose image file
image_path =  askopenfilename()
img = Image.open(image_path)

# resize the image
width, height = img.size
aspect_ratio = height/width

# new size of image
new_width = 180
new_height = aspect_ratio * new_width * 0.46
img = img.resize((new_width, int(new_height)))

# convert image to greyscale format
img = img.convert("L")

pixels = img.getdata()

# replace each pixel with a character from array
chars = [',', ':', '!', '/', '*', '%', '$', '&', '#', '@','Ø']

new_pixels = [chars[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)

# split string of chars into multiple strings of length equal to new width and create a list
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)
print(ascii_image)

# write to a text file.
save_path = fl.asksaveasfilename()
with open(save_path+'.txt', 'w') as f:
    f.write(ascii_image)
