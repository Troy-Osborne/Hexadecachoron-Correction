import encodeBytes
import correction

def bin8(i):
    s=bin(i)[2:]
    l=len(s)
    return [0]*(8-l)+list(map(int,s))

def bytes_to_bits(Bytes):
    out=[]
    for i in Bytes:
        out+=bin8(i)
    return out

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

def encode_string(String):
    Bytes=String.encode()
    Out=b""
    while Bytes:
        Char=Bytes[:1]
        Out+=encodeBytes.encode_byte[Char]
        Bytes=Bytes[1:]
    return Out

def decode_to_string(Bytes):
    return Bytes[0::5].decode()

def check_and_decode_string(Bytes):
    Out=b""
    while Bytes:
        chunk=Bytes[0:5]
        if chunk in encodeBytes.decode_bytes:
            Val=encodeBytes.decode_bytes[chunk]
        else:
            Bits=bytes_to_bits(chunk)
            OutBits,Error=correction.decode(Bits)
            #print("Error Detected: Chunk is %02d hamming distance from nearest valid neighbour"%Error)
            Val=bits_to_bytes(OutBits)
        Out+=Val
        Bytes=Bytes[5:]
    return Out.decode()

def encode_file(InName,OutName):
    ChunkSize=1024# How many bytes to load into memory at once
    InFile=open(InName,"rb")
    OutFile=open(OutName,"wb")
    while 1:
        Chunk=InFile.read(ChunkSize)
        if Chunk:
            while Chunk:
                Char=Chunk[:1]
                OutFile.write(encodeBytes.encode_byte[Char])
                Chunk=Chunk[1:]
        else:
            break
    InFile.close()
    OutFile.flush()
    OutFile.close()
    return Out

def check_and_decode_file(InName,OutName):
    ChunkSize=256*5# How many bytes to load into memory at once
    InFile=open(InName,"rb")
    OutFile=open(OutName,"wb")
    while 1:
        Chunk=InFile.read(ChunkSize)
        if Chunk:
            while Chunk:
                Char=Chunk[:5]
                if Char in encodeBytes.decode_bytes:
                    Val=encodeBytes.decode_bytes[Char]
                else:
                    Bits=bytes_to_bits(Char)
                    OutBits,Error=correction.decode(Bits)
                    #print("Error Detected: Chunk is %02d hamming distance from nearest valid neighbour"%Error)
                    Val=bits_to_bytes(OutBits)
                OutFile.write(Val)
                Chunk=Chunk[5:]
        else:
            break
    InFile.close()
    OutFile.flush()
    OutFile.close()
    return Out
    
    



if __name__=="__main__":
    print("Running Tests")
    from random import randint
    In="This is my test string, I'm going to randomly set 1000 bits on it's encoding and see how we go getting it back"
    Out=encode_string(In)
    Encoding_Bits=bytes_to_bits(Out)
    for i in range(1000):
        Encoding_Bits[randint(0,len(Encoding_Bits)-1)]=randint(0,1)
    NewOut=bits_to_bytes(Encoding_Bits)
    print(check_and_decode_string(NewOut))
    encode_file("Hexadecachoron Encoding.py","TestEnc")
    check_and_decode_file("TestEnc","HDCrecovered.py")
