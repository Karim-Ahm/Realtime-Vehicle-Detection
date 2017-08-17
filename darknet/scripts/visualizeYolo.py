import re
import numpy as np
from matplotlib import pyplot as plt

train_log_file = 'ainshams.log'


with open(train_log_file, "r") as log:
	logText = log.readlines()

logText = [re.sub('[^0-9a-zA-Z\s\.]+', '', line.strip()).split(" ")[0:3] for line in logText if "avg," in line]
logVals = np.array(logText).astype(np.float32)

plt.plot(logVals[:, 0], logVals[:, 1])
plt.ylim(plt.ylim()[0], 100)
plt.xlim(plt.xlim()[0], 6000)
plt.title("IOU")
plt.xlabel("Iteration #")
plt.ylabel("IOU %")
plt.tight_layout()
plt.savefig("avg-iou.png")
plt.close()

plt.plot(logVals[:, 0], logVals[:, 2])
plt.ylim(plt.ylim()[0], 100)
plt.xlim(plt.xlim()[0], 6000)
plt.title("Recall")
plt.xlabel("Iteration #")
plt.ylabel("Recall %")
plt.tight_layout()
plt.savefig("avg-recall.png")
plt.close()
