import cv2 as cv
import numpy as np
from constant import COLORS, RADIUS, CANVAS_SIZE
from function import draw_time

# Generate gradient image
gradient = np.zeros(CANVAS_SIZE, dtype=np.uint8)
start_color = (255, 255, 255)  # Starting color (white)
end_color = (0, 0, 0)          # Ending color (black)

for i in range(CANVAS_SIZE[1]):
    t = i / CANVAS_SIZE[1]
    current_color = tuple(int(t * end + (1 - t) * start) for start, end in zip(start_color, end_color))
    gradient = cv.rectangle(gradient, (0, i), (CANVAS_SIZE[0], i + 1), current_color, -1)

# Create canvas
img = np.zeros(CANVAS_SIZE, dtype=np.uint8)
img[:] = gradient

cv.circle(img, (320, 320), RADIUS + 10, COLORS['magenta'], 3)
cv.putText(img, "amritesh.py", (215,230), cv.FONT_HERSHEY_TRIPLEX, 1, COLORS['dark_gray'], 1, cv.LINE_AA)
while True:
    image = img.copy()
    clock_face = draw_time(image)

    cv.imshow('clock', image)
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
