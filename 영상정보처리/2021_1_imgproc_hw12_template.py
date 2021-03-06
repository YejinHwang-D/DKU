# -*- coding: utf-8 -*-
"""2021-1-ImgProc-HW12-Template.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W0_nHX2RcCd2awXYr1MN69C5rfEtQK-0

## 영상정보처리 12주차 과제 템플리트

이름: 황예진            
학번: 32195044

입력 이미지: 자유

# 구글 드라이브 마우팅 및 작업 경로로 이동
- 다음 쉘에 필요한 작업을 하시오.
"""

from google.colab import drive
drive.mount('/gdrive')

# Commented out IPython magic to ensure Python compatibility.
# %cd /gdrive/My Drive/Classroom/[영상정보처리] 2000004793-2021-1/2021-1 영상정보처리 12강/
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage.measure import compare_ssim

## print function
def show_with_matplotlib(img, title):
  """Shows an image using matplotlib capabilities"""

  #Convert BGR image to RGB:
  img_RGB = img[:,:,::-1]
  
  #Show the image using matplotlib:
  plt.imshow(img_RGB)
  plt.title(title)
  plt.show()

def show_with_matplotlib_gray(img, title):
  plt.imshow(img, cmap="gray")
  plt.title(title)
  plt.show()

image_path = '../Dongkeun-OpenCV-ImgData/lenna.png'
image_path2 = '../Dongkeun-OpenCV-ImgData/chessBoard.jpg'

"""##문제 1

입력 이미지는 자유롭게 선택을 하여, Canny Algorithm 의 패러미터에 변경에 따른 결과를 보이고, 간단하게 이해한 바를 정리하시오. 






"""

src = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

edges1 = cv2.Canny(src, 30, 100)
edges2 = cv2.Canny(src, 50, 100)
edges3 = cv2.Canny(src, 50, 200) #범위를 늘리면 노이즈에 가까운 엣지는 사라진다.
edges4 = cv2.Canny(src, 50, 300)

show_with_matplotlib_gray(edges1, "edges1 with limits = (30, 100)")
show_with_matplotlib_gray(edges2, "edges2 with limits = (50, 100)")
show_with_matplotlib_gray(edges3, "edges2 with limits = (50, 200)")
show_with_matplotlib_gray(edges4, "edges2 with limits = (50, 300)")

"""---

# 1번 정리

low limit와 high limit를 사용해 범위를 조절하여 Edge를 조절할 수 있다. 범위가 작아질수록 검출되는 Edge가 섬세해진다. 반면에 범위가 넓어질수록 노이즈에 가까운 Edge는 제거된 것을 확인했다.

---

##문제 2

입력 이미지는 자유롭게 선택을 하여, 통계적 Hough Transform 에 사용되는 패러미터 변경에 따른 결과를 보이고, 간단하게 이해한 바를 정리하시오.
"""

## 통계적 Hough Transform
src = cv2.imread(image_path2) #사용할 원본 이미지
def hough_transform(low, high, thrsh): #패러미터 변경을 위한 함수
  gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
  edges = cv2.Canny(gray, low, high)
  lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180.0, threshold=thrsh)

  for line in lines:
   x1, y1, x2, y2 = line[0]
   cv2.line(src, (x1,y1), (x2,y2), (0,0,255), 2)
  show_with_matplotlib(src, "Image")

hough_transform(50, 100, 100) #Canny 범위 50~100 / threshold 값 100
hough_transform(50, 60, 100)  #Canny 범위 줄이고 / threshold 값 그대로
hough_transform(50, 100, 10)  #Canny 범위 50~100 / threshold 값 줄이고
hough_transform(50, 70, 50)   #Canny 범위 줄이고 / threshold 값 줄이고

"""---

# 2번 정리
Canny Edge 검출에서 범위를 줄이거나, HoughLinesP 함수에서 threshold 값을 작게 주면 검출되는 Edge의 수가 많아진다.
그러나 threshold값을 너무 많이 줄이게되면 직선이 난잡하게 검출된다. 
특히, threshold 값이 작아질수록 많은 선이 검출되지만 정확도가 떨어지고, 값이 커지면 적은 수의 직선이 검출되어 정확도는 높아졌다.

---
"""