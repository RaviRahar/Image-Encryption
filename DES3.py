##################################################
# Author:  Ravi Rahar
##################################################

##################################################
### install libraries
# $ pip install nympy, opencv-python, pycryptodomex
### run Test.py
# $ python Test.py
##################################################

##################################################
# All symmetric algos use standard padding

#Details of all algorithms:
#Algo   BlockSize   KeySize

#3DES   64          168


# Note: Output will be stored in 
# directory named {{output}}
##################################################


from time import time_ns
from numpy import frombuffer
from Cryptodome.Util.Padding import pad
from Cryptodome.Cipher import DES3 as Ori_DES3
from Cryptodome.Random import get_random_bytes


class DES3:
    def __init__(self, **kwargs):
        self.key = kwargs["key"] if ("key" in kwargs and len(kwargs["key"]) == 24) else get_random_bytes(24)
        self.model = Ori_DES3.new(self.key, Ori_DES3.MODE_ECB)

    def encrypt(self, pimage):         # image as numpy array
        image_byte     = pad(pimage.tobytes(), 8)

        start_time = time_ns()
        image_enc_byte = self.model.encrypt(image_byte)
        print("Encryption time for DES3: {:.3f}".format(time_ns()-start_time))


        image_enc_byte = image_enc_byte[:len(pimage.tobytes())]
        image_enc = frombuffer(image_enc_byte, dtype=pimage.dtype)
        return image_enc.reshape(pimage.shape)
    def decrypt(self, cimage):         # cypher image as numpy array
        image_dec_byte = self.model.decrypt(pad(cimage.tobytes(), 8))
        image_dec_byte = image_dec_byte[:len(cimage.tobytes())]
        image_dec = frombuffer(image_dec_byte, dtype=cimage.dtype)
        return image_dec.reshape(cimage.shape)
    def export(self):
        return (self.key)

if __name__ == "__main__":
    print("ERROR: Use as module")
