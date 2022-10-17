from PIL import Image, ImageEnhance

# Create new image by import
image = Image.open('waterfall.jfif')

#Creating an Enhancer
color_enhancer = ImageEnhance.Color(image)

#Applying the Enhancer
enhanced_image = color_enhancer.enhance(5)

enhanced_image.show()
enhanced_image.save('color_enhancer.jfif')
