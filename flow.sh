#!bin/sh

# script for using https://github.com/Jiankai-Sun/dense_flow
DIR=' '
DEST=' '
DENSE_FLOW=/home/jack/dense_flow/build/extract_gpu

if [ ! -d "$DEST" ]; then
  mkdir $DEST
fi

for video in $DIR
do
    if test -f $video
    then
        mkdir $DEST$video
        echo $file 是文件
        $DENSE_FLOW -f $DIR$video -x $DEST$video/flow_x -y $DEST$video/flow_y -i $DEST$video/image -b 20 -t 1 -d 0 -s 1 -o dir
    fi
    if test -d $file
    then
        echo $file 是目录
    fi
done