# Realtime vehicle detection driver assistance system
Realtime vehicle detection for driver assistance using two approaches:
1. Traditional feature engineering approach: using Histogram of Oriented Gradients + Support vector machines. This approach proved to be very slow at the image level so we discontinued it
in favor of the deep learning based approach.

2. Deep learning based approach: Using state of the art convolutional neural networks architecture YOLO (You Only Look Once). The system was implemented using the reference framework [darknet](https://www.pjreddie.com/darknet/yolo/)
mimicing the **Tiny YOLOv2** by the original authors of the [paper](https://arxiv.org/abs/1506.02640) . 

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
+ We used a CNN based approach using YOLO. An extremely fast object detection and classification network. The framework we've used (darknet) is readily implemented in C and CUDA so it provided 
the maximum possible support for embedded systems with a GPU (Hence, the Jetson TK1 choice).
+ Installing darknet is easy and simple. Training it wasn't. However, the internet is **thankfully** full of resources for that. We recommend [this repository](https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects).
+ The network was trained using our custom CFG file and darknet pretrained vanilla weights. We used the Udacity dataset publicly available [here](https://github.com/udacity/self-driving-car/tree/master/annotations#dataset-2). We've written
our own scripts to convert the annotations to suit darknet. They're in the scripts folder along with other several useful scripts.

Training steps:
---
1. Clone the repository, install the dependencies and build using `make` after navigating to the repository root folder.
2. Download and extract the udacity dataset into a folder, then divide the dataset according to your liking (we used 10,000 for training, 3,000 for validation, & another unlabeled dataset for testing).
3. Run the necessary scripts to generate the files and annotations needed for training.
4. Run the anchors script to generate the anchors needed for your CFG file.
![Anchors visualization](https://github.com/Karim-92/Realtime-Vehicle-Detection/blob/master/images/anchors5.png "Anchors")
5. Create your CFG and data files as mentioned in the repository referenced [here](https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects).
6. Start training!

Results:
---
+ We've obtained an IOU value of 61% at iteration 5,000. The recall rate peak was at 71%. On a GTX960 the network ran at 40FPS and on the Jetson TK1 it ran at 8FPS after various optimizations we've done to both the code and the board itself.
to put things into perspective, the GTX960 has 1024 CUDA cores while the Jetson TK1 has 192 CUDA cores only.

![](https://github.com/Karim-92/Realtime-Vehicle-Detection/blob/master/images/IOU.JPG "Peak IOU at Iteration 5,000")

![](https://github.com/Karim-92/Realtime-Vehicle-Detection/blob/master/images/Recall.JPG "71% Recall at Iteration 5,000")

![](https://github.com/Karim-92/Realtime-Vehicle-Detection/blob/master/images/loss.JPG "Loss function during training")

![](https://github.com/Karim-92/Realtime-Vehicle-Detection/blob/master/images/results1.JPG "Europe Results")

![](https://github.com/Karim-92/Realtime-Vehicle-Detection/blob/master/images/results1.JPG "Cairo Results")


Reproducing Results:
---
+ We were training for only 1 class, Car. We've trained for 8,000 iterations and found out that the best IOU result was obtained at iteration 5,000. You can download our weights file [here](link).
+ The config file of our network is readily present in the cfg folder, as well as the data and names files. However, you'll need to modify the training, validation and names paths in your data file to match those on your environment.
+ Once you're done training (or if you're using our weights file) you can simply invoke one of the following three commands to validate or test YOLO:

```
./darknet detector valid data/rtcd.data cfg/rtcd.cfg path-to-weights -thresh 0.4
./darknet detector test data/rtcd.data cfg/rtcd.cfg path-to-weights path-to-image -thresh 0.4
./darknet detector demo data/rtcd.data cfg/rtcd.cfg path-to-weights path-to-video -thresh 0.4
```


