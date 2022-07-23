##################################################
# Author:  Ravi Rahar
##################################################

##################################################
### install libraries
# $ pip install nympy, opencv-python, pycryptodomex, rsa
### Place image in this folder, rename it as "target.jpg"
### run Test.py
# $ python Test.py
##################################################

##################################################
# All symmetric algos use standard padding,
# while RSA uses padding from PKCS_OAEP standard

#Details of all algorithms:
#Algo   BlockSize   KeySize

#DES    64          56
#3DES   64          168
#AES    128         256
#RSA    128         256


# Note: Output will be stored in 
# directory named {{output}}
##################################################



from os import mkdir
from numpy import loadtxt, savetxt
from cv2 import merge, split, imread, imwrite, imshow

from DES import DES
from DES3 import DES3
from AES import AES
from RSA import RSA

class FileHandling:
    @staticmethod
    def save_image_in_channels(image, R_file, G_file, B_file):
        # method to split image in 3 channels and save in 3 files
        try:
            (B, G, R) = split(image)
            savetxt(R_file, R)
            savetxt(G_file, G)
            savetxt(B_file, B)
            return True
        except Exception as e:
            return e
        
    @staticmethod
    def load_image_from_channels(R_file, G_file, B_file):
        # method to merge channels of a image from 3 files and save 
        R = loadtxt(R_file, dtype="uint8") 
        G = loadtxt(G_file, dtype="uint8") 
        B = loadtxt(B_file, dtype="uint8") 
        return merge([B, G, R])




def main():
    try:
        mkdir("output")
    except OSError as error:
        print(error)  

    # Creating object of each encryption class
    model_DES = DES()
    model_DES3 = DES3()
    model_AES = AES()
    model_RSA = RSA()


    # load original image
    image = imread("target.jpg")
    # save image numpy array in txt
    FileHandling.save_image_in_channels(image, "output/Targettext_R.txt", "output/Targettext_G.txt", "output/Targettext_B.txt")


    #### 
    #DES
    #### 

    # encrypt image with DES, with padding
    image_enc_DES = model_DES.encrypt(image) 
    # save encrypted image
    imwrite("output/DES.jpg", image_enc_DES)
    # save encrypted image numpy array in txt
    FileHandling.save_image_in_channels(image_enc_DES, "output/DES_R.txt", "output/DES_G.txt", "output/DES_B.txt")


    #####
    #DES3
    #####

    # encrypt image with DES3, with padding
    image_enc_DES3 = model_DES3.encrypt(image) 
    # save encrypted image
    imwrite("output/DES3.jpg", image_enc_DES3)
    # save encrypted image numpy array in txt
    FileHandling.save_image_in_channels(image_enc_DES3, "output/DES3_R.txt", "output/DES3_G.txt", "output/DES3_B.txt")


    #### 
    #AES
    #### 

    # encrypt image with AES, with padding
    image_enc_AES = model_AES.encrypt(image) 
    # save encrypted image
    imwrite("output/AES.jpg", image_enc_AES)
    # save encrypted image numpy array in txt
    FileHandling.save_image_in_channels(image_enc_AES, "output/AES_R.txt", "output/AES_G.txt", "output/AES_B.txt")


    #### 
    #RSA
    #### 

    # encrypt image with RSA, with padding
    image_enc_RSA = model_RSA.encrypt(image) 
    # save encrypted image
    imwrite("output/RSA.jpg", image_enc_RSA)
    # save encrypted image numpy array in txt
    FileHandling.save_image_in_channels(image_enc_RSA, "output/RSA_R.txt", "output/RSA_G.txt", "output/RSA_B.txt")

# running the main function
if __name__ == "__main__":
    main()
