from PIL import Image, ImageEnhance

# Create new image by import
image = Image.open('waterfall.jfif')

sharpness_enhancer = ImageEnhance.Sharpness(image)

enhanced_image = sharpness_enhancer.enhance(7)
enhanced_image.show()
enhanced_image.save('sharpness_waterfall.jfif')