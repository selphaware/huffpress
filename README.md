# Huffman compression and decompression functions and decorators (0.2.4)

## Compress function


```python
from huffpress.compress import compress
```

    """
    compress(inp: str, verbose: bool = False,
             mode: Mode = Mode.DEFAULT) -> CompData:

    Generic compression function taking in input either filename or
    string to compress.

    :param inp: filename or string text to compress
    :param verbose: set to True for printing console outputs
    :param mode:
                Mode.DEFAULT --> if file exists, compress file, otherwise
                                 compress string text
                Mode.FILE    --> compress file
                Mode.RAW     --> compress string text
    :return: if compressed file, return compressed output filename. otherwise,
             return bytearray compressed data
    """


```python
some_str = "Hello this is some text that will be encoded by the Huffman algorithm."
```


```python
comp_str = compress(some_str)
comp_str
```




    bytearray(b'\x07p\xbbNU\xb3\xdb?)\xa1\xc8\x98\xf2\xbb>v\xbb\xef\x1cB\x84\x88\x8f}<\xa8\xee\xaaR\xd6\xe1\xf7u\xa6\x0cWX\x80{"72":"01110","101":"000","108":"1011","111":"0100","32":"111","116":"001","104":"0101","105":"0110","115":"11001","109":"11010","120":"100110","97":"11011","119":"100111","98":"01111","110":"10000","99":"101000","100":"10001","121":"101001","117":"101010","102":"10010","103":"101011","114":"110000","46":"110001"}100111011')



## Decompress function


```python
from huffpress.decompress import decompress
```

    """
    decompress(inp: CompData, outfile: Optional[str] = None, verbose=False):

    Decompress bytearray data or contents of a file

    :param inp: either bytearray compressed data or the filename containing the
                data
    :param outfile: name of the output file name (optional)
    :param verbose: set to True for printing console outputs
    :return: either decompressed bytearray data or name of decompressed output
            file
    """


```python
decomp_byt = decompress(comp_str)
decomp_byt
```




    bytearray(b'Hello this is some text that will be encoded by the Huffman algorithm.')




```python
# Now let's compress a longer string
```


```python
long_str = "This is the start of a very long text.. It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like). Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc."
comp_long_str = compress(long_str)
comp_long_str
```




    bytearray(b'\x07\x9e\xc8k\x8d|\x91\xf5\x88\x19\xden\x9e\xf9\x0b<]\xad\xf8oy:w\xd1\x9ck\xa7\x8b\xb5\xbc\xd6&\xe8\x8dH\xaf\xcc\x97g\xc9&t\xe0Qd>\xa1\x8c~\xe3\xd65\x80\x97a_\xddg\xc9\x1e\x05\x16\x9b\xa2}\xce\xd8[;\xcd\xd3\xec\x96\x9f\xaaE\xbc]\xf4\x8b[\xd38\xe5x\xa5\x8e\xac\x9d\xe7\xb2?g\x16\xce\xf3uP\xb5\xbf}\xc0\xc3\xe8\xda\x95\x0e5\xf2I\x9cs\xc9+\xa7\x83\x81\x9e8O"j\xbb8A#\xd65\x80;\x95\x82\xed\xdeo\x13\x98B\xb5\xf4\xae\xfbl\xf4W\xf1\xfa\xa8Z\xdf\xbd\xbcN\xd8[<\x88\x1d~\xe7l-\x9eD\x0e\xf7_\x82i\x16\xb7\x8ex\xbb\xe9\xf1\x1d\'\x81E\xa6\xe8\x9fx\xda\xd8\x8dJw\x9f\x91\xac\xeb5\xa7\x1fo\xb2\xb7DjB\xd6\xfd\x92\xed)i\xae\x8c\xbf\xa8\xee\xfb%\xa7\x95\x8e8Wg\xd5\xd5G\xef\xb8\x18}\x1bR\xa1\xd2\xbeH\x88u\x99\x91Q\xcf\x07Y\x8f\xc3{\xcd}\x19}=\x14\x0b\xa5\xe6p\xfb\xd8\xb8\x18q\xda\x95\r\xef\xd41\x8fS\\\xf7\xc8x#Y\xf5\x1d\xde\x87\rz\xc1\x8cx\xb7\xc9\x11\x0e-25\xd6N\xf7\x91\x00]U\xef\x90\xa1v\xaf$\xbey\xbe\xf1\xbeW\xde\xf9\x0f\x92>\xc2\x81Z\xfd<\x0e\x0c\r}\xd6t\xba\xe1Yl\xd7\xe9\xe0p`k\xbb}\x94\x1b=\x1fyE\xa7\xc6\xec+\xf2T\x1dA\xd1\x97\xf2G\xc4t\x9b\xcd;\xef\xb8\x18}\x1bR\xa1\xc6\xbd\x0c6\x8d\x9dj\x84,\xf8oy\xdeo\x92?`\x16\xc1kz2\xfeY\xb1\xa3\x98-o\x16Z\xab\x02\xc9\xdf}\xc0\xc3\xe8\xda\x95\x0f$\xaf\xb8\x96\xf9#\xc5\x96\xaa\xc0\xb3{^\xb1\x19h\x0b\xebT!g\xc3{\xceo\x90\xf4-q\xf9#\xe7\xfb\xcf\xbc\xdeV\xbf\xaaE\xba7Sig\xd4\xdf`\x16\xc2\x1f\x1d\xf4\xf4\xf6\xa4bl\xef7\xcb6=\x19~\xae\x04\x86\xe8\x95\xf1\xcf\x8f\xe0\x9aOO\x96l}ln\x18\x16\xfb\x9d\xf4\xce\xfa3\xc9+\xd2\x82\xf8\xdf+\xec\xf9\xdd\xa3g\x98o\x9fqlP\t\xad\x7fr\xb3\xa4i\xfeH\xf8\x94\xdb\x8bc\xf3\x13v\x03\xb0\xdd\xf2\xcd\x8d\x1c\xc1ku\xf00Aaky\xaa-\x82\x91\x8d\x9dMt\x91\xad+\x9d\xf4g\xd4\x95\xf6}\x95\x14\x01\xa2\xbe-\xf2G\xcf\xf7\xa2\xf4\xef+\xea\x1c\x97\xc9\x1e\x06%(\xf7\x9b\xef\x9c\x04\xa3\x9e\xa4NW\xb9\xdb\x10XZ\xdf\xbe\xe0a\xf4mJ\x87\xd9*\x92\xd3Z\xfa2\xfc\x1c\x0f\x03ql\x8d\x9fP\xe4\xba\xcdi\xc7\xdb\xec\xad\xd1\x1a\x90\xb5\xbe\x9el\xd4\x80|GI\xf7\x84V\xaa\xf7\xa9-3\xf2i!\xc5\xae\x8a\x96-o\xbeB\x85\xda\xbb\xcd\xf7\xdc\x0c>\x8d\xa9P\x9d\xe7\xb2 z\x01\xf0F\xb3\xdf@\x14\xc1v\xae\xf3}\x92\xa9-5\xdeo\xbe\xe0a\xf4mJ\x87K\xe81M\xd1:\xfe\xe5g\xc9\x1f\x04\x9f8\x0eY\xe4\x97\xcf\xa5M1\x02\xbe\x91\xc2\t\x82\xed\xc5\xbd<\x0f\x99\xc2\x1a\xfe\xeb8\xb4\xf8\xdd\x85~J\x83\xa85\xf7\x0e\x08\xcbx\r\x15\xfdN\x0b\xaf\xaaCt\xba\xdd\xb7\xb9\xe2\xef\xa7\x9b\xe5\xbdDm\x96F\xcf\xb8\xc4M\xf4\xdd\x13;\xe8\x9b\xd8\xea\xe8\x07\xda\xe2\xd6\xfc~\xaa=>\xc9T\x96\x9e\xf3}\xf7\x03\x0f\xa3jT5\xfb\x1d]\x89_\xc7\xfb\x8f\xa5\x01\xf9"\x07\x8d6\xf7:5\x99!ky\x86\xe4\x00J\xa1k|\x85k-\xc5\xbeH\xf8\n\xd7\x13\xdeo\x86\xf7\x93\xbd\xe1\x18\xfc\x91\xfb\xee\x06\x1fF\xd4\xa8{K\x10Lp\xae\xed\xf2G\xe8l \xc7>\x16_\xc7\xe0v)\x9f`+3\x0b\x15\xfb\xa4\xa6\xd3]+\xb1\xb8\xd5 Y\xaf\xc14\x8b[\xf2C_$|\xc2\x15\x9f\x01G\xdaX\x82c\x87v\xf9#\xf46\x10c\x93\xbe\x8c\xea\xa3]:\xc6\xec\x17d\x0b;\xcd\xde\xf9\x0fz\xf7\x9b\xcf\xbe\x98-\xf58.\xb5\xfb\x9e\x1b\x85\x8a\xfe\xa1\xc9t\xf2F\\\xca\x8fy\xbc\x1df>\x8bak\x8f\xac\x05]\x8a\x03Z\xfe?\xb4\xb1\x04\xc3\xf7\xdc\x0c>\x8d\xa9P\xfa\xa47K\xc5\xdfMp)N\xc9\xba&w\x9e\xc8\xfbK\x10L+\xfb\xee\x06\x1fF\xd4\xa8q\xaf\x92 fp=#\xa9,\xaf0\x13\xe6\x07\x87\x03\xb1\xc1\xc1v\xd7\xc5\xa7\xc6\xec+\xf2T\x1dA\xaf\xb8vv\x9e]$\x04\xbb\x08\r`\xdd\xf58.\xb9\xcb\xa7\x00{"84":"100111101","104":"10010","105":"0001","115":"1010","32":"111","116":"1100","101":"001","97":"0100","114":"0000","111":"0111","102":"100110","118":"1011111","121":"101100","108":"10001","110":"0110","103":"101101","120":"101111011","46":"1001110","73":"1101000","98":"1101110","100":"01011","99":"101110","119":"1101010","112":"110110","107":"1101001","117":"01010","76":"11011111","109":"10000","45":"100111100","44":"1101011","39":"110111101","67":"10111100010","69":"10111100011","77":"1001111110","86":"10111100100","40":"10111100101","106":"100111110","41":"10111100110","49":"1001111111","53":"10111100111","48":"110111100","57":"10111101000","54":"10111101001","65":"1011110000","80":"10111101010","50":"10111101011"}1011011010')




```python
print(f"Length of original text: {len(long_str)}\nLength of compressed text: {len(comp_long_str)}")
```

    Length of original text: 1979
    Length of compressed text: 1829
    

# Compress and Decompress file


```python
!dir *.txt
```

     Volume in drive C has no label.
     Volume Serial Number is 6600-2488
    
     Directory of C:\Users\datas\PycharmProjects\main\TMP
    
    08/09/2021  18:33           481,072 text_file.txt
                   1 File(s)        481,072 bytes
                   0 Dir(s)  509,271,748,608 bytes free
    


```python
comp_file = compress("text_file.txt")
comp_file
```




    'text_file.txt.hac'




```python
!dir text_file.*
```

     Volume in drive C has no label.
     Volume Serial Number is 6600-2488
    
     Directory of C:\Users\datas\PycharmProjects\main\TMP
    
    08/09/2021  18:33           481,072 text_file.txt
    08/09/2021  18:59           288,356 text_file.txt.hac
                   2 File(s)        769,428 bytes
                   0 Dir(s)  509,271,392,256 bytes free
    


```python
decomp_file = decompress("text_file.txt.hac", "outfile.txt")
decomp_file
```




    'outfile.txt'




```python
!dir *.txt*
```

     Volume in drive C has no label.
     Volume Serial Number is 6600-2488
    
     Directory of C:\Users\datas\PycharmProjects\main\TMP
    
    08/09/2021  18:59           481,072 outfile.txt
    08/09/2021  18:33           481,072 text_file.txt
    08/09/2021  18:59           288,356 text_file.txt.hac
                   3 File(s)      1,250,500 bytes
                   0 Dir(s)  509,270,908,928 bytes free
    


```python
!fc text_file.txt outfile.txt
```

    Comparing files text_file.txt and OUTFILE.TXT
    FC: no differences encountered
    
    

## Compress and Decompress sub-functions

    """
    compress_string(inp_st: str, verbose=False) -> bytearray:

    Compresses input string using the Huffman Encoding algorithm

    :param inp_st: input string to be compressed
    :param verbose: set to True for printing console outputs
    :return: compressed data in bytearray format
    """
    
    """
    compress_file(inp_file: str, verbose: bool = False):

    Compresses the contents of a file and outputs to a file
    with extension ".hac"

    e.g. some_file.ext --- compressed to --> some_file.ext.hac

    :param inp_file: input file to compress
    :param verbose: set to True for printing console outputs
    :return: name of the compressed output file
    """
    
    """
    decompress_bytes(inp_bytes: bytes, verbose=False) -> bytearray:

    Main function to decompress input bytes by extracting the Huffman map
    and using the map to replace the encoded sequences with the original
    characters.

    :param inp_bytes: Input data to be compressed
    :param verbose: set to True for printing console outputs
    :return: decompressed bytearray data
    """
    
    """
    decompress_file(inp_file: str, outfile: Optional[str] = None,
                    verbose=False):

    Decompress file

    :param inp_file: File to be decompressed
    :param outfile: Output file for decompressed contents to be saved
    :param verbose: set to True for printing console outputs
    :return: name and path of the output file
    """

## Decorator examples

### Compression decorator


```python
from huffpress.decorators import comp
```

    """
    comp(fun)
    
    Compression decorator, which compresses final string result

    :param fun: Function to be decorated
    :return: decorator function
    """
    def decorator(*args, **kwargs) -> bytearray:
        """
        Compresses final result before returning

        :param args: Original list args
        :param kwargs: Original dict args
        :return: Compressed string in bytearray format
        """


```python
@comp
def multiply_string(inp_string):
    # do some processing...
    final_string = inp_string
    return final_string * 500
```


```python
in_st = "This will be Huffman encoded many times."
dec_string = multiply_string(in_st)
dec_string[-1000:]  # observe last 1000 chars of compressed string
```




    bytearray(b'\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc4&{U \x15\x7fX\xd1\x1c-\xbf\xaey\xf9\xdc-\x85\x8c\xe7\xf7\x88L\xf6\xaa@*\xfe\xb1\xa28[\x7f\\\xf3\xf3\xb8[\x0b\x19\xcf\xef\x10\x99\xedT\x80U\xfdcDp\xb6\xfe\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc4&{U \x15\x7fX\xd1\x1c-\xbf\xaey\xf9\xdc-\x85\x8c\xe7\xf7\x88L\xf6\xaa@*\xfe\xb1\xa28[\x7f\\\xf3\xf3\xb8[\x0b\x19\xcf\xef\x10\x99\xedT\x80U\xfdcDp\xb6\xfe\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc4&{U \x15\x7fX\xd1\x1c-\xbf\xaey\xf9\xdc-\x85\x8c\xe7\xf7\x88L\xf6\xaa@*\xfe\xb1\xa28[\x7f\\\xf3\xf3\xb8[\x0b\x19\xcf\xef\x10\x99\xedT\x80U\xfdcDp\xb6\xfe\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc4&{U \x15\x7fX\xd1\x1c-\xbf\xaey\xf9\xdc-\x85\x8c\xe7\xf7\x88L\xf6\xaa@*\xfe\xb1\xa28[\x7f\\\xf3\xf3\xb8[\x0b\x19\xcf\xef\x10\x99\xedT\x80U\xfdcDp\xb6\xfe\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc0{"84":"01000","104":"01001","105":"1001","115":"11101","32":"101","119":"01010","108":"0000","98":"01011","101":"1111","72":"01100","117":"01101","102":"0001","109":"1100","97":"0010","110":"1101","99":"01110","111":"01111","100":"0011","121":"10000","116":"10001","46":"11100"}100010110')




```python
print(f"Length of original string: {len(in_st) * 500}\nLength of compressed string: {len(dec_string)}")
```

    Length of original string: 20000
    Length of compressed string: 10726
    


```python
decompress(dec_string)[-2000:]  # last 2000 chars of decompressed data
```




    bytearray(b'This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.')



### Decompression decorator


```python
from huffpress.decorators import decomp
```

    """
    Decompression decorator, which first decompresses given bytearray variable
    objects before proceeding with the rest of the function

    :param bytearray_vars: Bytearray variables to decompress first
    :return: decorator function
    """
    def inner(fun):
        """
        Inner decorator for decompression
        :param fun: Function to decorate
        :return: inner decorator function
        """
        def decorator(*args, **kwargs):
            """
            Decompress bytearray input variables first before proceeding

            :param args: Original list args
            :param kwargs: Original dict args
            :return: usual returning from fun
            """


```python
@decomp("in_var")
def process_string(in_var: str):
    print(in_var[-1000:])
```


```python
print(dec_string[-1000:])
print("\n\nDecompressing via decomp decorator\n\n")
process_string(in_var=dec_string)  #  must provide the input variable key name i.e. in_var
```

    bytearray(b'\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc4&{U \x15\x7fX\xd1\x1c-\xbf\xaey\xf9\xdc-\x85\x8c\xe7\xf7\x88L\xf6\xaa@*\xfe\xb1\xa28[\x7f\\\xf3\xf3\xb8[\x0b\x19\xcf\xef\x10\x99\xedT\x80U\xfdcDp\xb6\xfe\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc4&{U \x15\x7fX\xd1\x1c-\xbf\xaey\xf9\xdc-\x85\x8c\xe7\xf7\x88L\xf6\xaa@*\xfe\xb1\xa28[\x7f\\\xf3\xf3\xb8[\x0b\x19\xcf\xef\x10\x99\xedT\x80U\xfdcDp\xb6\xfe\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc4&{U \x15\x7fX\xd1\x1c-\xbf\xaey\xf9\xdc-\x85\x8c\xe7\xf7\x88L\xf6\xaa@*\xfe\xb1\xa28[\x7f\\\xf3\xf3\xb8[\x0b\x19\xcf\xef\x10\x99\xedT\x80U\xfdcDp\xb6\xfe\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc4&{U \x15\x7fX\xd1\x1c-\xbf\xaey\xf9\xdc-\x85\x8c\xe7\xf7\x88L\xf6\xaa@*\xfe\xb1\xa28[\x7f\\\xf3\xf3\xb8[\x0b\x19\xcf\xef\x10\x99\xedT\x80U\xfdcDp\xb6\xfe\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc0{"84":"01000","104":"01001","105":"1001","115":"11101","32":"101","119":"01010","108":"0000","98":"01011","101":"1111","72":"01100","117":"01101","102":"0001","109":"1100","97":"0010","110":"1101","99":"01110","111":"01111","100":"0011","121":"10000","116":"10001","46":"11100"}100010110')
    
    
    Decompressing via decomp decorator
    
    
    This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.
    


```python

```
