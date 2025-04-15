Hexadecachoron based error correction code.

Encoder and decoder are in the python directory.
I've left attached some of the prolog code I used to develop, analyse, and test the encoding.

Each input byte and their corresponding encodings are stored in "Hexadecachoron Definition.txt" 
The python directory provides encoding and decoding dictionaries which can operate directly on bytes and dictionaries which operate directly on bits.
These are available in encodeBytes and encodeBits respectively (contains the encoding and decoding)

Encoding functions and demos are available in "Hexadecachoron Encoding.py"; 
the bottom of this script contains a demo where it encodes and decode itself which can be repurposed as required.


I neglected to attach the main shape geometry library used to convert shapes into encodings however the main shape definition is 

shape(hexadecachoron, %name
	[XP,XN,YP,YN,ZP,ZN,WP,WN], %vertices
		[[XP,YP,ZP],  %face 1
		 [XP,YP,ZN],  %face 2
		 [XP,YN,ZP],  %and so on
		 [XP,YN,ZN],
		 [XP,YP,WP],
		 [XP,YP,WN],
		 [XP,YN,WP],
		 [XP,YN,WN],
		 [XP,ZP,WP],
		 [XP,ZP,WN],
		 [XP,ZN,WP],
		 [XP,ZN,WN],
		 [XN,YP,ZP],
		 [XN,YP,ZN],
		 [XN,YN,ZP],
		 [XN,YN,ZN],
		 [XN,YP,WP],
		 [XN,YP,WN],
		 [XN,YN,WP],
		 [XN,YN,WN],
		 [XN,ZP,WP],
		 [XN,ZP,WN],
		 [XN,ZN,WP],
		 [XN,ZN,WN],
		 [YP,ZP,WP],
		 [YP,ZP,WN],
		 [YP,ZN,WP],
		 [YP,ZN,WN],
		 [YN,ZP,WP],
		 [YN,ZP,WN],
		 [YN,ZN,WP],
		 [YN,ZN,WN]]).

The encodings for each shape are created by assigning a bit to each vertex, and then each parity bit is created by taking each face of the shape and xoring all the bits associated with vertices bordering that face and associing the result with the face.
The encoding is simply the vertices' bits followed by the faces' bits
