#!/usr/bin/env python3

import sys, os, math
import cv2 as cv
import numpy as np
from pylibfreenect2 import Freenect2, SyncMultiFrameListener
from pylibfreenect2 import FrameType, Registration, Frame
from pylibfreenect2 import OpenGLPacketPipeline, CpuPacketPipeline

Xo = 100 
Yo = 100
nw= 100
nh= 100
Po= np.array([Xo,Yo])
Nmax = 4500;
cutoff = 700; 

def change_Xo(arg): global Xo; Xo = arg
def change_Yo(arg): global Yo; Yo = arg
def change_nh(arg): global nh; nh = arg
def change_nw(arg): global nw; nw = arg
def change_cut(arg): global cutoff; cutoff = arg

def kin_init():
    print('Hellou')
    fn = Freenect2()
    num_devices = fn.enumerateDevices()
    if num_devices == 0:
        print("No Kinect connected!")
        sys.exit(1)

    pipeline = OpenGLPacketPipeline()
    print("Kinect using OpenGL pipeline")

    return fn, pipeline 

def main():

    global Xo, Yo,  nw, nh;
    global cutoff;
    
    fn, pipeline = kin_init()
    serial = fn.getDeviceSerialNumber(0)
    device = fn.openDevice(serial, pipeline=pipeline)
    listener = SyncMultiFrameListener(FrameType.Depth)
    device.setIrAndDepthFrameListener(listener)
    device.start()
    
    cv.namedWindow('Depth')

    cv.createTrackbar('Xo', 'Depth', Xo, 170, change_Xo)
    cv.setTrackbarMin('Xo', 'Depth',30)
    cv.setTrackbarMax('Xo', 'Depth',414)

    cv.createTrackbar('Yo', 'Depth', Yo, 200, change_Yo)
    cv.setTrackbarMin('Yo', 'Depth',30)
    cv.setTrackbarMax('Yo', 'Depth',324)

    cv.createTrackbar('DY', 'Depth', nh, 100, change_nh)
    cv.setTrackbarMin('DY', 'Depth',10)
    cv.setTrackbarMax('DY', 'Depth',250)

    cv.createTrackbar('DX', 'Depth', nw, 100, change_nw)
    cv.setTrackbarMin('DX', 'Depth',10)
    cv.setTrackbarMax('DX', 'Depth',250)

    cv.namedWindow('Roi')

    cv.createTrackbar('Cutoff', 'Roi', cutoff, 550, change_cut)
    cv.setTrackbarMin('Cutoff', 'Roi',510)
    cv.setTrackbarMax('Cutoff', 'Roi',5000)


    u = True
    while u:

        frames = listener.waitForNewFrame()
        depth = frames["depth"].asarray()
        listener.release(frames)
        depth1 = (depth).astype(cv.numpy.uint8)
        depth1 = cv.applyColorMap(depth1, cv.COLORMAP_BONE)

        #Get the raw data and calculate the region of interest
        #data

        #Step 1: raw depth data
        Po = np.array([Xo,Yo])
        Dp = np.array([nw,nh])
        cv.rectangle(depth1,Po,Po+Dp,(2550,0),1)
        cv.imshow('Depth',depth1)
        
        #Step 2: Calculate the roi data with the cutoff value
        roidepth = depth[Yo:Yo+nh,Xo:Xo+nw].copy()
        roidepth[roidepth >cutoff]=0.0
        A = roidepth > 0
        roidepth[A]=25*Nmax/roidepth[A]

        wn = (roidepth).astype(cv.numpy.uint8)
        wn = cv.applyColorMap(wn, cv.COLORMAP_JET) 
        cv.imshow('Roi',wn)

        #ESC to quit
        if cv.waitKey(10) == 27:
            break


    device.stop()
    device.close()
    print("BYE!")

if __name__ == "__main__":

    print("SMILE") 
    main()
