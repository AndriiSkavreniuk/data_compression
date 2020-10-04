from PIL import Image
import glob

image_list = []
new_image_list = []
format_jpeg = '.JPEG'

for filename in glob.glob("images/*"):
    print(filename)
    img = Image.open(filename)
    image_list.append(img)

for image in image_list:
    # image.show()
    # some func

    new_image_list.append(image)

for (i, new) in enumerate(new_image_list):
    new.save('{}{}{}'.format("thumbfile/image_", i + 1, format_jpeg), format="JPEG", quality=85, progressive=True)
