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

#AES    128         256


# Note: Output will be stored in 
# directory named {{output}}
##################################################


from time import time_ns
from numpy import frombuffer
from Cryptodome.Util.Padding import pad
from Cryptodome.Cipher import AES as Ori_AES
from Cryptodome.Random import get_random_bytes


class AES:
    def __init__(self, **kwargs):
        self.key = kwargs["key"] if ("key" in kwargs and len(kwargs["key"]) == 32) else get_random_bytes(32)
        self.model = Ori_AES.new(self.key, Ori_AES.MODE_ECB)

    def encrypt(self, pimage):         # image as numpy array
        image_byte = pad(pimage.tobytes(), 16)
        
        start_time = time_ns()
        image_enc_byte = self.model.encrypt(image_byte)
        print("Encryption time for AES: {:.3f}".format(time_ns()-start_time))

        image_enc_byte = image_enc_byte[:len(pimage.tobytes())]
        image_enc = frombuffer(image_enc_byte, dtype=pimage.dtype)
        return image_enc.reshape(pimage.shape)
    def decrypt(self, cimage):         # cypher image as numpy array
        image_dec_byte = self.model.decrypt(pad(cimage.tobytes(), 16))
        image_dec_byte = image_dec_byte[:len(cimage.tobytes())]
        image_dec = frombuffer(image_dec_byte, dtype=cimage.dtype)
        return image_dec.reshape(cimage.shape)
    def export(self):
        return (self.key)

if __name__ == "__main__":
    print("ERROR: Use as module")
