import cv2
from . import inf_data as iD
from config import Config

cam = cv2.VideoCapture(0)

#Settings date time in video------
pos_datetime = (15, 15)
font_datetime = cv2.FONT_HERSHEY_PLAIN
scale_font = 1
color_datetime = (255, 255, 255)
thickness_datetime = 1
type_linetext = cv2.LINE_AA

#Settings record------
nFrames = 20.0
vResolution = (640, 480)

vid_file = None
state = False

def getFrame():
    global vid_file, state
    while True:
        ret, frame = cam.read()
        if ret:
            if vid_file is not None:
                vid_file.write(frame)
                if state:
                    vid_file.release()
                    vid_file = None
                    state = False
            _, bufer = cv2.imencode(".jpg", frame)
            img = bufer.tobytes()
            yield b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + img + b"\r\n"

def add_datetime_frame(frame):
    cv2.putText(frame, iD.dateTime(), pos_datetime, font_datetime, scale_font, color_datetime, thickness_datetime, type_linetext)

def screen():
    name_img = "img_{}.jpg".format(iD.get_uuid())
    dir_img = Config.CAP_IMG_FOLDER + "/" + name_img
    ret, frame = cam.read()
    if ret:
        cv2.imwrite(dir_img, frame)
    return name_img

def record():
    global vid_file, state

    if vid_file is None:
        name_vid = "vid_{}.avi".format(iD.get_uuid())
        dir_vid = Config.CAP_VID_FOLDER+ "/" + name_vid
        vid_file = cv2.VideoWriter(dir_vid, cv2.VideoWriter_fourcc(*'XVID'), nFrames, vResolution)
        return True

    else:
        state = True
        return False
