# -*- coding: utf-8 -*-
"""2021-1-ImgProc-HW4-Template.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16VqdE0c7S5AZk_QkgoYxLC6BgbipR6Ez

## 2021-1 영상정보처리 4주차 과제 템플리트
- 점수: 10점 만점
- 이미지 경로 잘못 사용한 경우: -3
- 문제1: 5점 
- 문제2: 5점

이름: 황예진            
학번: 32195044

이미지를 컬러로 읽기
동일 크기의 그레이스케일 공 이미지 만들기
컬러 이미지의 각 픽셀의 RGB 값을 이용하여 grayscale 값으로 만들어서 그레이스케일 이미지의 동일자리에 배정하기 -> 그레이스케일 이미지 만들기
새로운 컬러 공 이미지를 만들고, 그레이스케일 이미지 값을 참조하여 화소값을 채운 후 출력하시오
"""

from google.colab import drive 
drive.mount('/gdrive')

"""Souce image 는 다음의 image_path 를 변경하지 말고 이용할 것. 경로가 다른 경우 감점 -3"""

image_path = '../Dongkeun-OpenCV-ImgData/logo.png'

"""## 문제 1: 부분 이미지를 이용한 이미지 생성

1. 위의 이미지 경로를 이용하여 이미지를 컬러 이미지 org_image 로 읽기
2. 읽은 이미지와 동일 크기의 컬러 이미지를 new_image1 로 만들기 
3. new_image1 를 x 축 방향으로 4등분하고 왼쪽부터 subimage 1, 2, 3, 4 라고 할때 다음과 같이 new_image1을 구성하기 
  - x 축값이 4등분하여 4개의 영역이 동일 크기가 되지 않는 경우, 맨 오른쪽 영역에는 남는 크기 배분
  - subimage 1: 동일 영역에 해당하는 org_image 부분 복사하기 
  - subimage 2: 동일 영역에 해당하는 org_image 부분에서 Red 성분만 복사하고, green/blue 부분은 0으로 하여 subimage 2에 채워 넣을 것
  - subimage 3: 동일 영역에 해당하는 org_image 부분에서 Blue 성분만 복사하고, green/red 부분은 0으로 하여 subimage 3에 채워 넣을 것
  - subimage 4: 동일 영역에 해당하는 org_image 부분에서 Green 성분만 복사하고, blue/red 부분은 0으로 하여 subimage 4에 채워 넣을 것

4. new_image1 을 디스플레이하기 
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /gdrive/My Drive/Classroom/[영상정보처리] 2000004793-2021-1/2021-1 영상정보처리 4강/
import matplotlib.pyplot as pyplot
import numpy as np
import cv2

##### 1.
org_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
print(org_image.shape)
##### 2.
new_image1 = np.zeros(org_image.shape, np.uint8)

##### 3. 첫번째 방법
  #org_image의 BGR값을 가져온 후 다른 색상은 0으로 만들기
#subimage 1
new_image1[:, 0:121] = org_image[:, 0:121].copy()

#subimage 2 - Red만
new_image1[:, 121:242] = org_image[:, 121:242].copy()
g = new_image1[:, 121:242, 1] = 0 
b = new_image1[:, 121:242, 0] = 0

#subimage 3 - Blue만
new_image1[:, 242:363] = org_image[:, 242:363].copy()
r = new_image1[:, 242:363, 2] = 0
g = new_image1[:, 242:363, 1] = 0

#subimage 4 - Green만 
new_image1[:, 363:487] = org_image[:, 363:487].copy()
r = new_image1[:, 363:487, 2] = 0
b = new_image1[:, 363:487, 0] = 0

##### 4.
#BGR -> RGB 변환
new_image1 = cv2.cvtColor(new_image1, cv2.COLOR_BGR2RGB)
pyplot.imshow(new_image1)
pyplot.show()

##### 3. 두번째 방법
  #org_image의 BGR값을 HSV값으로 변환 후 copy해오기

#subimage 1
new_image1[:, 0:121] = org_image[:, 0:121].copy()

#subimage 2 - Red만
red = np.uint8([[[0, 0, 255]]])
hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)

  #색상 범위
lower_red = np.array([0, 255, 255])
upper_red = np.array([0, 255, 255])
  #cvtColor함수로 HSV값으로 변환하기
image_hsv = cv2.cvtColor(org_image, cv2.COLOR_BGR2HSV)
image_mask = cv2.inRange(image_hsv, lower_red, upper_red)
image_result = cv2.bitwise_and(org_image, org_image, mask=image_mask)
  #지정 영역 copy
new_image1[:, 121:242] = image_result[:, 121:242].copy()

#subimage 3 - Blue만
blue = np.uint8([[[255, 0, 0]]])
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)

  #색상 범위
lower_blue = np.array([120, 255, 255])
upper_blue = np.array([120, 255, 255])
  #cvtColor함수로 HSV값으로 변환하기
image_hsv = cv2.cvtColor(org_image, cv2.COLOR_BGR2HSV)
image_mask = cv2.inRange(image_hsv, lower_blue, upper_blue)
image_result = cv2.bitwise_and(org_image, org_image, mask=image_mask)
  #지정 영역 copy
new_image1[:, 242:363] = image_result[:, 242:363].copy()

#subimage 4 - Green만 
green = np.uint8([[[0, 255, 0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)

  #색상 범위
lower_green = np.array([60, 255, 255])
upper_green = np.array([60, 255, 255])
  #cvtColor함수로 HSV값으로 변환하기
image_hsv = cv2.cvtColor(org_image, cv2.COLOR_BGR2HSV)
image_mask = cv2.inRange(image_hsv, lower_green, upper_green)
image_result = cv2.bitwise_and(org_image, org_image, mask=image_mask)
  #지정 영역 copy
new_image1[:, 363:487] = image_result[:, 363:487].copy()

#BGR값을 RGB값으로 변환하여 출력
new_image1 = cv2.cvtColor(new_image1, cv2.COLOR_BGR2RGB)
pyplot.imshow(new_image1)
pyplot.show()

"""## 문제 2: 식을 이용한 grayscale 이미지 만들기 

1. org_image와 같은 크기의 공백 grayscale 이미지 new_image2 만들기
2. org_image 의 각 화소를 접근하여 강의에서 설명한 공식을 사용하여 grayscale 값으로 변환하여 새로운 그레이스케일 이미지 new_image2 에 저장하기
2. new_image2 디스플레이하기 

[참조] https://stackoverflow.com/questions/17615963/standard-rgb-to-grayscale-conversion


"""

##### 1.
row, col, ch = org_image.shape #org_image의 shape 정보
new_image2 = np.zeros((row, col), np.uint8) #new grayscale image

##### 2.

  # (1) 첫번째 방법 : 화소에 접근하여 공식 사용
def bgr_to_gray(img):
  b = img[:,:,0]
  g = img[:,:,1]
  r = img[:,:,2]
  gray = ((0.299 * r) + (0.587 * g) + (0.114 * b))
  return gray.astype(np.uint8)
new_image2 = bgr_to_gray(org_image)

##### 3.
new_image2 = cv2.cvtColor(new_image2, cv2.COLOR_BGR2RGB)
pyplot.imshow(new_image2)
pyplot.show()

##### 1.
org_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
row, col, ch = org_image.shape #org_image의 shape 정보
new_image2 = np.zeros((row, col), np.uint8) #new grayscale image

##### 2.

  # (2) 두번째 방법 : 각 화소에 접근하여 공식 사용
def bgr_to_gray(y, x, img):
  b = img[y,x,0]
  g = img[y,x,1]
  r = img[y,x,2]
  gray = ((0.299 * r) + (0.587 * g) + (0.114 * b))
  return gray.astype(np.uint8)

for y in range(row):
  for x in range(col):
    new_image2[y, x] = bgr_to_gray(y, x, org_image)


##### 3.
new_image2 = cv2.cvtColor(new_image2, cv2.COLOR_BGR2RGB)
pyplot.imshow(new_image2)
pyplot.show()