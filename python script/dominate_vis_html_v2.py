# -*- coding:utf-8 -*-
#/usr/bin/python3
'''
This python script use `dominate` package to generate static html file

Put `dominate_vis.py` together with 
.
├── dominate_vis.py
├── index.html
├── Camera_RGB_BACK
├── Camera_RGB_FRONT
├── Camera_RGB_LEFT
├── Camera_RGB_RIGHT
├── Camera_Semantic
└── Camera_Semantic_vis

run `python dominate_vis.py` to generate `index.html`, open `index.html` with browser
'''

import dominate
from dominate.tags import *
import os


web_path = '.'

# with dominate.document('Data Visualization') as web:
#     for mod in ['Camera_RGB_FRONT', 'Camera_RGB_RIGHT', 'Camera_RGB_BACK', 'Camera_RGB_LEFT', 'Camera_Semantic_10', 'Camera_Semantic_vis_10']:
#         h2('{0}'.format(mod))
#         with table(border=1, style='table-layout: fixed;'):
#             with tr():
#                 num_img = len(os.listdir('{0}'.format(mod)))
#                 print('Number of images in folder {0}: {1}'.format(mod, num_img))
#                 for i in range(num_img):
#                     path = '{0}/{1:0>6}.png'.format(mod, str(i))
#                     with td(style='word-warp: break-world;', halign='center', valign='top'):
#                         img(style='width:128px', src=path)
    

with dominate.document('Data Visualization') as web:
    h2('{0}'.format('Data Vis'))
    num_img = len(os.listdir('{0}'.format('Camera_RGB_FRONT')))
    print('Number of images in folder {0}: {1}'.format('Camera_RGB_FRONT', num_img))
    with table(border=1, style='table-layout: fixed;'):
        for i in range(num_img):
            with tr():
                with tr(style='word-warp: break-world;', halign='center', valign='top'):
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px')
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_RGB_FRONT', str(i)))
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px')
                with tr(style='word-warp: break-world;', halign='center', valign='top'):
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_RGB_LEFT', str(i)))
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_Seg_TOPDOWN_10_vis', str(i)))
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_RGB_RIGHT', str(i)))
                with tr(style='word-warp: break-world;', halign='center', valign='top'):
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px')
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_RGB_BACK', str(i)))
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px')
            with tr():
                with tr(style='word-warp: break-world;', halign='center', valign='top'):
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px')
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_Seg_FRONT_vis', str(i)))
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px')
                with tr(style='word-warp: break-world;', halign='center', valign='top'):
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_Seg_LEFT_vis', str(i)))
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_Seg_TOPDOWN_10_vis', str(i)))
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_Seg_RIGHT_vis', str(i)))
                with tr(style='word-warp: break-world;', halign='center', valign='top'):
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px')
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_Seg_BACK_vis', str(i)))
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px')
            with tr():
                with tr(style='word-warp: break-world;', halign='center', valign='top'):
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px')
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_Depth_FRONT_vis', str(i)))
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px')
                with tr(style='word-warp: break-world;', halign='center', valign='top'):
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_Depth_LEFT_vis', str(i)))
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_Seg_TOPDOWN_10_vis', str(i)))
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_Depth_RIGHT_vis', str(i)))
                with tr(style='word-warp: break-world;', halign='center', valign='top'):
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px')
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_Depth_BACK_vis', str(i)))
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px')
    h2('{0}'.format('Semantic_Comparision'))
    with table(border=1, style='table-layout: fixed;'):
        # with td(style='word-warp: break-world;', halign='center', valign='top', 'Camera_Seg_TOPDOWN_10_vis'):
        td('Camera_Seg_TOPDOWN_10_vis')
            # h3(style='width:128px', 'Camera_Seg_TOPDOWN_10_vis')
        td('Camera_Seg_TOPDOWN_15_vis')
            # h3(style='width:128px', 'Camera_Seg_TOPDOWN_15_vis')
        td('Camera_Seg_TOPDOWN_20_vis')
            # h3(style='width:128px', 'Camera_Seg_TOPDOWN_20_vis')
        for i in range(num_img):
            with tr():
                with tr(style='word-warp: break-world;', halign='center', valign='top'):
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_Seg_TOPDOWN_10_vis', str(i)))
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_Seg_TOPDOWN_15_vis', str(i)))
                    with td(style='word-warp: break-world;', halign='center', valign='top'):
                        img(style='width:128px', src='{0}/{1:0>6}.png'.format('Camera_Seg_TOPDOWN_20_vis', str(i)))
        


with open(os.path.join(web_path, 'index.html'), 'w') as fp:
    fp.write(web.render())

