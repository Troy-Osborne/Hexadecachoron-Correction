from encodeBits import encode_dict,decode_dict
from functools import reduce
def hamming_distance(List1,List2):
        if len(List1)==len(List2):
                d=0
                for i in range(len(List1)):
                        d+=1 if List1[i]!=List2[i] else 0
                return d

def check_and_decode(Input):
        Input=tuple(Input)
        if Input in decode_dict:
                return (decode_dict[Input],0)
        closest=[None,999999]##initialise closest solution with arbitrary large distance (will be overwritten by first value)
        for key in encode_dict:
                value=encode_dict[key]
                Dist=hamming_distance(Input,value)
                if closest[1]>Dist:##If the hamming distance of the current value is lower than it's the closest value
                        closest=(key,Dist)
        return closest

def decode(Input):
        Input=tuple(Input)
        closest=[None,999999]##initialise closest solution with arbitrary large distance (will be overwritten by first value)
        for key in encode_dict:
                value=encode_dict[key]
                Dist=hamming_distance(Input,value)
                if closest[1]>Dist:##If the hamming distance of the current value is lower than it's the closest value
                        closest=(key,Dist)
        return closest
        
                
