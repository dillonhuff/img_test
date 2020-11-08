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
ef = 480
num_frames = buf.shape[0]
writer = cv2.VideoWriter('gray_head.mp4', cv2.VideoWriter_fourcc(*'ffds'), 25, (sf, ef), True)
for i in range(num_frames):
    frame = buf[i, 0:480, 0:640]
    print('frame shape =', frame.shape)
    # x = np.random.randint(255, size=(ef, sf)).astype('uint8')
    x = frame.astype('uint8')
    writer.write(x)

