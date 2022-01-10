# This file is a cheat shit, it is not meant to be executed.

coach -p Doom_Health_Supreme_NoSpawn_DFP -e trash -r --evaluate -crd experiments/cpu_training_health_supreme_depth/27_12_2021-17_28/checkpoint/

coach -p Doom_Health_Supreme_DFP -n 1 -s 1800 -e cpu_training_health_supreme_depth_maze_from_depth -crd experiments/cpu_training_health_supreme_depth/27_12_2021-17_28/checkpoint/

dashboard -d experiments/cpu_training_health_supreme_depth_maze/28_12_2021-17_11/ -rc