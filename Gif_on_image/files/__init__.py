my_image = 'files/my_image.jpg'
snow_animation = 'files/animation.gif'

with open(my_image, 'rb') as file:
    my_image_binary = file.read()

with open(snow_animation, 'rb') as file:
    snow_animation_binary = file.read()
