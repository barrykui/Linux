import sys
from PIL import Image
import os
import matplotlib.pyplot as plt

img_folder = 'person01_running_d1_uncomp_new'

img_num = 400
images = []
images_name_list = []
for i in range(img_num):
  img_name = os.path.join(img_folder, 'frame_'+str(i)+'.jpg')
  if os.path.exists(img_name):
    images.append(Image.open(img_name))  # im.size = (352, 288)
    images_name_list.append(img_name)

widths, heights = zip(*(i.size for i in images))
print('Number of images to concatenate: {0}'.format(len(images_name_list)))

max_height = 256
total_width = max_height * img_num

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0

# counter = 0
for im in images:
  im = im.resize(size=(max_height, max_height), resample=Image.ANTIALIAS)
  # print(images_name_list[counter], im.size)
  # plt.imshow(im)
  # plt.show()
  new_im.paste(im, box=(x_offset,0))  # im.size = (352, 288)

  x_offset += im.size[0]
  # counter += 1

new_im.save(img_folder+'.jpg')