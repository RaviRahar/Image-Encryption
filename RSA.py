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
# RSA uses padding from PKCS_OAEP standard

#Details of all algorithms:
#Algo   BlockSize   KeySize

#RSA    128         256


# Note: Output will be stored in 
# directory named {{output}}
##################################################


from time import time_ns
from numpy import frombuffer
import rsa

class RSA:
    def __init__(self, **kwargs):
        (self.public_key, self.private_key) =  rsa.newkeys(256)

    def encrypt(self, pimage):         # image as numpy array
        image_byte = pimage.tobytes()
        chunk_size = 16
        image_byte_chunks = [image_byte[i*chunk_size:i*chunk_size+chunk_size] for i in range(0, len(image_byte)//chunk_size)]
        image_byte_chunks += image_byte[chunk_size*(len(image_byte)//chunk_size):len(image_byte)] 
        image_enc_byte = b''

        start_time = time_ns()

        for _itr in image_byte_chunks:
            image_enc_byte += rsa.encrypt(_itr, self.public_key)

        print("Encryption time for RSA: {:.3f}".format(time_ns()-start_time))

        image_enc = frombuffer(image_enc_byte, dtype=pimage.dtype)
        shape = list(pimage.shape)
        shape[1] = -1
        return image_enc.reshape(shape)

    def decrypt(self, cimage, image_shape):         # cypher image as numpy array
        image_enc_byte = cimage.tobytes()
        chunk_size = 16
        image_byte_chunks = [image_enc_byte[i*chunk_size:i*chunk_size+chunk_size] for i in range(0, len(image_enc_byte)//chunk_size)]
        image_byte_chunks += image_enc_byte[chunk_size*(len(image_enc_byte)//chunk_size):len(image_enc_byte)] 
        image_enc_byte_chunks = [image_enc_byte[i:i+chunk_size] for i in range(0, len(image_enc_byte), chunk_size)]
        image_dec_byte = b''

        for _itr in image_enc_byte_chunks:
            image_dec_byte += rsa.decrypt(_itr, self.private_key)

        image_dec = frombuffer(image_dec_byte, dtype=cimage.dtype)
        return image_dec.reshape(image_shape)

    def export(self):
        return (self.private_key, self.public_key)

if __name__ == "__main__":
    print("ERROR: Use as module")
