import cv2
import numpy as np

# Load the two images
img1 = cv2.imread("rup (1).jpg")
img2 = cv2.imread("14e8bca29cf9aa7b3727b1b41e54dfb3.jpg")

# Resize both images to the same height for alignment
height = min(img1.shape[0], img2.shape[0])
img1_resized = cv2.resize(img1, (int(img1.shape[1] * height / img1.shape[0]), height))
img2_resized = cv2.resize(img2, (int(img2.shape[1] * height / img2.shape[0]), height))

# Combine images side by side
merged_image = np.hstack((img1_resized, img2_resized))

# Save or display the result
cv2.imwrite("merged_output.jpg", merged_image)
cv2.imshow("Merged Image", merged_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
