import image

img = image.Image("cy.png")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        newred = 255 - p.getRed()
        newgreen = 255 - p.getGreen()
        newblue = 255 - p.getBlue()

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()

##There are a number of different image processing algorithms that follow the same pattern as shown above. Namely, take the original pixel, extract the red, green, and blue intensities, and then create a new pixel from them. The new pixel is inserted into an empty image at the same location as the original.
##
##For example, you can create a gray scale pixel by averaging the red, green and blue intensities and then using that value for all intensities.
##
##From the gray scale you can create black white by setting a threshold and selecting to either insert a white pixel for a black pixel into the empty image.
##
##You can also do some complex arithmetic and create interesting effects, such as Sepia Tone
