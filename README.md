# Kinect-OCV

Scripts to read the kinect sensor depth map and to generate 3d meshes.

`blog_pi.py` - This script is to run the kinect sensor using Open CV in python, the installation and setup for using a Raspberry Pi is described here. However it should run on any device with Open CV, libfreenect2 and pylibfreenetc2 installed.

![](renders/hand.png)

The notebook `3DRENDERS.ipynb` contains a small set of interactve cv2 filters to remove some edges and to generate a 3d mesh of the image loaded, using Pyvista.

![](renders/hand.gif)

