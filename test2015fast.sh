#!/bin/bash
# Put this file under directory mc-cnn/
Folder_A="/data/jack/AutoNav_Data/data0/GoodCar/data/ConferenceHall/2/"
Folder_B="/data/jack/AutoNav_Data/data0/data/ConferenceHall/2/"
Destination_Folder="/data/jack/kitti2015fast/"
num_1_last=""
num_2_last=""

mkdir ${Destination_Folder}
echo "Under Folder_A:"
# Traverse files with .png suffix
for file_a in ${Folder_A}/*.png
do
	temp_file_a=`basename $file_a`
	echo "temp_file_a" $temp_file_a
	num_1=${temp_file_a%%_*}
	echo "num_1" $num_1
	num_2_tmp=${temp_file_a:2:4}
	num_2_tmp_1=${num_2_tmp%_*}
	num_2=${num_2_tmp_1#*_}
	echo "num_2" $num_2

#	break

	if [ "$num_1_last" = "$num_1" ] && [ "$num_2_last" = "$num_2" ]; then
		continue
	else
		num_1_last=${num_1}
		num_2_last=${num_2}
	fi 
	./main.lua kitti fast -a predict -net_fname net/net_kitti2015_fast_-a_train_all.t7 -left ${Folder_A}${num_1}_${num_2}_BACK_LEFT.png -right ${Folder_B}${num_1}_${num_2}_FRONT_RIGHT.png -disp_max 228
	luajit samples/bin2png.lua 
	# Take the camera position of LEFT picture as reference
	mv disp.png ${Destination_Folder}${num_1}_${num_2}_BACK_disp.png
	# mv left.png ${Destination_Folder}${num_1}_${num_2}_BACK_left.png
	# mv right.png ${Destination_Folder}${num_1}_${num_2}_BACK_right.png
	# mv left.bin ${Destination_Folder}${num_1}_${num_2}_BACK_left.bin
	# mv right.bin ${Destination_Folder}${num_1}_${num_2}_BACK_right.bin
	# mv disp.bin ${Destination_Folder}${num_1}_${num_2}_BACK_disp.bin
	
	./main.lua kitti fast -a predict -net_fname net/net_kitti2015_fast_-a_train_all.t7 -left ${Folder_A}${num_1}_${num_2}_FRONT_LEFT.png -right ${Folder_B}${num_1}_${num_2}_BACK_RIGHT.png -disp_max 228
	luajit samples/bin2png.lua 
	mv disp.png ${Destination_Folder}${num_1}_${num_2}_FRONT_disp.png
	# mv left.png ${Destination_Folder}${num_1}_${num_2}_FRONT_left.png
	# mv right.png ${Destination_Folder}${num_1}_${num_2}_FRONT_right.png
	# mv left.bin ${Destination_Folder}${num_1}_${num_2}_FRONT_left.bin
	# mv right.bin ${Destination_Folder}${num_1}_${num_2}_FRONT_right.bin
	# mv disp.bin ${Destination_Folder}${num_1}_${num_2}_FRONT_disp.bin
	
	./main.lua kitti fast -a predict -net_fname net/net_kitti2015_fast_-a_train_all.t7 -left ${Folder_A}${num_1}_${num_2}_LEFT_LEFT.png -right ${Folder_B}${num_1}_${num_2}_RIGHT_RIGHT.png -disp_max 228
	luajit samples/bin2png.lua 
	mv disp.png ${Destination_Folder}${num_1}_${num_2}_LEFT_disp.png
	# mv left.png ${Destination_Folder}${num_1}_${num_2}_LEFT_left.png
	# mv right.png ${Destination_Folder}${num_1}_${num_2}_LEFT_right.png
	# mv left.bin ${Destination_Folder}${num_1}_${num_2}_LEFT_left.bin
	# mv right.bin ${Destination_Folder}${num_1}_${num_2}_LEFT_right.bin
	# mv disp.bin ${Destination_Folder}${num_1}_${num_2}_LEFT_disp.bin

	./main.lua kitti fast -a predict -net_fname net/net_kitti2015_fast_-a_train_all.t7 -left ${Folder_A}${num_1}_${num_2}_RIGHT_LEFT.png -right ${Folder_B}${num_1}_${num_2}_LEFT_RIGHT.png -disp_max 228
	luajit samples/bin2png.lua 
	mv disp.png ${Destination_Folder}${num_1}_${num_2}_RIGHT_disp.png
	# mv left.png ${Destination_Folder}${num_1}_${num_2}_RIGHT_left.png
	# mv right.png ${Destination_Folder}${num_1}_${num_2}_RIGHT_right.png
	# mv left.bin ${Destination_Folder}${num_1}_${num_2}_RIGHT_left.bin
	# mv right.bin ${Destination_Folder}${num_1}_${num_2}_RIGHT_right.bin
	# mv disp.bin ${Destination_Folder}${num_1}_${num_2}_RIGHT_disp.bin

done

