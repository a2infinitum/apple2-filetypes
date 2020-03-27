# $C2 Paintworks Animation
This is a simple but popular format for animations the Apple IIgs computer.  It was originally intended for animating hand drawn frames in the Paintworks software with a simple streaming format that includes one keyframe, followed by a number of delta frames that update the changing pixels.

It is very easy to decode but is not optimized for speed or size.

## Format Specification
The file starts with an initial keyframe of image data, followed by total length and "playback speed", followed by a stream of frames data.
### Header
|  Offset  |	Length	 | Description                                         |
|:--------:|:-----------:|-----------------------------------------------------|
|  +$0000  |  	$8000	 | first uncompressed picture with SCBs and palettes   |
|  +$8000  |  	long (4) | length of animation data minus $8008                |
|  +$8004  |  	long (4) | timing of the animation (in VBLs)                   |
|  +$8008  |  	...      | frames of the animation                             |

The first 32KB ($0000-$8000) are basically a full dump of the [screen RAM with SCB and palette data.](https://github.com/digarok/gslib/blob/master/documentation/GS%20Video%20Layout.pdf)

### Frames data
Each frame has the following format:
|  Offset  |	Length	 | Description                                         |
|----------|-------------|-----------------------------------------------------|
|  +$0000  |  	long (4) | length of frame data in bytes including itself      |
|  +$0004  |    ...      | the animation data                                  |

### Animation data
Each value is a pair of words (2 bytes each in Apple IIgs endian)
The offset to screen is a value between $0000 and $7FFE.  This allows you to write to the screen's pixel, SCB, and palette RAM. 
- (In reality, playback engines don't check this offset and going above $7FFE will likely result in writing to areas above screen RAM.)

|  Offset  |	Length	 | Description                                         |
|:--------:|:-----------:|-----------------------------------------------------|
|  +$0000  |  	word (2) | offset to the screen (`$E12000,x` where x=offset)   |
|  +$0002  |    word (2) | value to put in screen data (i.e. 4 pixels in SHR)  |
|  +$0004  |  	word (2) | offset   "                                          |
|  +$0006  |    word (2) | value    "                                          |
|    ...   |             |                                                     |

If the offset to screen value is $0000, it is considered as a timing tick and the program must use the timing of the animation value.

## Compatible software
- [Paintworks Plus](http://www.whatisthe2gs.apple2.org.za/paintworks-plus)
- [Paintworks Gold](http://www.whatisthe2gs.apple2.org.za/paintworks-gold)
- [DreamGrafix](http://www.whatisthe2gs.apple2.org.za/dream-grafix)
- [PicViewer](http://www.brutaldeluxe.fr/products/apple2gs/picviewer.html)
- Jason Harper's AnimShow
