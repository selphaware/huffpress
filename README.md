# Huffman compression, decompression functions and decorators (1.0.54)

## Compress functions


```python
import huffpress
from huffpress.press.compress import compress
```


```python
help(huffpress.press.compress)
```

    Help on module huffpress.press.compress in huffpress.press:
    
    NAME
        huffpress.press.compress - (c) 2021 Usman Ahmad https://github.com/selphaware
    
    DESCRIPTION
        compress.py
        
        Contains all compression functions using the Huffman encoding algorithm to
        encode most frequently occurring terms with short binary sequences,
        and encoding least frequently occurring terms with longer binary sequences.
        
        Process:
        -------
        1) Input String -> 2) ASCII ordinal values -> 3) Huffman Encoding
        -> 4) Replace characters with Encodings -> NOTE: Most frequent characters
        will have shorter encodings than Least frequent characters. The idea is
        there will be numerous frequent characters, which can be replaced by a short
        binary encoding - and so when we 5) Pack binaries into buckets of
        length 8 -> we combine 2 or more characters into a single 8-bit byte,
        and hence 6) Convert the binaries of length 8 to decimal and 7) The decimals
        are ASCII ordinal values which can be converted to characters
        (ASCII values between 1 and 255).
    
    FUNCTIONS
        add_huff_map(final_seq: bytearray, huff_map: huffpress.huff.htypes.HuffCode) -> bytearray
            Concatenate the final generated Huffman sequence with the Huffman map,
            which is required for decoding the Huffman sequence.
            
            :param final_seq: final compressed Huffman sequence binaries computed by
                            compress_seq_bins function
            :param huff_map: Huffman map containing terms and their encoding
            :return: concatenated final_seq + huff_map in a bytearray sequence
        
        compress(inp: str, verbose: bool = False, mode: huffpress.auxi.modes.Mode = <Mode.DEFAULT: 0>) -> Union[str, bytearray]
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
        
        compress_bytes(inp_bytes: bytes, verbose: bool = False) -> bytearray
            Compress input data bytes using the Huffman Encoding algorithm.
            Function compress_string takes an input string which transforms to bytes,
            then calls this function to compress.
            
            :param inp_bytes: input data bytes to be compressed
            :param verbose: set to True for printing console outputs
            :return: Final compressed bytearray sequence
        
        compress_file(inp_file: str, verbose: bool = False)
            Compresses the contents of a file and outputs to a file
            with extension ".hac"
            
            e.g. some_file.ext --- compressed to --> some_file.ext.hac
            
            :param inp_file: input file to compress
            :param verbose: set to True for printing console outputs
            :return: name of the compressed output file
        
        compress_seq_bins(final_bins: List[str], verbose: bool = False) -> bytearray
            From a given list of binaries constructed from the final Huffman sequence
            i.e. create_seq_bins function, compress the binaries (converting) to an
            ASCII ordinal value.
            
            :param final_bins: list of binary sequences construct from the final
                                Huffman sequence
            :param verbose: set to True for printing console outputs
            :return: bytearray of ascii ordinal values constructed from the Huffman
                    sequence of binaries, which collapses 2 or
                    more characters into less number of characters for most frequent
                    occurring terms in the original raw data
        
        compress_string(inp_st: str, verbose: bool = False) -> bytearray
            Compresses input string using the Huffman Encoding algorithm
            
            :param inp_st: input string to be compressed
            :param verbose: set to True for printing console outputs
            :return: compressed data in bytearray format
        
        create_final_sequence(huff_seq_rem: Tuple[int, str], verbose: bool = False) -> str
            From a given Huffman encoded sequence (computed by create_huff_sequence
            function), convert to a binary sequence.
            
            :param huff_seq_rem: tuple of 0:Huffman sequence and 1:remainder length
                                (to be used for '0' padding)
            :param verbose: set to True for printing console outputs
            :return: final Huffman sequence converted to a binary sequence
        
        create_huff_sequence(huff: huffpress.huff.htypes.HuffCode, inp_data: huffpress.huff.htypes.InputData, verbose: bool = False) -> Tuple[int, str]
            Creates an encoded Huffman sequence from a given Huffman tree dictionary
            and input data string text.
            
            :param huff: Huffman tree dictionary (encoded sequences per term)
                        computed by hfunctions.create_huff_tree_encoding
            :param inp_data: input data string text to be encoded
            :param verbose: set to True for printing console outputs
            :return: (number of 0 paddings required, new encoded sequence)
        
        create_seq_bins(final_seq: str, verbose: bool = False) -> List[str]
            From a given final Huffman sequence (computed by create_final_sequence
            function) extract the sequence of binaries of length 8 and store in a list
            
            :param final_seq: Final Huffman sequence string of binaries
            :param verbose: set to True for printing console outputs
            :return:
    
    DATA
        List = typing.List
        Optional = typing.Optional
        Tuple = typing.Tuple
        Union = typing.Union
    
    FILE
        c:\programdata\anaconda3\lib\site-packages\huffpress\press\compress.py
    
    
    


```python
some_str = "Hello this is some text that will be encoded by the Huffman algorithm."
```


```python
comp_str = compress(some_str)
comp_str
```




    bytearray(b'\x07p\xbbNU\xb3\xdb?)\xa1\xc8\x98\xf2\xbb>v\xbb\xef\x1cB\x84\x88\x8f}<\xa8\xee\xaaR\xd6\xe1\xf7u\xa6\x0cWX\x80{"72":"1A","101":"8","108":"R","111":"K","32":"F","116":"9","104":"L","105":"M","115":"1L","109":"1M","120":"2U","97":"1N","119":"2V","98":"1B","110":"1C","99":"2W","100":"1D","121":"2X","117":"2Y","102":"1E","103":"2Z","114":"34","46":"35"}6P')



## Decompress functions


```python
from huffpress.press.decompress import decompress
```


```python
help(huffpress.press.decompress)
```

    Help on module huffpress.press.decompress in huffpress.press:
    
    NAME
        huffpress.press.decompress - (c) 2021 Usman Ahmad https://github.com/selphaware
    
    DESCRIPTION
        decompress.py
        
        Contains all decompression functions by first extracting the Huffman map
        from the input data and using the map to convert back the compressed
        characters to the original characters.
    
    FUNCTIONS
        decompress(inp: Union[str, bytes, bytearray], outfile: Union[str, NoneType] = None, verbose=False)
            Decompress bytearray data or contents of a file
            
            :param inp: either bytearray compressed data or the filename containing the
                        data
            :param outfile: name of the output file name (optional)
            :param verbose: set to True for printing console outputs
            :return: either decompressed bytearray data or name of decompressed output
                    file
        
        decompress_bytes(inp_bytes: bytes, verbose=False) -> bytearray
            Main function to decompress input bytes by extracting the Huffman map
            and using the map to replace the encoded sequences with the original
            characters.
            
            :param inp_bytes: Input data to be compressed
            :param verbose: set to True for printing console outputs
            :return: decompressed bytearray data
        
        decompress_file(inp_file: str, outfile: Union[str, NoneType] = None, verbose=False)
            Decompress file
            
            :param inp_file: File to be decompressed
            :param outfile: Output file for decompressed contents to be saved
            :param verbose: set to True for printing console outputs
            :return: name and path of the output file
        
        extract_huff_map(inp_bytes: bytes, verbose: bool = False) -> Tuple[huffpress.huff.htypes.HuffCode, int]
            Extract Huffman encoding dictionary map from the input data.
            
            :param inp_bytes: input sequence of bytes containing compressed data
                              and Huffman map
            :param verbose: set to True for printing console outputs
            :return: Huffmann map dictionary and the length of the map
        
        reverse_final_sequence(bstr: bytes, verbose: bool = False) -> str
            Convert the input (already compressed sequence) of ascii ordinal values to
            a binary sequence string, which is the encoded Huffman sequence
            
            :param bstr: input sequence of ascii ordinal values (compressed data
                         bytearray format)
            :param verbose: set to True for printing console outputs
            :return: binary string of compressed data (Huffman encoded sequence
                     of 0's and 1's)
        
        reverse_huff_sequence(huff_map: huffpress.huff.htypes.HuffCode, seq: str, verbose: bool = False) -> bytearray
            Reverse the input binary string Huffman encoded sequence --> back to the
            original characters. This is done by traversing through the sequence in
            order and identifying any of the Huffman encoded sequence from the
            given (huff) Huffman map. Since all encodings are unique at any length,
            we can replace in this forward travelling manner.
            
            :param huff_map: Huffman map containing the binary encodings to original
                         character
            :param seq: input binary string of Huffman encoded sequence
            :param verbose: set to True for printing console outputs
            :return:
    
    DATA
        Optional = typing.Optional
        Tuple = typing.Tuple
        Union = typing.Union
    
    FILE
        c:\programdata\anaconda3\lib\site-packages\huffpress\press\decompress.py
    
    
    


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




    bytearray(b'\x07\x9e\xc8k\x8d|\x91\xf5\x88\x19\xden\x9e\xf9\x0b<]\xad\xf8oy:w\xd1\x9ck\xa7\x8b\xb5\xbc\xd6&\xe8\x8dH\xaf\xcc\x97g\xc9&t\xe0Qd>\xa1\x8c~\xe3\xd65\x80\x97a_\xddg\xc9\x1e\x05\x16\x9b\xa2}\xce\xd8[;\xcd\xd3\xec\x96\x9f\xaaE\xbc]\xf4\x8b[\xd38\xe5x\xa5\x8e\xac\x9d\xe7\xb2?g\x16\xce\xf3uP\xb5\xbf}\xc0\xc3\xe8\xda\x95\x0e5\xf2I\x9cs\xc9+\xa7\x83\x81\x9e8O"j\xbb8A#\xd65\x80;\x95\x82\xed\xdeo\x13\x98B\xb5\xf4\xae\xfbl\xf4W\xf1\xfa\xa8Z\xdf\xbd\xbcN\xd8[<\x88\x1d~\xe7l-\x9eD\x0e\xf7_\x82i\x16\xb7\x8ex\xbb\xe9\xf1\x1d\'\x81E\xa6\xe8\x9fx\xda\xd8\x8dJw\x9f\x91\xac\xeb5\xa7\x1fo\xb2\xb7DjB\xd6\xfd\x92\xed)i\xae\x8c\xbf\xa8\xee\xfb%\xa7\x95\x8e8Wg\xd5\xd5G\xef\xb8\x18}\x1bR\xa1\xd2\xbeH\x88u\x99\x91Q\xcf\x07Y\x8f\xc3{\xcd}\x19}=\x14\x0b\xa5\xe6p\xfb\xd8\xb8\x18q\xda\x95\r\xef\xd41\x8fS\\\xf7\xc8x#Y\xf5\x1d\xde\x87\rz\xc1\x8cx\xb7\xc9\x11\x0e-25\xd6N\xf7\x91\x00]U\xef\x90\xa1v\xaf$\xbey\xbe\xf1\xbeW\xde\xf9\x0f\x92>\xc2\x81Z\xfd<\x0e\x0c\r}\xd6t\xba\xe1Yl\xd7\xe9\xe0p`k\xbb}\x94\x1b=\x1fyE\xa7\xc6\xec+\xf2T\x1dA\xd1\x97\xf2G\xc4t\x9b\xcd;\xef\xb8\x18}\x1bR\xa1\xc6\xbd\x0c6\x8d\x9dj\x84,\xf8oy\xdeo\x92?`\x16\xc1kz2\xfeY\xb1\xa3\x98-o\x16Z\xab\x02\xc9\xdf}\xc0\xc3\xe8\xda\x95\x0f$\xaf\xb8\x96\xf9#\xc5\x96\xaa\xc0\xb3{^\xb1\x19h\x0b\xebT!g\xc3{\xceo\x90\xf4-q\xf9#\xe7\xfb\xcf\xbc\xdeV\xbf\xaaE\xba7Sig\xd4\xdf`\x16\xc2\x1f\x1d\xf4\xf4\xf6\xa4bl\xef7\xcb6=\x19~\xae\x04\x86\xe8\x95\xf1\xcf\x8f\xe0\x9aOO\x96l}ln\x18\x16\xfb\x9d\xf4\xce\xfa3\xc9+\xd2\x82\xf8\xdf+\xec\xf9\xdd\xa3g\x98o\x9fqlP\t\xad\x7fr\xb3\xa4i\xfeH\xf8\x94\xdb\x8bc\xf3\x13v\x03\xb0\xdd\xf2\xcd\x8d\x1c\xc1ku\xf00Aaky\xaa-\x82\x91\x8d\x9dMt\x91\xad+\x9d\xf4g\xd4\x95\xf6}\x95\x14\x01\xa2\xbe-\xf2G\xcf\xf7\xa2\xf4\xef+\xea\x1c\x97\xc9\x1e\x06%(\xf7\x9b\xef\x9c\x04\xa3\x9e\xa4NW\xb9\xdb\x10XZ\xdf\xbe\xe0a\xf4mJ\x87\xd9*\x92\xd3Z\xfa2\xfc\x1c\x0f\x03ql\x8d\x9fP\xe4\xba\xcdi\xc7\xdb\xec\xad\xd1\x1a\x90\xb5\xbe\x9el\xd4\x80|GI\xf7\x84V\xaa\xf7\xa9-3\xf2i!\xc5\xae\x8a\x96-o\xbeB\x85\xda\xbb\xcd\xf7\xdc\x0c>\x8d\xa9P\x9d\xe7\xb2 z\x01\xf0F\xb3\xdf@\x14\xc1v\xae\xf3}\x92\xa9-5\xdeo\xbe\xe0a\xf4mJ\x87K\xe81M\xd1:\xfe\xe5g\xc9\x1f\x04\x9f8\x0eY\xe4\x97\xcf\xa5M1\x02\xbe\x91\xc2\t\x82\xed\xc5\xbd<\x0f\x99\xc2\x1a\xfe\xeb8\xb4\xf8\xdd\x85~J\x83\xa85\xf7\x0e\x08\xcbx\r\x15\xfdN\x0b\xaf\xaaCt\xba\xdd\xb7\xb9\xe2\xef\xa7\x9b\xe5\xbdDm\x96F\xcf\xb8\xc4M\xf4\xdd\x13;\xe8\x9b\xd8\xea\xe8\x07\xda\xe2\xd6\xfc~\xaa=>\xc9T\x96\x9e\xf3}\xf7\x03\x0f\xa3jT5\xfb\x1d]\x89_\xc7\xfb\x8f\xa5\x01\xf9"\x07\x8d6\xf7:5\x99!ky\x86\xe4\x00J\xa1k|\x85k-\xc5\xbeH\xf8\n\xd7\x13\xdeo\x86\xf7\x93\xbd\xe1\x18\xfc\x91\xfb\xee\x06\x1fF\xd4\xa8{K\x10Lp\xae\xed\xf2G\xe8l \xc7>\x16_\xc7\xe0v)\x9f`+3\x0b\x15\xfb\xa4\xa6\xd3]+\xb1\xb8\xd5 Y\xaf\xc14\x8b[\xf2C_$|\xc2\x15\x9f\x01G\xdaX\x82c\x87v\xf9#\xf46\x10c\x93\xbe\x8c\xea\xa3]:\xc6\xec\x17d\x0b;\xcd\xde\xf9\x0fz\xf7\x9b\xcf\xbe\x98-\xf58.\xb5\xfb\x9e\x1b\x85\x8a\xfe\xa1\xc9t\xf2F\\\xca\x8fy\xbc\x1df>\x8bak\x8f\xac\x05]\x8a\x03Z\xfe?\xb4\xb1\x04\xc3\xf7\xdc\x0c>\x8d\xa9P\xfa\xa47K\xc5\xdfMp)N\xc9\xba&w\x9e\xc8\xfbK\x10L+\xfb\xee\x06\x1fF\xd4\xa8q\xaf\x92 fp=#\xa9,\xaf0\x13\xe6\x07\x87\x03\xb1\xc1\xc1v\xd7\xc5\xa7\xc6\xec+\xf2T\x1dA\xaf\xb8vv\x9e]$\x04\xbb\x08\r`\xdd\xf58.\xb9\xcb\xa7\x00{"84":"N1","104":"1E","105":"H","115":"Q","32":"F","116":"S","101":"9","97":"K","114":"G","111":"N","102":"2U","118":"67","121":"30","108":"1D","110":"M","103":"31","120":"OR","46":"5Q","73":"6G","98":"6M","100":"17","99":"32","119":"6I","112":"3A","107":"6H","117":"16","76":"DB","109":"1C","45":"N0","44":"6J","39":"QL","67":"2QQ","69":"2QR","77":"1A6","86":"2QS","40":"2QT","106":"N2","41":"2QU","49":"1A7","53":"2QV","48":"QK","57":"2QW","54":"2QX","65":"1DC","80":"2QY","50":"2QZ"}DI')




```python
print(f"Length of original text: {len(long_str)}\nLength of compressed text: {len(comp_long_str)}")
```

    Length of original text: 1979
    Length of compressed text: 1577
    

# Compress and Decompress file


```python
!dir *.txt
```

     Volume in drive C has no label.
     Volume Serial Number is 6600-2488
    
     Directory of C:\Users\datas\PycharmProjects\main\TMP
    
    15/09/2021  16:14           481,072 outfile.txt
    08/09/2021  18:33           481,072 text_file.txt
                   2 File(s)        962,144 bytes
                   0 Dir(s)  479,901,315,072 bytes free
    


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
    15/09/2021  16:14           287,076 text_file.txt.hac
                   2 File(s)        768,148 bytes
                   0 Dir(s)  479,901,315,072 bytes free
    


```python
from huffpress.huff.htypes import InputData
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
    
    15/09/2021  16:14           481,072 outfile.txt
    08/09/2021  18:33           481,072 text_file.txt
    15/09/2021  16:14           287,076 text_file.txt.hac
                   3 File(s)      1,249,220 bytes
                   0 Dir(s)  479,899,254,784 bytes free
    


```python
!fc text_file.txt outfile.txt
```

    Comparing files text_file.txt and OUTFILE.TXT
    FC: no differences encountered
    
    

## Decorators


```python
from huffpress.press.decorators import comp, decomp
```


```python
help(huffpress.press.decorators)
```

    Help on module huffpress.press.decorators in huffpress.press:
    
    NAME
        huffpress.press.decorators - (c) 2021 Usman Ahmad https://github.com/selphaware
    
    DESCRIPTION
        decorators.py
        
        Contains decorators for compressing and decompressing variable objects
        
        e.g.
        
        # Function below with @comp decorator returns the compressed
        # byterray of "Hello world"
        @comp
        def some_fn():
            return "Hello world"
        
        
        # Function below decompresses contents of var2 first before proceeding
        # with the rest of the function
        @decomp("var2")
        def some_fn2(var1, var2):
            ...
    
    FUNCTIONS
        comp(fun)
            Compression decorator, which compresses final string result
            
            :param fun: Function where string output will be compressed
            :return: compressed string
        
        decomp(*bytearray_vars)
            Decompression decorator, which first decompresses given bytearray variable
            objects before proceeding with the rest of the function
            
            :param bytearray_vars: Bytearray variables to decompress first
            :return: function is run as normal with the input bytearray_vars
                    variables being decompressed first
    
    FILE
        c:\programdata\anaconda3\lib\site-packages\huffpress\press\decorators.py
    
    
    

### Compression decorator


```python
help(comp)
```

    Help on function comp in module huffpress.press.decorators:
    
    comp(fun)
        Compression decorator, which compresses final string result
        
        :param fun: Function where string output will be compressed
        :return: compressed string
    
    


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




    bytearray(b'\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc4&{U \x15\x7fX\xd1\x1c-\xbf\xaey\xf9\xdc-\x85\x8c\xe7\xf7\x88L\xf6\xaa@*\xfe\xb1\xa28[\x7f\\\xf3\xf3\xb8[\x0b\x19\xcf\xef\x10\x99\xedT\x80U\xfdcDp\xb6\xfe\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc4&{U \x15\x7fX\xd1\x1c-\xbf\xaey\xf9\xdc-\x85\x8c\xe7\xf7\x88L\xf6\xaa@*\xfe\xb1\xa28[\x7f\\\xf3\xf3\xb8[\x0b\x19\xcf\xef\x10\x99\xedT\x80U\xfdcDp\xb6\xfe\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc4&{U \x15\x7fX\xd1\x1c-\xbf\xaey\xf9\xdc-\x85\x8c\xe7\xf7\x88L\xf6\xaa@*\xfe\xb1\xa28[\x7f\\\xf3\xf3\xb8[\x0b\x19\xcf\xef\x10\x99\xedT\x80U\xfdcDp\xb6\xfe\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc4&{U \x15\x7fX\xd1\x1c-\xbf\xaey\xf9\xdc-\x85\x8c\xe7\xf7\x88L\xf6\xaa@*\xfe\xb1\xa28[\x7f\\\xf3\xf3\xb8[\x0b\x19\xcf\xef\x10\x99\xedT\x80U\xfdcDp\xb6\xfe\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc0{"84":"14","104":"15","105":"P","115":"1P","32":"D","119":"16","108":"G","98":"17","101":"V","72":"18","117":"19","102":"H","109":"S","97":"I","110":"T","99":"1A","111":"1B","100":"J","121":"1C","116":"1D","46":"1O"}60')




```python
print(f"Length of original string: {len(in_st) * 500}\nLength of compressed string: {len(dec_string)}")
```

    Length of original string: 20000
    Length of compressed string: 10657
    


```python
decompress(dec_string)[-2000:]  # last 2000 chars of decompressed data
```




    bytearray(b'This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.')



### Decompression decorator


```python
from huffpress.press.decorators import decomp
```


```python
help(decomp)
```

    Help on function decomp in module huffpress.press.decorators:
    
    decomp(*bytearray_vars)
        Decompression decorator, which first decompresses given bytearray variable
        objects before proceeding with the rest of the function
        
        :param bytearray_vars: Bytearray variables to decompress first
        :return: function is run as normal with the input bytearray_vars
                variables being decompressed first
    
    


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

    bytearray(b'\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc4&{U \x15\x7fX\xd1\x1c-\xbf\xaey\xf9\xdc-\x85\x8c\xe7\xf7\x88L\xf6\xaa@*\xfe\xb1\xa28[\x7f\\\xf3\xf3\xb8[\x0b\x19\xcf\xef\x10\x99\xedT\x80U\xfdcDp\xb6\xfe\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc4&{U \x15\x7fX\xd1\x1c-\xbf\xaey\xf9\xdc-\x85\x8c\xe7\xf7\x88L\xf6\xaa@*\xfe\xb1\xa28[\x7f\\\xf3\xf3\xb8[\x0b\x19\xcf\xef\x10\x99\xedT\x80U\xfdcDp\xb6\xfe\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc4&{U \x15\x7fX\xd1\x1c-\xbf\xaey\xf9\xdc-\x85\x8c\xe7\xf7\x88L\xf6\xaa@*\xfe\xb1\xa28[\x7f\\\xf3\xf3\xb8[\x0b\x19\xcf\xef\x10\x99\xedT\x80U\xfdcDp\xb6\xfe\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc4&{U \x15\x7fX\xd1\x1c-\xbf\xaey\xf9\xdc-\x85\x8c\xe7\xf7\x88L\xf6\xaa@*\xfe\xb1\xa28[\x7f\\\xf3\xf3\xb8[\x0b\x19\xcf\xef\x10\x99\xedT\x80U\xfdcDp\xb6\xfe\xb9\xe7\xe7p\xb6\x163\x9f\xde!3\xda\xa9\x00\xab\xfa\xc6\x88\xe1m\xfds\xcf\xce\xe1l,g?\xbcBg\xb5R\x01W\xf5\x8d\x11\xc2\xdb\xfa\xe7\x9f\x9d\xc2\xd8X\xce\x7fx\x84\xcfj\xa4\x02\xaf\xeb\x1a#\x85\xb7\xf5\xcf?;\x85\xb0\xb1\x9c\xfe\xf1\t\x9e\xd5H\x05_\xd64G\x0bo\xeb\x9e~w\x0bac9\xfd\xe2\x13=\xaa\x90\n\xbf\xach\x8e\x16\xdf\xd7<\xfc\xee\x16\xc2\xc6s\xfb\xc0{"84":"14","104":"15","105":"P","115":"1P","32":"D","119":"16","108":"G","98":"17","101":"V","72":"18","117":"19","102":"H","109":"S","97":"I","110":"T","99":"1A","111":"1B","100":"J","121":"1C","116":"1D","46":"1O"}60')
    
    
    Decompressing via decomp decorator
    
    
    This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.This will be Huffman encoded many times.
    

## Data structure types


```python
help(huffpress.huff.htypes)
```

    Help on module huffpress.huff.htypes in huffpress.huff:
    
    NAME
        huffpress.huff.htypes - (c) 2021 Usman Ahmad https://github.com/selphaware
    
    DESCRIPTION
        htypes.py
        
        Contains all Huffman Data Structure Types
    
    CLASSES
        builtins.object
            HuffCode
            HuffSeq
            HuffTerm
            HuffTuple
            InputData
            Leaves
            SortedTree
            TermFreq
        
        class HuffCode(builtins.object)
         |  HuffCode(data: Dict[int, str]) -> None
         |  
         |  HuffCode = Dict[int, str]
         |  
         |  Final encoded Huffman encoded sequences with key as the ordinal ASCII value
         |  and the value as the binary sequence string
         |  
         |  Methods defined here:
         |  
         |  __eq__(self, other)
         |  
         |  __init__(self, data: Dict[int, str]) -> None
         |  
         |  __repr__(self)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __annotations__ = {'data': typing.Dict[int, str]}
         |  
         |  __dataclass_fields__ = {'data': Field(name='data',type=typing.Dict[int...
         |  
         |  __dataclass_params__ = _DataclassParams(init=True,repr=True,eq=True,or...
         |  
         |  __hash__ = None
        
        class HuffSeq(builtins.object)
         |  HuffSeq(seq_term: str, huff_term: huffpress.huff.htypes.HuffTerm) -> None
         |  
         |  seq_term = str
         |  huff_term = HuffTerm
         |  
         |  Huffman sequence made up of the sequence of terms string and the HuffTerm
         |  
         |  Methods defined here:
         |  
         |  __eq__(self, other)
         |  
         |  __init__(self, seq_term: str, huff_term: huffpress.huff.htypes.HuffTerm) -> None
         |  
         |  __repr__(self)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __annotations__ = {'huff_term': <class 'huffpress.huff.htypes.HuffTerm...
         |  
         |  __dataclass_fields__ = {'huff_term': Field(name='huff_term',type=<clas...
         |  
         |  __dataclass_params__ = _DataclassParams(init=True,repr=True,eq=True,or...
         |  
         |  __hash__ = None
        
        class HuffTerm(builtins.object)
         |  HuffTerm(freq: int, node: Union[huffpress.huff.HuffNode.HuffNode, NoneType]) -> None
         |  
         |  freq = int
         |  node = Optional[HuffNode]]
         |  
         |  For a single Huffman Node we have a total number of frequency
         |  occurrences, and we have the node (which can be null)
         |  
         |  Methods defined here:
         |  
         |  __eq__(self, other)
         |  
         |  __init__(self, freq: int, node: Union[huffpress.huff.HuffNode.HuffNode, NoneType]) -> None
         |  
         |  __repr__(self)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __annotations__ = {'freq': <class 'int'>, 'node': typing.Union[huffpre...
         |  
         |  __dataclass_fields__ = {'freq': Field(name='freq',type=<class 'int'>,d...
         |  
         |  __dataclass_params__ = _DataclassParams(init=True,repr=True,eq=True,or...
         |  
         |  __hash__ = None
        
        class HuffTuple(builtins.object)
         |  HuffTuple(seq_term: str = '', total_freq: int = -1, node: Union[huffpress.huff.HuffNode.HuffNode, NoneType] = None) -> None
         |  
         |  seq_term = str
         |  total_freq = int,
         |  node = Optional[HuffNode]
         |  
         |  Similar structure to SortedTree where we have string term,
         |  total frequency, and the HuffNode (which could be null)
         |  
         |  Methods defined here:
         |  
         |  __eq__(self, other)
         |  
         |  __init__(self, seq_term: str = '', total_freq: int = -1, node: Union[huffpress.huff.HuffNode.HuffNode, NoneType] = None) -> None
         |  
         |  __repr__(self)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __annotations__ = {'node': typing.Union[huffpress.huff.HuffNode.HuffNo...
         |  
         |  __dataclass_fields__ = {'node': Field(name='node',type=typing.Union[hu...
         |  
         |  __dataclass_params__ = _DataclassParams(init=True,repr=True,eq=True,or...
         |  
         |  __hash__ = None
         |  
         |  node = None
         |  
         |  seq_term = ''
         |  
         |  total_freq = -1
        
        class InputData(builtins.object)
         |  InputData(data: Union[str, bytes]) -> None
         |  
         |  data = Union[str, bytes]
         |  
         |  Input data to be compressed will either be a string or sequence of bytes
         |  string e.g. "Hello"
         |  bytes e.g. b"ABC" or [65, 66, 67]
         |  
         |  Methods defined here:
         |  
         |  __eq__(self, other)
         |  
         |  __init__(self, data: Union[str, bytes]) -> None
         |  
         |  __repr__(self)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __annotations__ = {'data': typing.Union[str, bytes]}
         |  
         |  __dataclass_fields__ = {'data': Field(name='data',type=typing.Union[st...
         |  
         |  __dataclass_params__ = _DataclassParams(init=True,repr=True,eq=True,or...
         |  
         |  __hash__ = None
        
        class Leaves(builtins.object)
         |  Leaves(data: Dict[str, huffpress.huff.htypes.HuffTerm]) -> None
         |  
         |  data = Dict[str, HuffTerm]
         |  
         |  Initial set of leaves set as a dictionary of keys as the term made up of
         |  comma delimited ordinal ASCII values, and the value as the HuffTerm.
         |  
         |  Methods defined here:
         |  
         |  __eq__(self, other)
         |  
         |  __init__(self, data: Dict[str, huffpress.huff.htypes.HuffTerm]) -> None
         |  
         |  __repr__(self)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __annotations__ = {'data': typing.Dict[str, huffpress.huff.htypes.Huff...
         |  
         |  __dataclass_fields__ = {'data': Field(name='data',type=typing.Dict[str...
         |  
         |  __dataclass_params__ = _DataclassParams(init=True,repr=True,eq=True,or...
         |  
         |  __hash__ = None
        
        class SortedTree(builtins.object)
         |  SortedTree(data: List[huffpress.huff.htypes.HuffSeq]) -> None
         |  
         |  data = List[Tuple[str, HuffTerm]]
         |  
         |  Huffman tree structure, which is a list of tuples of the term made up of
         |  comma delimited ordinal ASCII values, and the HuffTerm. The list is sorted
         |  by the total number of frequency order in ascending order.
         |  
         |  Methods defined here:
         |  
         |  __eq__(self, other)
         |  
         |  __init__(self, data: List[huffpress.huff.htypes.HuffSeq]) -> None
         |  
         |  __repr__(self)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __annotations__ = {'data': typing.List[huffpress.huff.htypes.HuffSeq]}
         |  
         |  __dataclass_fields__ = {'data': Field(name='data',type=typing.List[huf...
         |  
         |  __dataclass_params__ = _DataclassParams(init=True,repr=True,eq=True,or...
         |  
         |  __hash__ = None
        
        class TermFreq(builtins.object)
         |  TermFreq(tf: Dict[int, int]) -> None
         |  
         |  tf = Dict[str, int]
         |  
         |  When calculating collections.Counter on a input string or bytes,
         |  we return a dictionary of key being the ordinal ASCII value, and
         |  the value being the frequency of occurrence in the input data.
         |  
         |  Methods defined here:
         |  
         |  __eq__(self, other)
         |  
         |  __init__(self, tf: Dict[int, int]) -> None
         |  
         |  __repr__(self)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __annotations__ = {'tf': typing.Dict[int, int]}
         |  
         |  __dataclass_fields__ = {'tf': Field(name='tf',type=typing.Dict[int, in...
         |  
         |  __dataclass_params__ = _DataclassParams(init=True,repr=True,eq=True,or...
         |  
         |  __hash__ = None
    
    DATA
        Dict = typing.Dict
        List = typing.List
        Optional = typing.Optional
        Union = typing.Union
    
    FILE
        c:\programdata\anaconda3\lib\site-packages\huffpress\huff\htypes.py
    
    
    

## Huffman functions


```python
help(huffpress.huff.hfunctions)
```

    Help on module huffpress.huff.hfunctions in huffpress.huff:
    
    NAME
        huffpress.huff.hfunctions - (c) 2021 Usman Ahmad https://github.com/selphaware
    
    DESCRIPTION
        hfunctions.py
        
        Contains all Huffman building and deconstructing functions
    
    FUNCTIONS
        build_leaves(term_freq: huffpress.huff.htypes.TermFreq, verbose: bool = False) -> huffpress.huff.htypes.Leaves
            Builds initial leaf HuffNode's from a given dictionary of character
            frequency occurrence counts
            
            :param term_freq: dictionary of frequency occurrence counts of a given
            string computed by calc_term_freq function
            :param verbose: set to True for printing console outputs
            :return: dictionary of leaf HuffNode's for a given character frequency
            count dictionary
        
        build_tree(sorted_new_tree: huffpress.huff.htypes.SortedTree, verbose: bool = False) -> Union[huffpress.huff.HuffNode.HuffNode, NoneType]
            Builds Huffman tree made out of HuffNode's, constructed from initial
            HuffNode leaves
            
            :param sorted_new_tree: sorted [ term, (total-frequency, HuffNode) ]
            :param verbose: set to True for printing console outputs
            :return: Built Huffman tree from initial asc sorted  list of leaves
                     HuffNode's computed by build_leaves function and sorted by
                     sort_tree function
        
        calc_term_freq(data: huffpress.huff.htypes.InputData) -> huffpress.huff.htypes.TermFreq
            Returns dictionary of frequency occurrence counts for each character
            of a given string
            
            e.g. "ABBcCC" --> { "A": 1, "B": 2, "c": 1, "C": 2 }
            
            :param data: input string text
            :return: dictionary of character frequency occurrence counts
        
        create_huff_tree(data, verbose: bool = False)
            creates Huffman tree, calling either:
            create_huff_tree(InputData, bool); or
            create_huff_tree(TermFreq, bool)
            
            :param data: InputData (str or bytes) or TermFreq term frequency counts
            :param verbose: bool - verbose for printing
        
        encode(data, tree: Union[huffpress.huff.HuffNode.HuffNode, NoneType], path: str = '', verbose: bool = False)
            encode function calling either:
            encode(int, HuffNode, str); or
            encode(Leaves, HuffNode, bool)
            :param verbose: bool for verbose printing
            :param path: str for 1, 0 paths visited
            :param data: either int (term) or Leaves (initial set of term leaves)
            :param tree: Huffman tree
        
        print_node(node: Union[huffpress.huff.HuffNode.HuffNode, NoneType], depth: int = 0, verbose: bool = True) -> str
            Recursive printing of the HuffNode tree showing all branches, leaves and
            their terms and total-frequencies
            
            :param node: HuffNode tree i.e. Huffman tree
            :param depth: How many whitespaces to print to represent depth level
                         (starting at depth 0)
            :param verbose: set to True to print to console, False to return string
                            output
            :return: None (prints Huffman tree to console)
        
        sort_tree(tree: huffpress.huff.htypes.Leaves, verbose: bool = False) -> huffpress.huff.htypes.SortedTree
            Sorts a Huffman tree dictionary by total frequency ascending order
            returning a list
            
            e.g.
            
            { "D": (4, HuffNode), "E": (3, HuffNode),
              "F": (7, HuffNode), "ABC": (2, HuffNode) }
            
            -->
            
            [ ("ABC", (2, HuffNode)), ("E", (3, HuffNode)),
              ("D", (4, HuffNode)), ("F", (7, HuffNode)) ]
            
            :param tree: dictionary of HuffNode's { term : (total-frequency, HuffNode) }
            :param verbose: set to True for printing console outputs
            :return: sorted dictionary of HuffNode's converted to a list
    
    DATA
        ItemsView = typing.ItemsView
        List = typing.List
        Optional = typing.Optional
    
    FILE
        c:\programdata\anaconda3\lib\site-packages\huffpress\huff\hfunctions.py
    
    
    

## Huffman node class


```python
help(huffpress.huff.HuffNode)
```

    Help on module huffpress.huff.HuffNode in huffpress.huff:
    
    NAME
        huffpress.huff.HuffNode - (c) 2021 Usman Ahmad https://github.com/selphaware
    
    DESCRIPTION
        HuffNode.py
        
        Huffman tree class
    
    CLASSES
        builtins.object
            HuffNode
        
        class HuffNode(builtins.object)
         |  HuffNode(term: str, freq: int, left_child=None, right_child=None)
         |  
         |  A class representing a Huffman Binary tree (Huffman node)
         |  
         |  ...
         |  
         |  Attributes
         |  ----------
         |  term : str
         |      ordinal character terms i.e. ascii values delimited by comma
         |  freq : int
         |      total number of occurrences of this term
         |  left_child : HuffNode
         |      left child node / recursive left branch
         |  right_child : HuffNode
         |      right child node / recursive right branch
         |  
         |  Methods
         |  -------
         |  is_leaf():
         |      Returns True if leaf node, otherwise False
         |  
         |  Methods defined here:
         |  
         |  __init__(self, term: str, freq: int, left_child=None, right_child=None)
         |      __init__(self, term: str, freq: int, left_child=None, right_child=None):
         |      
         |      Constructs HuffNode with all necessary attributes
         |      
         |      :param term: (str) ordinal character terms i.e. ascii values
         |                   delimited by comma
         |      :param freq: (int) total number of occurrences of this term
         |      :param left_child: (HuffNode) left child node / recursive left branch
         |      :param right_child: (HuffNode) right child node / recursive right branch
         |  
         |  ----------------------------------------------------------------------
         |  Readonly properties defined here:
         |  
         |  is_leaf
         |      @property
         |      def is_leaf(self) -> bool:
         |      
         |      Checks if current node is a leaf node
         |      
         |      :return: True if leaf, False otherwise
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
    
    FILE
        c:\programdata\anaconda3\lib\site-packages\huffpress\huff\huffnode.py
    
    
    

## Auxiliary functions

### BaseN for converting numbers back-forth to different base numbers


```python
help(huffpress.auxi.basen)
```

    Help on module huffpress.auxi.basen in huffpress.auxi:
    
    NAME
        huffpress.auxi.basen - (c) 2021 Usman Ahmad https://github.com/selphaware
    
    DESCRIPTION
        BaseN.py
        
        Contains numeric functionality converting back-forth decimal to a Base N
        number. e.g. binary, hex, base 5, etc.
    
    CLASSES
        builtins.object
            BaseRange
        
        class BaseRange(builtins.object)
         |  BaseRange class holding the following static consts:
         |  
         |  -- dec: immutable dict --
         |  decimal to base range i.e. {10: A, 11:B, ..., 35: Z} and rest of the
         |  decimal to base range {1: 1, 2:2, ..., 9:9, 10:A, ..., 35: Z}
         |  
         |  -- rev: dict --
         |  
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __annotations__ = {'dec': <class 'huffpress.auxi.idict.IDict'>, 'rev':...
         |  
         |  dec = <huffpress.auxi.idict.IDict object>
         |  
         |  rev = <huffpress.auxi.idict.IDict object>
    
    FUNCTIONS
        basen(in_num, fbase: int = 10, tbase: int = 2, out_str: bool = False)
            converts number in_num from base fbase to base tbase
            see overloads below
            
            :param in_num: number to convert: either str or List[str]
            :param fbase: from base
            :param tbase: to base
            :param out_str: False, out = List[str]. True, out = str
            :return: List[str] value conversion
        
        nmod(x: int, y: int) -> str
            BaseN modulo operator
            
            nmod(10, 16) = "A"
            nmod(10, 2) = "0"
            
            :param x: number
            :param y: modulo
            :return: remainder
        
        to_basen(num: int, base: int = 2) -> List[str]
            to_basen(num: int) -> List[str]:
            
            Convert decimal to base number list
            
            :param base: base number. for binary, base = 2. for hex, base = 16
            :param num: decimal number
            :return: binary list of 1's 0's
        
        to_dec(in_bin: List[str], base: int = 2) -> int
            to_dec(in_bin: List[str]) -> int:
            
            Convert base number list to decimal integer
            
            :param base: base number. for binary, base = 2. for hex, base = 16
            :param in_bin: binary list of 1's and 0's
            :return: decimal integer converted from input binary
    
    DATA
        List = typing.List
        Union = typing.Union
    
    FILE
        c:\programdata\anaconda3\lib\site-packages\huffpress\auxi\basen.py
    
    
    

#### BaseN examples converting numbers of any base to any base


```python
from huffpress.auxi.basen import basen
```


```python
help(basen)
```

    Help on function basen in module huffpress.auxi.basen:
    
    basen(in_num, fbase: int = 10, tbase: int = 2, out_str: bool = False)
        converts number in_num from base fbase to base tbase
        see overloads below
        
        :param in_num: number to convert: either str or List[str]
        :param fbase: from base
        :param tbase: to base
        :param out_str: False, out = List[str]. True, out = str
        :return: List[str] value conversion
    
    


```python
# Converting from number of a base to a different base
```


```python
basen("1234", 10, 2)  # converting from base 10 to 2 (binary)
```




    ['1', '0', '0', '1', '1', '0', '1', '0', '0', '1', '0']




```python
basen("1234", 10, 2, True)  # converting from base 10 to 2 (binary) output as one string
```




    '10011010010'




```python
basen("1234", 10, 16, True)  # converting from base 10 to 16 (hex) output as one string
```




    '4D2'




```python
basen("Z", 36, 10, True)  # converting from base 36 to 10 (dec) output as one string
```




    '35'




```python
basen("64FP", 27, 5, True)  # converting from base 27 to 5 output as one string
```




    '12341234'




```python
# Example of compressing a string via base conversions of the ASCII values
```


```python
hello = "Hello world"
hello_ascii = list(map(ord, list(hello)))
hello_ascii
```




    [72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]




```python
hello_ascii_join = ",".join(list(map(str, hello_ascii)))
print(hello_ascii_join)
print(f"Length = {len(hello_ascii_join)}")
```

    72,101,108,108,111,32,119,111,114,108,100
    Length = 41
    


```python
hello_36 = list(map(lambda x: basen(str(x), 10, 36, True), hello_ascii))
hello_36
```




    ['20', '2T', '30', '30', '33', 'W', '3B', '33', '36', '30', '2S']




```python
hello_36_join = ",".join(list(map(str, hello_36)))
print(hello_36_join)
print(f"Length = {len(hello_36_join)}")
```

    20,2T,30,30,33,W,3B,33,36,30,2S
    Length = 31
    

### Compression modes


```python
help(huffpress.auxi.modes)
```

    Help on module huffpress.auxi.modes in huffpress.auxi:
    
    NAME
        huffpress.auxi.modes - (c) 2021 Usman Ahmad https://github.com/selphaware
    
    DESCRIPTION
        modes.py
        
        Contains all modes used in the rest of the codebase (currently we only
        have 1 mode)
    
    CLASSES
        enum.Enum(builtins.object)
            Mode
        
        class Mode(enum.Enum)
         |  Mode(value, names=None, *, module=None, qualname=None, type=None, start=1)
         |  
         |  Compression modes
         |  
         |  0 - Default (File or Raw input data)
         |  1 - File compression only
         |  2 - Raw input data compression only
         |  
         |  Method resolution order:
         |      Mode
         |      enum.Enum
         |      builtins.object
         |  
         |  Data and other attributes defined here:
         |  
         |  DEFAULT = <Mode.DEFAULT: 0>
         |  
         |  FILE = <Mode.FILE: 1>
         |  
         |  RAW = <Mode.RAW: 2>
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from enum.Enum:
         |  
         |  name
         |      The name of the Enum member.
         |  
         |  value
         |      The value of the Enum member.
         |  
         |  ----------------------------------------------------------------------
         |  Readonly properties inherited from enum.EnumMeta:
         |  
         |  __members__
         |      Returns a mapping of member name->value.
         |      
         |      This mapping lists all enum members, including aliases. Note that this
         |      is a read-only view of the internal mapping.
    
    FILE
        c:\programdata\anaconda3\lib\site-packages\huffpress\auxi\modes.py
    
    
    

### Immutable Dictionary class


```python
help(huffpress.auxi.idict)
```

    Help on module huffpress.auxi.idict in huffpress.auxi:
    
    NAME
        huffpress.auxi.idict - (c) 2021 Usman Ahmad https://github.com/selphaware
    
    DESCRIPTION
        idict.py
        
        Immutable dictionary
    
    CLASSES
        collections.abc.Mapping(collections.abc.Collection)
            IDict
        
        class IDict(collections.abc.Mapping)
         |  IDict(immutable: bool = True, *args, **kwargs)
         |  
         |  IDict
         |  
         |  Dynamic Immutable/Mutable dictionary class,
         |  can be used as a normal dictionary but can be __immutable or mutable
         |  set in the constructor.
         |  
         |  Method resolution order:
         |      IDict
         |      collections.abc.Mapping
         |      collections.abc.Collection
         |      collections.abc.Sized
         |      collections.abc.Iterable
         |      collections.abc.Container
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __getitem__(self, key)
         |      gets item from index key
         |      
         |      :param key: index key
         |      :return: value from dictionary as per key
         |  
         |  __hash__(self)
         |      updates and returns hash value of all items in the dictionary
         |      
         |      :return:
         |  
         |  __init__(self, immutable: bool = True, *args, **kwargs)
         |      sets the input dictionary passed through and makes it __immutable or
         |      mutable based on the input param '__immutable' (True/False)
         |      
         |      :param immutable: set to True to make this dict __immutable, ow. is mutable
         |      :param args: input args
         |      :param kwargs: input dict args
         |  
         |  __iter__(self)
         |      returns iterable object of dictionary
         |      
         |      :return:
         |  
         |  __len__(self)
         |      returns length of dictionary
         |      
         |      :return:
         |  
         |  __setitem__(self, key, value)
         |      sets items in dictionary if dictionary is mutable
         |      checks self.__immutable (bool)
         |      
         |      :param key: key index to set
         |      :param value: value to set
         |      :return:
         |  
         |  ----------------------------------------------------------------------
         |  Readonly properties defined here:
         |  
         |  is_immutable
         |      returns True if this dict obj is immutable, otherwise false
         |      :return: looks at self.__immutable, set in the constructor
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __abstractmethods__ = frozenset()
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from collections.abc.Mapping:
         |  
         |  __contains__(self, key)
         |  
         |  __eq__(self, other)
         |      Return self==value.
         |  
         |  get(self, key, default=None)
         |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
         |  
         |  items(self)
         |      D.items() -> a set-like object providing a view on D's items
         |  
         |  keys(self)
         |      D.keys() -> a set-like object providing a view on D's keys
         |  
         |  values(self)
         |      D.values() -> an object providing a view on D's values
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes inherited from collections.abc.Mapping:
         |  
         |  __reversed__ = None
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from collections.abc.Collection:
         |  
         |  __subclasshook__(C) from abc.ABCMeta
         |      Abstract classes can override this to customize issubclass().
         |      
         |      This is invoked early on by abc.ABCMeta.__subclasscheck__().
         |      It should return True, False or NotImplemented.  If it returns
         |      NotImplemented, the normal algorithm is used.  Otherwise, it
         |      overrides the normal algorithm (and the outcome is cached).
    
    DATA
        __warningregistry__ = {'version': 7}
    
    FILE
        c:\programdata\anaconda3\lib\site-packages\huffpress\auxi\idict.py
    
    
    


```python
from huffpress.auxi.idict import IDict
```


```python
# Immutable normal dictionary (same as dict but immutable)
idict = IDict(True, {1: 2, "a": 3, "a-b": "hello", 2: 1.89})
idict.__immutable = False  # this will not be possible
print(f"\nDict is immutable: {idict.is_immutable}")
correct_error = False
try:
    idict["yes"] = 1
except TypeError as err:
    print(f"\nCorrect error: {err}")
    correct_error = True
print("\nCorrect error: ", correct_error)
print("Dictionaries contain same unchanged items as before: ",
      idict == {1: 2, "a": 3, "a-b": "hello", 2: 1.89})
```

    
    Dict is immutable: True
    
    Correct error: object is __immutable (set to False), cannot set assignment in this object.
    
    Correct error:  True
    Dictionaries contain same unchanged items as before:  True
    


```python
# Mutable normal dictionary (same as normal Python dict)
idict = IDict(False, {1: 2, "a": 3, "a-b": "hello", 2: 1.89})
idict.__immutable = True  # this will not be possible
print(f"\nDict is immutable: {idict.is_immutable}")
idict["yes"] = 1
idict[3] = ["9.99", 8]
idict["a-b"] = "goodbye"
print("Dictionaries contain added and changed items: ", 
      idict == {1:2, "a": 3, "a-b": "goodbye", 2: 1.89, "yes": 1, 3: ["9.99", 8]})
```

    
    Dict is immutable: False
    Dictionaries contain added and changed items:  True
    

# Further examples and documentation

## Going through the Huffman encoding compression step-by-step


```python
from huffpress.press.compress import *
from huffpress.press.decompress import *
```


```python
from huffpress.huff.hfunctions import *
from huffpress.huff.htypes import *
from huffpress.huff.HuffNode import *
```


```python
text = "Hello World"
```


```python
encod_seq: HuffCode
huff_tree: Optional[HuffNode]
```


```python
input_data = InputData(data=str.encode(text))
input_data
```




    InputData(data=b'Hello World')




```python
help(calc_term_freq)
```

    Help on function calc_term_freq in module huffpress.huff.hfunctions:
    
    calc_term_freq(data: huffpress.huff.htypes.InputData) -> huffpress.huff.htypes.TermFreq
        Returns dictionary of frequency occurrence counts for each character
        of a given string
        
        e.g. "ABBcCC" --> { "A": 1, "B": 2, "c": 1, "C": 2 }
        
        :param data: input string text
        :return: dictionary of character frequency occurrence counts
    
    


```python
term_freq: TermFreq = calc_term_freq(input_data)
term_freq
```




    TermFreq(tf={72: 1, 101: 1, 108: 3, 111: 2, 32: 1, 87: 1, 114: 1, 100: 1})




```python
help(build_leaves)
```

    Help on function build_leaves in module huffpress.huff.hfunctions:
    
    build_leaves(term_freq: huffpress.huff.htypes.TermFreq, verbose: bool = False) -> huffpress.huff.htypes.Leaves
        Builds initial leaf HuffNode's from a given dictionary of character
        frequency occurrence counts
        
        :param term_freq: dictionary of frequency occurrence counts of a given
        string computed by calc_term_freq function
        :param verbose: set to True for printing console outputs
        :return: dictionary of leaf HuffNode's for a given character frequency
        count dictionary
    
    


```python
leaves: Leaves = build_leaves(term_freq, verbose=True)
for x in leaves.data.items():
    print(x)
```

    Building leaves
    

    100%|████████████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:00<?, ?it/s]

    (72, HuffTerm(freq=1, node=<huffpress.huff.HuffNode.HuffNode object at 0x000001793A056CD0>))
    (101, HuffTerm(freq=1, node=<huffpress.huff.HuffNode.HuffNode object at 0x000001793A056B50>))
    (108, HuffTerm(freq=3, node=<huffpress.huff.HuffNode.HuffNode object at 0x000001793A058A90>))
    (111, HuffTerm(freq=2, node=<huffpress.huff.HuffNode.HuffNode object at 0x000001793A0584C0>))
    (32, HuffTerm(freq=1, node=<huffpress.huff.HuffNode.HuffNode object at 0x000001793A058B20>))
    (87, HuffTerm(freq=1, node=<huffpress.huff.HuffNode.HuffNode object at 0x000001793A058BE0>))
    (114, HuffTerm(freq=1, node=<huffpress.huff.HuffNode.HuffNode object at 0x000001793A058CA0>))
    (100, HuffTerm(freq=1, node=<huffpress.huff.HuffNode.HuffNode object at 0x000001793A058D60>))
    

    
    


```python
help(sort_tree)
```

    Help on function sort_tree in module huffpress.huff.hfunctions:
    
    sort_tree(tree: huffpress.huff.htypes.Leaves, verbose: bool = False) -> huffpress.huff.htypes.SortedTree
        Sorts a Huffman tree dictionary by total frequency ascending order
        returning a list
        
        e.g.
        
        { "D": (4, HuffNode), "E": (3, HuffNode),
          "F": (7, HuffNode), "ABC": (2, HuffNode) }
        
        -->
        
        [ ("ABC", (2, HuffNode)), ("E", (3, HuffNode)),
          ("D", (4, HuffNode)), ("F", (7, HuffNode)) ]
        
        :param tree: dictionary of HuffNode's { term : (total-frequency, HuffNode) }
        :param verbose: set to True for printing console outputs
        :return: sorted dictionary of HuffNode's converted to a list
    
    


```python
sleaves: SortedTree = sort_tree(leaves)
for x in sleaves.data:
    print(x)
```

    HuffSeq(seq_term=72, huff_term=HuffTerm(freq=1, node=<huffpress.huff.HuffNode.HuffNode object at 0x000001793A056CD0>))
    HuffSeq(seq_term=101, huff_term=HuffTerm(freq=1, node=<huffpress.huff.HuffNode.HuffNode object at 0x000001793A056B50>))
    HuffSeq(seq_term=32, huff_term=HuffTerm(freq=1, node=<huffpress.huff.HuffNode.HuffNode object at 0x000001793A058B20>))
    HuffSeq(seq_term=87, huff_term=HuffTerm(freq=1, node=<huffpress.huff.HuffNode.HuffNode object at 0x000001793A058BE0>))
    HuffSeq(seq_term=114, huff_term=HuffTerm(freq=1, node=<huffpress.huff.HuffNode.HuffNode object at 0x000001793A058CA0>))
    HuffSeq(seq_term=100, huff_term=HuffTerm(freq=1, node=<huffpress.huff.HuffNode.HuffNode object at 0x000001793A058D60>))
    HuffSeq(seq_term=111, huff_term=HuffTerm(freq=2, node=<huffpress.huff.HuffNode.HuffNode object at 0x000001793A0584C0>))
    HuffSeq(seq_term=108, huff_term=HuffTerm(freq=3, node=<huffpress.huff.HuffNode.HuffNode object at 0x000001793A058A90>))
    


```python
help(build_tree)
```

    Help on function build_tree in module huffpress.huff.hfunctions:
    
    build_tree(sorted_new_tree: huffpress.huff.htypes.SortedTree, verbose: bool = False) -> Union[huffpress.huff.HuffNode.HuffNode, NoneType]
        Builds Huffman tree made out of HuffNode's, constructed from initial
        HuffNode leaves
        
        :param sorted_new_tree: sorted [ term, (total-frequency, HuffNode) ]
        :param verbose: set to True for printing console outputs
        :return: Built Huffman tree from initial asc sorted  list of leaves
                 HuffNode's computed by build_leaves function and sorted by
                 sort_tree function
    
    


```python
help(print_node)
```

    Help on function print_node in module huffpress.huff.hfunctions:
    
    print_node(node: Union[huffpress.huff.HuffNode.HuffNode, NoneType], depth: int = 0, verbose: bool = True) -> str
        Recursive printing of the HuffNode tree showing all branches, leaves and
        their terms and total-frequencies
        
        :param node: HuffNode tree i.e. Huffman tree
        :param depth: How many whitespaces to print to represent depth level
                     (starting at depth 0)
        :param verbose: set to True to print to console, False to return string
                        output
        :return: None (prints Huffman tree to console)
    
    


```python
huff_tree: Optional[HuffNode] = build_tree(sleaves, verbose=True)
print_node(huff_tree)
```

    Building Huffman tree
    

    100%|████████████████████████████████████████████████████████████████████████████████████████████| 7/7 [00:00<?, ?it/s]

    |--o--o--o--[3> Term: 32, Freq: 1
    
    |--o--o--o--[3> Term: 87, Freq: 1
    
    |--o--o--[2> Term: 32,87, Freq: 2
    |
    |----Left child:
    |
    |----Right child:
    
    |--o--o--o--[3> Term: 114, Freq: 1
    
    |--o--o--o--[3> Term: 100, Freq: 1
    
    |--o--o--[2> Term: 114,100, Freq: 2
    |
    |----Left child:
    |
    |----Right child:
    
    |--o--[1> Term: 32,87,114,100, Freq: 4
    |
    |--Left child:
    |
    |--Right child:
    
    |--o--o--[2> Term: 108, Freq: 3
    
    |--o--o--o--[3> Term: 111, Freq: 2
    
    |--o--o--o--o--[4> Term: 72, Freq: 1
    
    |--o--o--o--o--[4> Term: 101, Freq: 1
    
    |--o--o--o--[3> Term: 72,101, Freq: 2
    |
    |------Left child:
    |
    |------Right child:
    
    |--o--o--[2> Term: 111,72,101, Freq: 4
    |
    |----Left child:
    |
    |----Right child:
    
    |--o--[1> Term: 108,111,72,101, Freq: 7
    |
    |--Left child:
    |
    |--Right child:
    
    
    Term: 32,87,114,100,108,111,72,101, Freq: 11
    |
    Left child:
    |
    Right child:
    
    

    
    




    ''




```python
encod_seq: HuffCode = encode(leaves, tree=huff_tree, verbose=True)
encod_seq
```

    Encoding tree
    

    100%|██████████████████████████████████████████████████████████████████████████████████| 8/8 [00:00<00:00, 8305.55it/s]
    




    HuffCode(data={72: '1110', 101: '1111', 108: '10', 111: '110', 32: '000', 87: '001', 114: '010', 100: '011'})




```python
huff_seq: Tuple[int, str] = create_huff_sequence(encod_seq, input_data, verbose=True)
huff_seq
```

    100%|██████████████████████████████████████████████████████████████████████████████████████████| 11/11 [00:00<?, ?it/s]
    




    (8, '1110111110101100000011100101001100000000')




```python
final_seq: str = create_final_sequence(huff_seq, verbose=True)
final_seq
```

    Generating final sequence
    




    '000010001110111110101100000011100101001100000000'




```python
seq_bins: List[str] = create_seq_bins(final_seq, verbose=True)
final_res: bytearray = compress_seq_bins(seq_bins, verbose=True)
final_res
```

    100%|████████████████████████████████████████████████████████████████████████████████████████████| 6/6 [00:00<?, ?it/s]
    100%|██████████████████████████████████████████████████████████████████████████████████| 6/6 [00:00<00:00, 6014.78it/s]
    




    bytearray(b'\x08\xef\xac\x0eS\x00')




```python
f"RESULT = {len(input_data.data) - len(final_res)}, FINAL: {len(final_res)}, ORIGINAL: {len(input_data.data)}"
```




    'RESULT = 5, FINAL: 6, ORIGINAL: 11'




```python
app_res = add_huff_map(final_res, encod_seq)
app_res
```




    bytearray(b'\x08\xef\xac\x0eS\x00{"72":"U","101":"V","108":"6","111":"E","32":"8","87":"9","114":"A","100":"B"}26')




```python
f"RESULT = {len(input_data.data) - len(app_res)}, FINAL: {len(app_res)}, ORIGINAL: {len(input_data.data)}"
```




    'RESULT = -75, FINAL: 86, ORIGINAL: 11'


