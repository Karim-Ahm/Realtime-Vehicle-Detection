# Realtime vehicle detection driver assistance system
Realtime vehicle detection for driver assistance using two approaches:
1. Traditional feature engineering approach: using Histogram of Oriented Gradients + Support vector machines. This approach proved to be very slow at the image level so we discontinued it
in favor of the deep learning based approach.

2. Deep learning based approach: Using state of the art convolutional neural networks architecture YOLO (You Only Look Once). The system was implemented using the reference framework [darknet](https://www.pjreddie.com/darknet/yolo/)
by the original authors of the [paper](https://arxiv.org/abs/1506.02640) . 
