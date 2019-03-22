import os, argparse, shutil
from gluoncv.utils import makedirs
import cv2

def parse_opts():
    parser = argparse.ArgumentParser(description='Preparing MINC 2500 Dataset',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--data', type=str, required=True,
                        help='directory for the original data folder')
    opts = parser.parse_args()
    return opts

# Preparation
opts = parse_opts()

path = opts.data

# Read files
train_images_file = os.path.join(path, 'TrainImages.txt')
with open(train_images_file, 'r') as f:
    train_images = f.readlines()

test_images_file = os.path.join(path, 'TestImages.txt')
with open(test_images_file, 'r') as f:
    test_images = f.readlines()

# Create directories
src_path = os.path.join(path, 'Images')
train_path = os.path.join(path, 'train')
test_path = os.path.join(path, 'val')
makedirs(train_path)
makedirs(test_path)

labels = sorted(os.listdir(src_path))

for l in labels:
    makedirs(os.path.join(train_path, l))
    makedirs(os.path.join(test_path, l))

# Copy files to corresponding directory
for im in train_images:
    im_path = im.strip('\n')
    img = cv2.imread(os.path.join(src_path, im_path))
    try:
        tmp = img.shape
    except AttributeError as e:
        print('train: ' + im_path)
        continue
    cv2.imwrite(os.path.join(train_path, im_path),img)
    '''
    shutil.copy(os.path.join(src_path, im_path),
                os.path.join(train_path, im_path))
    '''

for im in test_images:
    im_path = im.strip('\n')
    img = cv2.imread(os.path.join(src_path, im_path))
    try:
        tmp = img.shape
    except AttributeError as e:
        print('test: ' + im_path)
        continue
    cv2.imwrite(os.path.join(test_path, im_path),img)
    '''
    shutil.copy(os.path.join(src_path, im_path),
                os.path.join(test_path, im_path))
    '''
