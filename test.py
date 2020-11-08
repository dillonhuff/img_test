import cv2
import numpy as np

# cap = cv2.VideoCapture('/Users/dillon/Documents/TechVideos/two_second_screen_recording.mov')
cap = cv2.VideoCapture('/Users/dillon/Documents/TechVideos/me_moving_my_head_3_seconds.mov')
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('Frame count:', frameCount)

frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('Frame width:', frameWidth)

frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('Frame height:', frameHeight)

buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))

fc = 0
ret = True

while (fc < frameCount  and ret):
    ret, buf[fc] = cap.read()
    fc += 1

cap.release()

# cv2.namedWindow('frame 10')
# cv2.imshow('frame 10', buf[9])

# cv2.waitKey(0)

sf = 640
num_frames = 200
writer = cv2.VideoWriter('gray_head.mp4', cv2.VideoWriter_fourcc(*'ffds'), 25, (sf, 480), False)
for i in range(num_frames):
    x = np.random.randint(255, size=(480, sf)).astype('uint8')
    writer.write(x)

# height = 640 
# width = 480
# writer = cv2.VideoWriter('gray_head.mp4', cv2.VideoWriter_fourcc(*'ffds'), 25, (height, width), False)
# for i in range(100):
    # x = np.random.randint(255, size=(height, width)).astype('uint8')
    # writer.write(x)


# writer = cv2.VideoWriter('gray_head.mp4', cv2.VideoWriter_fourcc(*'ffds'), 25, (480, 640), False)
# for b in range(buf.shape[0]):
    # # x = buf[b].astype('uint8')
    # x = np.random.randint(255, size=(480, 640)).astype('uint8')
    # writer.write(x)
