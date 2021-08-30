import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name, frame)
        start_time = time.time
        result = False

    return image_name
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_files(image_name):
    accessToken = 'sl.A1J4DS5UZ0cSO3ztY_9bVGE_a6td7moWJKl_zGp4VAYTZ5OYHcsQao6AXWUfgEhVCXoLeLH8gzGiANfZ9K_hxs942XcoPly5bzVlOrhASqLQn8JwVEgNYjt5BbYZx4qE0asNhbI'
    file = image_counter
    file_from = file
    file_to = "NewFolder1/" + (image_name)
    dbx = dropbox.Dropbox(accessToken)
    with open(file_from, 'rb')as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)

        print("file_upload")

def main():
    while(True):
        if((time.time() - start_time)>=300):
            name = take_snapshot()
            upload_files(name)

main()