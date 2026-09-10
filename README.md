# Kinect-OCV

Scripts to read the kinect sensor depth map and to generate 3d meshes.

`blog_pi.py` - This script is to run the kinect sensor using Open CV in python, the installation and setup for using a Raspberry Pi is described here. However it should run on any device with Open CV, libfreenect2 and pylibfreenetc2 installed. In other we can scan and produce an image like the one below.


![Hand Scan](renders/hand.png)

The notebook `3DRENDERS.ipynb` contains a small set of interactve cv2 filters to remove some edges and to generate a 3d mesh of the image loaded, using Pyvista. In other words we take the image produced with the sensor and produce a mesh like the one below.

![Hand Render](renders/hand.gif)

A full tutorial on hardware and software about this project can be found [here](https://www.hackster.io/kupkasmale/super-cheap-3d-scanner-camera-controller-b1ff81)



