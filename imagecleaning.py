import argparse
from pathlib import Path
import os
import cv2
import pickle

sep = os.path.sep

parser = argparse.ArgumentParser()
parser.add_argument("file_path", type=Path)

p = parser.parse_args()
if not p.file_path.exists():
    print('Invalid path')
    exit(1)

try:
    imgs = pickle.load(open(str(p.file_path)+sep+'imgs.pkl', 'rb'))
    print('Loaded images')
except Exception as e:
    imgs = []
    for file in os.listdir(str(p.file_path)):
        if (
            file.endswith('.jpg') or
            file.endswith('.jpeg') or
            file.endswith('.png') or
            file.endswith('.gif') 
        ):
            imgs.append(cv2.imread(str(p.file_path)+sep+file))
    pickle.dump(imgs, open(str(p.file_path)+sep+'imgs.pkl', 'wb'))
    print('Dumped images')

def print_click(event, x, y, flags, param):
    global mouseX, mouseY
    if event == cv2.EVENT_LBUTTONDOWN:
        mouseX, mouseY = x, y
        print(x, y)

keepGoing = True
i = 0
lastmove = 0
cv2.namedWindow('image')
cv2.setMouseCallback('image', print_click)
while keepGoing:
    img = imgs[i]
    height, width = img.shape[:2]
    side = min(height, width)
    c = (width//2, height//2)
    tl = (c[0] - side//2, c[1] - side//2)
    br = (c[0] + side//2, c[1] + side//2)
    cv2.rectangle(img, tl, br, (0,0,255), 5)
    cv2.imshow('image', img)
    key = cv2.waitKey(0)
    if key == ord('n') and i < len(imgs):
        i += 1
    elif key == ord('b') and i > 0:
        i -= 1
    elif key == ord('q'):
        keepGoing = False
        cv2.destroyAllWindows()