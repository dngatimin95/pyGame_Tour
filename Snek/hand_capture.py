import cv2
import os
import sys


num_hands = input("Please enter the number of training images you want to capture: ")
hand_storage = "C:\\Users\\Darren\\Documents\\GitHub\\pyGame-Tour\\Snek\\hand"
label_name = input("Please enter the label of the image set: ")

font = cv2.FONT_HERSHEY_DUPLEX
label_name = os.path.join(hand_storage, label_name)
count = image_name = 0
click = False

try:
    os.mkdir(label_name)
except FileExistsError:
    image_name=len(os.listdir(label_name))

video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 2000)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 2000)

while True:
    ret, image = video.read()
    image = cv2.flip(image, 1)

    if not ret:
        continue
    if count == int(num_hands):
        break

    #Drawing a square with white border. Anything inside this square box will be captured as training image.
    cv2.rectangle(image, (200, 200), (550, 550), (255, 255, 255), 2)

    #Start capturing pictures when user presses 's' key
    if click:
        region_of_interest = image[200:550, 200:550]
        save_path = os.path.join(label_name, '{}.jpg'.format(image_name + 1))
        cv2.imwrite(save_path, region_of_interest)
        image_name += 1
        count += 1

    cv2.putText(image, "Fit the gesture inside the white box and Press 's' key to start clicking pictures", (20, 30), font, 0.8, (255, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(image, "Press 'q' to exit.", (20, 60), font, 0.8, (255, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(image, "Image Count: {}".format(count), (20, 100), font, 1, (12, 20, 200), 2, cv2.LINE_AA)
    cv2.imshow("Get Training Images", image)

    k = cv2.waitKey(10)
    if k==ord('q'):
            break
    if k == ord('s'):
        click = not click

print("\n\nDone\n\n")
video.release()
cv2.destroyAllWindows()
