from PIL import Image

# List of image file paths
images = ['assets/Image (10).jfif','assets/Image (11).jfif','assets/Image (12).jfif','assets/Image (13).jfif','assets/Image (14).jfif','assets/Image (15).jfif']

# Open the images and store them in a list
gif_images = [Image.open(image) for image in images]

# Save the images as a GIF
gif_images[0].save(
    "custom.gif", save_all=True, append_images=gif_images[1:], duration=200, loop=0
)
