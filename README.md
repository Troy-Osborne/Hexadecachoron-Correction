Hexadecachoron based error correction code.

While this was created as an error correction code for transmission on lossy or corruptable mediums, as well long term backup storage,
I may extend it in a attempt to make some post-quantum cryptography, however there are a few things I would need to brush up on before I plan that out.

Encoder and decoder are in the python directory.
I've left attached some of the prolog code I used to develop, analyse, and test the encoding.

Each input byte and their corresponding encodings are stored in "Hexadecachoron Definition.txt" 
The python directory provides encoding and decoding dictionaries which can operate directly on bytes and dictionaries which operate directly on bits.
These are available in encodeBytes and encodeBits respectively (contains the encoding and decoding)

Encoding functions and demos are available in "Hexadecachoron Encoding.py"; 
the bottom of this script contains a demo where it encodes and decode itself which can be repurposed as required.


I neglected to attach the main shape geometry library used to convert shapes into encodings however the main shape definition is 

Name=hexadecachoron,

Vertices=[XP,XN,YP,YN,ZP,ZN,WP,WN] %XYZW(Positive & Negative),

Faces=[[XP,YP,ZP],[XP,YP,ZN],[XP,YN,ZP],[XP,YN,ZN],[XP,YP,WP],[XP,YP,WN],[XP,YN,WP],[XP,YN,WN],[XP,ZP,WP],[XP,ZP,WN],[XP,ZN,WP],[XP,ZN,WN],[XN,YP,ZP],[XN,YP,ZN],[XN,YN,ZP],[XN,YN,ZN],[XN,YP,WP],[XN,YP,WN],[XN,YN,WP],[XN,YN,WN],[XN,ZP,WP],[XN,ZP,WN],[XN,ZN,WP],[XN,ZN,WN],[YP,ZP,WP],[YP,ZP,WN],[YP,ZN,WP],[YP,ZN,WN],[YN,ZP,WP],[YN,ZP,WN],[YN,ZN,WP],[YN,ZN,WN]],

shape(Name,
	Vertices,
	Faces).

The encodings for each shape are created by assigning a bit to each vertex, and then each parity bit is created by taking each face of the shape and xoring all the bits associated with vertices bordering that face and associing the result with the face.
The encoding is simply the vertices' bits followed by the faces' bits
