# Realtime vehicle detection driver assistance system
Realtime vehicle detection for driver assistance using two approaches:
1. Traditional feature engineering approach: using Histogram of Oriented Gradients + Support vector machines. This approach proved to be very slow at the image level so we discontinued it
in favor of the deep learning based approach.

2. Deep learning based approach: Using state of the art convolutional neural networks architecture YOLO (You Only Look Once). The system was implemented using the reference framework [darknet](https://www.pjreddie.com/darknet/yolo/)
by the original authors of the [paper](https://arxiv.org/abs/1506.02640) . 

Environment:
---
The system was developed using the following:
1. **Hardware**: 
+ A PC running Ubuntu 16.04 LTS, Intel core i-5 4670-K, Nvidia GTX960, 8 GB RAM. We later ported it on a [Nvidia Jetson TK1](http://www.nvidia.com/object/jetson-tk1-embedded-dev-kit.html) to test its performance on a relatively modest embedded system.
2. **Software**: 
+ For various scripts, we needed Python 2 so we used Anaconda2.
+ Opencv 3.1.
+ CUDA 8.
+ cuDNN 5.1.

Project Goals:
---
+Our aim was to create a realtime vehicle detection systems that would detect the surrounding vehicles from the drivers using an incoming video stream only.

Project Information:
---
+We used a CNN based approach using YOLO. An extremely fast object detection and classification network. The framework we've used (darknet) is readily implemented in C and CUDA so it provided 
the maximum possible support for embedded systems with a GPU (Hence, the Jetson TK1 choice).
+Installing darknet is easy and simple. Training it wasn't. However, the internet is **thankfully** full of resources for that. We recommend [this repository](https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects).
+The network was trained using our custom CFG file and darknet pretrained vanilla weights. We used the Udacity dataset publicly available [here](https://github.com/udacity/self-driving-car/tree/master/annotations#dataset-2). We've written
our own scripts to convert the annotations to suit darknet. They're in the scripts folder along with other several useful scripts.

Project steps:
---
1. Download and extract the udacity dataset into a folder, then divide the dataset according to your liking(we used 10,000 for training, 3,000 for validation, & another unlabeled dataset for testing).
2. Run the necessary scripts to generate the files and annotations needed for training.
3. Run the anchors script to generate the anchors needed for your CFG file.
4. Create your CFG and data files as mentioned in the repository referenced [here](https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects).
5. Start training!
