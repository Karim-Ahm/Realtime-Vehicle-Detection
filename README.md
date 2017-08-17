# Realtime vehicle detection driver assistance system
Realtime vehicle detection for driver assistance using two approaches:
1. Traditional feature engineering approach: using Histogram of Oriented Gradients + Support vector machines. This approach proved to be very slow at the image level so we discontinued it
in favor of the deep learning based approach.

2. Deep learning based approach: Using state of the art convolutional neural networks architecture YOLO (You Only Look Once). The system was implemented using the reference framework [darknet](https://www.pjreddie.com/darknet/yolo/)
by the original authors of the [paper](https://arxiv.org/abs/1506.02640) . 

Environment:
---
The system was developed using the following:
1. Hardware: A PC running Ubuntu 16.04 LTS, Core i-5 4670-K, Nvidia GTX960, 8 GB RAM. We later ported it on a [Nvidia Jetson TK1](http://www.nvidia.com/object/jetson-tk1-embedded-dev-kit.html) to test its performance on a relatively modest embedded system.
2. Software: 
2.1 For various scripts, we needed Python 2 so we used Anaconda2.
2.2 Opencv 3.1.
2.3 CUDA 8.
2.4 cuDNN 5.1.
