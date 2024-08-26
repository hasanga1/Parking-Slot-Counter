import cv2
import pickle

carpark = cv2.imread('carPark.png')

# Slots dimentions
parkingSlotWidth = 100
parkingSlotHeight = 40

# Load previously added positions
try:
    with open('slotPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []


# Draw Rectangles
def handleClick(e, x, y, flags, params):
    global posList
    if e == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))

    if e == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + parkingSlotWidth and y1 < y < y1 + parkingSlotHeight:
                posList.pop(i)
                break
    
    with open('slotPos', 'wb') as f:
        pickle.dump(posList, f)

while True:
    # Create a copy of the original image for drawing
    display_img = carpark.copy()

    # Draw rectangles on the image based on positions in posList
    for pos in posList:
        cv2.rectangle(display_img, pos, (pos[0] + parkingSlotWidth, pos[1] + parkingSlotHeight), (153, 255, 51), 2)


    cv2.imshow("image", display_img)
    cv2.setMouseCallback("image", handleClick)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
