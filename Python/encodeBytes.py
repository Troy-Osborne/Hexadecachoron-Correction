from encodeBits import *

def bits_to_bytes(Bits):
    Out=b""
    while Bits:
        N=0
        if len(Bits)>7:
            for n in range(8):
                N+=Bits[n]<<(7-n)
            Bits=Bits[8:]
        else:
            for n in range(len(Bits)):
                N+=Bits[n]<<(7-n)
            Bits=Bits[8:]
        Out+=bytes([N])
    return Out


###Construct dictionaries that convert entire bytes back and forward.
###For encoding and decoding
###If these methods fail there is likely corruption or the data isn't formatted with this encoding.
###Corruption can be repaired by sending each 5 bytes as a list of 40 bits to check_and_decode in correction.py
##This should to repair most errors as well as returning an error score
encode_byte={}
decode_bytes={}

for In in encode_dict:
    InByte=bits_to_bytes(In)
    OutBytes=bits_to_bytes(encode_dict[In])
    encode_byte[InByte]=OutBytes
    decode_bytes[OutBytes]=InByte

