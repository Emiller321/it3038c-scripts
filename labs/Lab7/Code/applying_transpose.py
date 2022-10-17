from PIL import Image

# Create new image by import
image = Image.open('waterfall.jfif')

#Transpose the Image
image_flip = image.transpose(Image.Transpose.TRANSPOSE)

image_flip.show()
image_flip.save('transpose_waterfall.jfif')
