from tkinter import filedialog,simpledialog
from tkinter import *
import cv2
import numpy as np
from hashlib import *
from mHash import *


def messageToBinary(message):
    if type(message) == str:
        return ''.join([format(ord(i), "08b") for i in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [format(i, "08b") for i in message]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Input type not supported")


def hideData(image, secret_message):
    # calculate the maximum bytes to encode
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    print("Maximum bytes to encode:", n_bytes)

    # Check if the number of bytes to encode is less than the maximum bytes in the image
    if len(secret_message) > n_bytes:
        raise ValueError("Error encountered insufficient bytes, need bigger image or less data !!")

    secret_message += "#####"  # you can use any string as the delimiter

    data_index = 0
    # convert input data to binary format using messageToBinary() function
    binary_secret_msg = messageToBinary(secret_message)

    data_len = len(binary_secret_msg)  # Find the length of data that needs to be hidden
    for values in image:
        for pixel in values:
            # convert RGB values to binary format
            r, g, b = messageToBinary(pixel)
            # modify the least significant bit only if there is still data to store
            if data_index < data_len:
                # hide the data into least significant bit of red pixel
                pixel[0] = int(r[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # hide the data into least significant bit of green pixel
                pixel[1] = int(g[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # hide the data into least significant bit of  blue pixel
                pixel[2] = int(b[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            # if data is encoded, just break out of the loop
            if data_index >= data_len:
                break

    return image


def showData(image):
    binary_data = ""
    for values in image:
        for pixel in values:
            r, g, b = messageToBinary(pixel)  # convert the red,green and blue values into binary format
            binary_data += r[-1]  # extracting data from the least significant bit of red pixel
            binary_data += g[-1]  # extracting data from the least significant bit of red pixel
            binary_data += b[-1]  # extracting data from the least significant bit of red pixel
    # split by 8-bits
    all_bytes = [binary_data[i: i + 8] for i in range(0, len(binary_data), 8)]
    # convert from bits to characters
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "#####":  # check if we have reached the delimeter which is "#####"
            break
    # print(decoded_data)
    return decoded_data[:-5]  # remove the delimeter to show the original hidden message


# Encode data into image
def encode_text():
    textDecoded.delete(1.0, END)
    # image_name = input("Enter image name(with extension): ")
    image = cv2.imread(imgPath)  # Read the input image using OpenCV-Python.
    # It is a library of Python bindings designed to solve computer vision problems.

    # details of the image
    print("The shape of the image is: ", image.shape)  # check the shape of image to calculate the number of bytes in it
    print("The original image is as shown below: ")
    resized_image = cv2.resize(image, (500, 500))  # resize the image as per your requirement
    cv2.imshow('Encode', image)  # display the image
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    # data = input("Enter data to be encoded : ")
    data = simpledialog.askstring("Input", "Enter data to be encoded", parent=t)
    if len(data) == 0:
        raise ValueError('Data is empty')

    # filename = input("Enter the name of new encoded image(with extension): ")
    filename = simpledialog.askstring("Input", "Enter the name of new encoded image(with extension)")
    encoded_image = hideData(image, data)  # call the hideData function to hide the secret message into the selected image
    cv2.imwrite(filename, encoded_image)
    textDecoded.insert(INSERT, f'Successfully encoded to {filename}')


# Decode the data in the image
def decode_text():
    textDecoded.delete(1.0, END)
    # read the image that contains the hidden image
    # image_name = input("Enter the name of the steganographed image that you want to decode (with extension) :")
    image = cv2.imread(imgPath)  # read the image using cv2.imread()

    # print("The Steganography image is as shown below: ")
    resized_image = cv2.resize(image, (500, 500))  # resize the original image as per your requirement
    cv2.imshow('Decode', image)  # display the Steganographed image
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    value = showData(image)
    textDecoded.insert(INSERT, f'Decoded: {value}')
    return value


def change_path():
    global imgPath
    t.filename = filedialog.askopenfilename(initialdir="C:\\Source\\Scripting\\Steganography", title="Select file",
                                               filetypes=(("png files", "*.png"), ("jpeg files", "*.jpg"), ("all files", "*.*")))
    imgPath = t.filename
    pathText.delete(1.0, END)
    pathText.insert(INSERT, f"Path: {imgPath}\n")
    pathText.update_idletasks()


#
# HASHING
def encrypt256(value):
    textEncResult.delete(1.0, END)
    signature = sha256(str(value.get("1.0", END)).strip().encode()).hexdigest()
    # return signature
    textEncResult.insert(INSERT, signature)


def encrypt512(value):
    textEncResult.delete(1.0, END)
    signature = sha512(str(value.get("1.0", END)).strip().encode()).hexdigest()
    # return signature
    textEncResult.insert(INSERT, signature)


def mHashEnc(value):
    textEncResult.delete(1.0, END)
    signature = hashEncrypt(str(value.get("1.0", END)).strip())

    print(signature)
    textEncResult.insert(INSERT, str(signature))


def mHashDec(value):
    textEncResult.delete(1.0, END)
    signature = hashDecrypt(str(value.get("1.0", END)).strip())

    # return signature
    textEncResult.insert(INSERT, signature)


#
#
def Steganography():
    global t, pathText, imgPath, textDecoded, textEnc, textEncResult
    t = Tk()
    baseBgColor = "#333"
    baseFgColor = "white"
    t.title("Cryptography")
    t.configure(bg=baseBgColor)
    t.geometry("950x600")
    imgPath = ''

    # ENCODING
    pathText = Text(t, width=120, height=2)
    pathText.configure(bg="lime green", fg="black")
    pathText.place(x=0, y=100)
    pathText.insert(INSERT, f'Path: {imgPath}')
    textDecoded = Text(t, width=120, height=2)
    textDecoded.configure(bg="lime green", fg="black")
    textDecoded.place(x=0, y=160)

    lblEncDec = Label(t, text="Encode/Decode Images", width='30', height='2', font=("Courier", 12), bg=baseBgColor, fg=baseFgColor).place(x=10, y=30)
    encode = Button(t, text="Encode", command=lambda: encode_text(), width=15, height=2, bg="lightskyblue2").place(x=350, y=30)
    decode = Button(t, text="Decode", command=lambda: decode_text(), width=15, height=2, bg="lightskyblue2").place(x=480, y=30)
    changePath = Button(t, text="Change Path", command=lambda: change_path(), width=15, height=2, bg="lightskyblue2").place(x=610, y=30)

    # SHA255/512 HASHING
    textEnc = Text(t, width=120, height=2)
    textEnc.configure(bg="lime green", fg="black")
    textEnc.place(x=0, y=300)
    textEncResult = Text(t, width=120, height=2)
    textEncResult.configure(bg="lime green", fg="black")
    textEncResult.place(x=0, y=360)
    lbl256512 = Label(t, text="Sha256 and Sha512 hash", width='30', height='2', font=("Courier", 12), bg=baseBgColor, fg=baseFgColor).place(x=10, y=250)
    sha256 = Button(t, text="sha256", command=lambda: encrypt256(textEnc), width=15, height=2, bg="lightskyblue2").place(x=350, y=250)
    sha512 = Button(t, text="sha512", command=lambda: encrypt512(textEnc), width=15, height=2, bg="lightskyblue2").place(x=480, y=250)
    mHashEncrypt = Button(t, text="mHash Encrypt", command=lambda: mHashEnc(textEnc), width=15, height=2, bg="lightskyblue2").place(x=610, y=250)
    mHashDecrypt = Button(t, text="mHash Decrypt", command=lambda: mHashDec(textEnc), width=15, height=2, bg="lightskyblue2").place(x=740, y=250)

    t.mainloop()


t = ''
pathText = ''
imgPath = ''
textDecoded = ''
textEnc = ''
textEncResult = ''
Steganography()  # encode image


# Reference: https://github.com/rroy1212/Image_Steganography/blob/master/ImageSteganography.ipynb

#

