#reference : https://www.codespeedy.com/merge-two-images-in-python/
from PIL import Image
# Open images and store them in a list
images = [Image.open(x) for x in ['B1_x.jpg', 'B1_x-02.jpeg']]
save_file_name = "test2.pdf" #can be PDF or JPG.
img_quality = 30
def merge_horizontal(images):
    total_height =0 
    max_width = 0
# find the width and height of the final image 
#merge horizontal 
    for img in images:
        total_height += img.size[1]
        max_width = max(max_width,img.size[0])
# create a new image with the appropriate height and width
        new_img = Image.new('RGB', (max_width, total_height))
# Write the contents of the new image
        current_height = 0
        for img in images:
            new_img.paste(img, (0,current_height))
            current_height += img.size[1]
    return new_img
# Save the image
def merge_vertical(images):
    total_width = 0
    max_height = 0
# find the width and height of the final image 
#merge vertical
    for img in images:
        total_width += img.size[0]
        max_height = max(max_height, img.size[1])
# create a new image with the appropriate height and width
        new_img = Image.new('RGB', (total_width, max_height))
# Write the contents of the new image
        current_width = 0
        for img in images:
            new_img.paste(img, (current_width,0))
            current_width += img.size[0]
    return new_img
# Save the image
#new_image_return = merge_horizontal(images)
new_image_return = merge_vertical(images)
new_image_return.save(save_file_name,optimize=True,quality=img_quality)
