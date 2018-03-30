#!/bin/bash

# Convert .json files to .obj and .mtl files for SUNCG
SEARCH_DIR=/home/jack/tmp/suncg_data/house/
SUNCG_COMMAND=/home/jack/Applications/SUNCGtoolbox/gaps/bin/x86_64/scn2scn
COUNTER=0
for DIR in `ls $SEARCH_DIR`
do
  echo $DIR
  cd $SEARCH_DIR$DIR
  $SUNCG_COMMAND house.json house.obj

  cd ..
  COUNTER=$(($COUNTER+1))
done
echo $COUNTER
