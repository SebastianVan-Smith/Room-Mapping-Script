# Room-Mapping-Script
This is the Scripts for my room mapping robot.

I always wanted to make a robot that could autonomusly naviagte through a room (this hasnt got there yet but it will!). 
The first step in that is knowing the area you can move in and that is where this project comes in.

The Mark Evison Foundation provided the funds to make the robot that accompanies this script. 

Currently it only outputs a point cloud but with my skills at the time that was all i could do, i hope to expand it in the future to use more advanced techniques.

It has a 2D lidar ontop that provides angle and distance data for a few hundred points in a full rotation i then convert this to cartesian coordianes and store them
It then moves in the space as the lidar has limited range and also to see arround obstacles in the room. It then overlapps these and provides a completed point cloud
