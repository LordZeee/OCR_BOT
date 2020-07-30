import cv2
import pytesseract
import numpy as np

from PIL import Image
import os
import glob

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
def benchmark(func):
    def decorator(*args, **kwargs):
        import time
        time_ = time.time()

        ans = func(*args,**kwargs)
        print(time.time() - time_)
        return ans
    return decorator


def read_image(path: str):
    image_path = glob.glob(path + '/*.jpg')
    image = np.array([np.array(Image.open(i)) for i in image_path])

    return np.reshape(image, (image[0].shape[0], image[0].shape[1], image[0].shape[2]))


@benchmark
def preprocess_image(image):
    image = np.array(Image.open(image))
    image = np.reshape(image, (image.shape[0], image.shape[1], image.shape[2]))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(gray)
    # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # load the image as a PIL/PIllow image apply OCR
    text = pytesseract.image_to_string(gray)
    return text

    # os.remove(filename)


if __name__ == "__main__":
    path = r"C:\Users\malin\Desktop\Python\OCRBOT\\"
    image_path = glob.glob(path + '/*.jpg')
    text = [preprocess_image(i) for i in image_path]

    # text = preprocess_image(img_arrys)
    print(text[0])

