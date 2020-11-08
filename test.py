import cv2
import numpy as np

def rgb2gray(rgb):
    assert(len(rgb.shape) == 3)

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

# cap = cv2.VideoCapture('/Users/dillon/Documents/TechVideos/two_second_screen_recording.mov')
cap = cv2.VideoCapture('/Users/dillon/Documents/TechVideos/me_moving_my_head_3_seconds.mov')
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('Frame count:', frameCount)

frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('Frame width:', frameWidth)

frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('Frame height:', frameHeight)

buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))
gray_buf = np.empty((frameCount, frameHeight, frameWidth), np.dtype('uint8'))

fc = 0
ret = True

while (fc < frameCount  and ret):
    ret, buf[fc] = cap.read()
    gray_buf[fc] = rgb2gray(buf[fc])

    gray = np.float32(gray_buf[fc])
    dst = cv2.cornerHarris(gray,2,3,0.04)

    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)

    # Threshold for an optimal value, it may vary depending on the image.
    marked_img = buf[fc]
    marked_img[dst>0.01*dst.max()]=[0,0,255]

    cv2.imshow('dst', marked_img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

    fc += 1


cap.release()

sf = 640
ef = 480
num_frames = buf.shape[0]
writer = cv2.VideoWriter('gray_head.mp4', cv2.VideoWriter_fourcc(*'ffds'), 25, (sf, ef), True)
for i in range(num_frames):
    frame = buf[i, 0:480, 0:640]
    print('frame shape =', frame.shape)
    x = frame.astype('uint8')
    writer.write(x)

