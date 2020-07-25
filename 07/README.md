# $07 Font
This file type was reserved for Apple /// Font resources. Other applications have adopted the file type for their own purposes, and are described here.

TODO: Document Apple /// Font format. I believe this is 1024 bytes, 8 bytes per character (for characters $00 through $7F), using 7 bits per byte with least significant bit in each byte being the leftmost pixel.

# BeagleWrite
The file's aux type is the "font number", which is used as the sort order in the application.

## Format Specification
The file starts with a header, followed by character index, followed by glyph bitmaps.

### Header
|  Offset  | Length   | Description                                         |
|:--------:|:--------:|-----------------------------------------------------|
|  +$0000  | byte (1) | signature byte; always $20                          |
|  +$0001  | byte (1) | maximum character; usually $7F                      |
|  +$0002  | byte (1) | font height in pixels                               |
|  +$0003  | byte (1) | font baseline (offset from top of glyph)            |
|  +$0004  | word (2) | EOF (should match the file length)                  |
|  +$0006  | ...      | index and bitmap data                               |

### Character Index
Following the header, for each character from 32 (space) to the maximum character has an index record:
|  Offset  | Length   | Description                                         |
|:--------:|:--------:|-----------------------------------------------------|
|  +$0000  | word (2) | bitmap offset (from start of file to bitmap)        |
|  +$0002  | byte (1) | width                                               |

The width is not just the glyph width in pixels. Only 7 bits per byte are used for the bitmap. If the actual glyph width is w, the stored value is w + floor(w/7).

### Glyph Bitmap
Following all character indexes is the glyph bitmap data.

Note that glyph bitmaps are referenced by offsets from the start of the file. That means that the overall order of data for the bitmap section of the file is not defined. If two characters had the same glyph, the same offsets could be used to reference the same bitmap data which would reduce the file size. This does not appear to occur in practice.

A glyph bitmap is row-ordered data; each glyph has the same height, so the same number of rows.

Each row has a sequence of bytes which encode 7 bits each of the bitmap. The lowest bit of each row is the leftmost pixel of the glyph. This is similar to Apple II high resolution graphics format. If w is the stored width in the character index, the number of bytes in each row is w/8.
