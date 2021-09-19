# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:21:50 2019

@author: sebastian
"""
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians, pi
from rplidar import RPLidar
import numpy as np
import time


comport='COM3'

def genpoints():
    x=[]
    y=[]
    xx=0
    yy=0
    x.append(0)
    y.append(0)
    b=scanarea()
    temp=cordinateconversion(0,0,b,0)
    angle=0
    for n in range (0,3):
        for n in range (0,len(temp)):
            x.append(temp[n][0])
            y.append(temp[n][1])


        
        
        plt.scatter(x, y)
        plt.show()
        forward=spaceangle(0)        
        
        
        if forward>500:
            #go forward one second
            oldforward=forward
            newforward=spaceangle(0)
            if angle%360 ==0:
                yy+=(oldforward-newforward)
            elif angle%360 ==90:
                xx+=(newforward-oldforward)
            elif angle%360==180:
                yy+=(newforward-oldforward)
            elif angle%360==270:
                xx+=(oldforward-newforward)
            
        else:

            
     
            left=spaceangle(270)
        
            if left>500:
                #turn left
                #go forwardonesec
                oldforward=left
                newforward=spaceangle(0)             
                angle+=90
                if angle%360 ==0:
                    yy+=(oldforward-newforward)
                elif angle%360 ==90:
                    xx+=(newforward-oldforward)
                elif angle%360==180:
                    yy+=(newforward-oldforward)
                elif angle%360==270:
                    xx+=(oldforward-newforward)
               
            else:
                right=spaceangle(90)
            
                if right>500:
                    #turn right
                    #go forwardonesec
                    oldforward=right
                    newforward=spaceangle(0)
                    (oldforward-newforward)
                    angle+=270
                    if angle%360 ==0:
                        yy+=(oldforward-newforward)
                    elif angle%360 ==90:
                        xx+=(newforward-oldforward)
                    elif angle%360==180:
                        yy+=(newforward-oldforward)
                    elif angle%360==270:
                        xx+=(oldforward-newforward)
                else:
                    break
        b=scanarea()
        temp=cordinateconversion(xx,yy,b,angle)
        
        

    return(x,y)



def scanarea():
    lidar = RPLidar(comport)
   
    for i, scan in enumerate(lidar.iter_scans()):
        if i > 0:
            break
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
    time.sleep(1)
    return(scan)
    

def spaceangle(n):

    r=scanarea()
    if n==0:
        low =359
        high=1
    else:
        low=n-1
        high=n+1
    for n in range(0,len(r)):
        if r[n][1] > (low) or r[n][1] < (high):
            return(r[n][2])



def point_pos(x0, y0, d, theta):
    theta_rad = pi/2 - radians(theta)
    return x0 + d*cos(theta_rad), y0 + d*sin(theta_rad)

def cordinateconversion(x0,y0,pointlist,theta):
    temparray=[]
    for n in range(0,len(pointlist)):
        temp=point_pos(x0,y0,pointlist[n][2],pointlist[n][1]+theta)
        temparray.append(temp)
    return(temparray)
    


x,y=genpoints()
np.savetxt('pointx.txt',x, delimiter=" ")
np.savetxt('pointy.txt',y, delimiter=" ")
lidar.disconnect()




x=np.loadtxt('pointx.txt', delimiter=" ")
y=np.loadtxt('pointy.txt', delimiter=" ")
plt.scatter(x, y)
plt.show()




