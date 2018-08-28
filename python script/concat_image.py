# -*- coding: utf-8 -*-
#!/usr/bin/python3
# Concatenating 2 *.PNG to 1 *.PNG 
# PNG1, PNG2 -> PNG1|PNG2

import sys
from PIL import Image
import os
import numpy as np

if not os.path.exists('train'):
    os.makedirs('train')

image_list = os.listdir('trainA')
for image_name in image_list:
    print('Processing '+image_name)
    name_0, name_1, name_2, name_3, name_4 = image_name.split('_')
    image_1_name = os.path.join('trainA', name_0+'_'+name_1+'_'+name_2+'_051_'+name_4)
    image_2_name = os.path.join('trainB', name_0+'_'+name_1+'_'+name_2+'_090_'+name_4)
    save_name =  name_0+'_'+name_1+'_'+name_2+'_051+090_'+name_4

    image_1 = Image.open(image_1_name)
    image_2 = Image.open(image_2_name)

    total_width = image_1.size[0] + image_2.size[0]
    max_height = max(image_1.size[1], image_2.size[1])

    new_im = Image.new('RGB', (total_width, max_height))

    new_im.paste(image_1, (0,0))
    new_im.paste(image_2, (image_1.size[0],0))

    new_im.save(os.path.join('train', save_name))