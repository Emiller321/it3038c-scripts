# LAB 7 Pillow Plugin with Python
Here is how you can run a Python script that I created, which uses a plugin called Pillow. 

First, open up vscode application in which you can download here: https://code.visualstudio.com/download

Once you open up vscode, you wan to make sure you have Pillow plugin installed on your system. Go to your terminal and input this below:

```pip install Pillow
```

Once you do this open up vscode and find an image you want to use and input this code to import the Image (Make sure to have your image in the same folder with your code):

```from PIL import Image, ImageEnhance

# Create new image by import
image = Image.open("Here input the name of the image you want to use")
```
For example my image that was used was 'waterfall.jfif'

Now, if you want to apply a color enhancer to the code input this:

```#Creating an Enhancer
color_enhancer = ImageEnhance.Color(image)

#Applying the Enhancer
enhanced_image = color_enhancer.enhance(5)

enhanced_image.show()
```
If you want to apply sharpness input this below:

```sharpness_enhancer = ImageEnhance.Sharpness(image)

enhanced_image = sharpness_enhancer.enhance(7)
enhanced_image.show()
```

Finally, if you want to transpose the image input this code:

```#Transpose the Image
image_flip = image.transpose(Image.Transpose.TRANSPOSE)

image_flip.show()
```
There is many more features to do with this code. However these were my three different usages of the plgin for Lab 7
