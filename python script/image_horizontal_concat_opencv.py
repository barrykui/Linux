#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Using OpenCV to concatenate serveral RGB images horizontally

import sys
import os
import cv2
import numpy as np
import argparse

def concatenate(args):
  img_folder = args.input_folder
  img_resize = 256

  img_num = 400
  video_start = 0
  images = []
  images_name_list = []
  for i in range(video_start, img_num):
    img_name = os.path.join(img_folder, 'frame_'+str(i)+'.jpg')
    if os.path.exists(img_name):
      image = cv2.cvtColor(cv2.imread(img_name), cv2.COLOR_BGR2RGB)
      image = cv2.resize(image, dsize=(img_resize, img_resize))
      images.append(image)  # im.size = (352, 288)
      images_name_list.append(img_name)

  (widths, heights) = images[0].shape[0], images[0].shape[1]
  print('Number of images to concatenate: {0}'.format(len(images_name_list)))

  max_height = 256
  total_width = max_height * img_num

  new_im = np.hstack(images[:100])
  print(new_im.max(), new_im.min())
  print('Original image shape:{0}. New image shape: {1}'.format((widths, heights), new_im.shape))

  cv2.imwrite(img_folder+'.jpg', new_im)

if __name__ == "__main__":

    print("Start image concat script ...")

    parser = argparse.ArgumentParser(description="Concatenate image horizontally")
    parser.add_argument('input_folder', metavar='<input_video_file>', default='person01_running_d2_uncomp', help="Input video file")
    # parser.add_argument('output_folder', metavar='<output_folder>', help="Output folder. If exists it will be removed")

    args = parser.parse_args()
    ret = concatenate(args)
    exit(ret)