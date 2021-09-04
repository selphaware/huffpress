# huffpress.huffman package

## Submodules

## huffpress.huffman.HuffNode module


1. 2021 Usman Ahmad [https://github.com/selphaware](https://github.com/selphaware)

HuffNode.py

Huffman tree class


### class huffpress.huffman.HuffNode.HuffNode(term: str, freq: int, left_child=None, right_child=None)
Bases: `object`

A class representing a Huffman Binary tree (Huffman node)

…

term

    ordinal character terms i.e. ascii values delimited by comma

freq

    total number of occurrences of this term

left_child

    left child node / recursive left branch

right_child

    right child node / recursive right branch

is_leaf():

    Returns True if leaf node, otherwise False


#### \__init__(term: str, freq: int, left_child=None, right_child=None)
__init__(self, term: str, freq: int, left_child=None, right_child=None):

Constructs HuffNode with all necessary attributes


* **Parameters**

    
    * **term** – (str) ordinal character terms i.e. ascii values
    delimited by comma


    * **freq** – (int) total number of occurrences of this term


    * **left_child** – (HuffNode) left child node / recursive left branch


    * **right_child** – (HuffNode) right child node / recursive right branch



#### property is_leaf(: bool)
@property
def is_leaf(self) -> bool:

Checks if current node is a leaf node


* **Returns**

    True if leaf, False otherwise


## huffpress.huffman.hfunctions module


1. 2021 Usman Ahmad [https://github.com/selphaware](https://github.com/selphaware)

hfunctions.py

Contains all Huffman building and deconstructing functions


### huffpress.huffman.hfunctions.build_leaves(term_freq: Dict[int, int], verbose: bool = False)
build_leaves(term_freq: TermFreq,

    verbose: bool = False) -> Leaves:

Builds initial leaf HuffNode’s from a given dictionary of character
frequency occurrence counts


* **Parameters**

    **term_freq** – dictionary of frequency occurrence counts of a given


string computed by calc_term_freq function
:param verbose: set to True for printing console outputs
:return: dictionary of leaf HuffNode’s for a given character frequency
count dictionary


### huffpress.huffman.hfunctions.build_tree(sorted_new_tree: List[Tuple[str, Tuple[int, Optional[huffpress.huffman.HuffNode.HuffNode]]]], verbose: bool = False)
build_tree(sorted_new_tree: SortedTree,

    verbose: bool = False) -> Optional[HuffNode]:

Builds Huffman tree made out of HuffNode’s, constructed from initial
HuffNode leaves


* **Parameters**

    
    * **sorted_new_tree** – sorted [ term, (total-frequency, HuffNode) ]


    * **verbose** – set to True for printing console outputs



* **Returns**

    Built Huffman tree from initial asc sorted  list of leaves
    HuffNode’s computed by build_leaves function and sorted by
    sort_tree function



### huffpress.huffman.hfunctions.calc_term_freq(data: InputData)
Returns dictionary of frequency occurrence counts for each character
of a given string

e.g. “ABBcCC” –> { “A”: 1, “B”: 2, “c”: 1, “C”: 2 }


* **Parameters**

    **data** – input string text



* **Returns**

    dictionary of character frequency occurrence counts



### huffpress.huffman.hfunctions.create_huff_tree(data: Union[str, bytes], verbose: bool = False)
create_huff_tree(data: InputData,

    verbose: bool = False) -> Tuple[HuffCode,

        Optional[HuffNode]]:

Method:

    leaves = build_leaves(calc_term_freq(data), verbose=verbose)
    sleaves = sort_tree(leaves)
    huff_tree = build_tree(sleaves, verbose=verbose)
    encod_seq = encode_all(leaves, huff_tree, verbose=verbose)
    return encod_seq, huff_tree

Main function to create Huffman tree from an input data string


* **Parameters**

    
    * **data** – input data string or bytearray to be transformed to a
    Huffman tree


    * **verbose** – set to True to print to console, False to return
    string output



* **Returns**

    tuple of final encoded sequences per term and constructed
    Huffman tree



### huffpress.huffman.hfunctions.encode(single_term: int, tree: Optional[HuffNode], path='')
Encode Huffman tree recursively adding 0’s to left branches, and 1’s to
right branches.

Most frequent occurring terms will be encoded with a shorter sequence.
Least frequent occurring terms will be encoded with a longer sequence


* **Parameters**

    
    * **single_term** – single character term


    * **tree** – HuffNode tree already built by create_huff_tree function


    * **path** – visited nodes collecting 0’s (left side), 1’s (right side)
    along the way



* **Returns**

    dictionary containing a single term as the key, and its continually
    constructed binary sequence (Huffman map)



### huffpress.huffman.hfunctions.encode_all(leaves: Dict[str, Tuple[int, Optional[huffpress.huffman.HuffNode.HuffNode]]], final_tree: Optional[huffpress.huffman.HuffNode.HuffNode], verbose=False)
encode_all(leaves: Leaves, final_tree: Optional[HuffNode],

    verbose=False) -> HuffCode:

Encode all unique character terms, constructing binary sequences from the
Huffman tree


* **Parameters**

    
    * **leaves** – initial list of leaves with unique character terms


    * **final_tree** – constructed Huffman tree computed by create_huff_tree
    function


    * **verbose** – set to True to print to console, False to return string
    output



* **Returns**

    dictionary of all terms as keys, and their encoded binary sequence



### huffpress.huffman.hfunctions.print_node(node: HuffNode, depth: int = 0, verbose: bool = True)
Recursive printing of the HuffNode tree showing all branches, leaves and
their terms and total-frequencies


* **Parameters**

    
    * **node** – HuffNode tree i.e. Huffman tree


    * **depth** – How many whitespaces to print to represent depth level
    (starting at depth 0)


    * **verbose** – set to True to print to console, False to return string
    output



* **Returns**

    None (prints Huffman tree to console)



### huffpress.huffman.hfunctions.sort_tree(tree: dict, verbose: bool = False)
Sorts a Huffman tree dictionary by total frequency ascending order
returning a list

e.g.

{ “D”: (4, HuffNode), “E”: (3, HuffNode),

    “F”: (7, HuffNode), “ABC”: (2, HuffNode) }

–>

[ (“ABC”, (2, HuffNode)), (“E”, (3, HuffNode)),

    (“D”, (4, HuffNode)), (“F”, (7, HuffNode)) ]


* **Parameters**

    
    * **tree** – dictionary of HuffNode’s { term : (total-frequency, HuffNode) }


    * **verbose** – set to True for printing console outputs



* **Returns**

    sorted dictionary of HuffNode’s converted to a list


## huffpress.huffman.htypes module


1. 2021 Usman Ahmad [https://github.com/selphaware](https://github.com/selphaware)

htypes.py

Contains all Huffman Data Structure Types:


---

CompData = Union[str, bytearray]

Data to be compressed will either be the filename (str) or compressed data
(bytearray)


---

InputData = Union[str, bytes]

Input data to be compressed will either be a string or sequence of bytes
string e.g. “Hello”
bytes e.g. b”ABC” or [65, 66, 67]


---

TermFreq = Dict[str, int]

When calculating collections.Counter on a input string or bytes,
we return a dictionary of key being the ordinal ASCII value, and
the value being the frequency of occurrence in the input data.


---

HuffTerm = Tuple[int, Optional[HuffNode]]

For a single Huffman Node we have a tuple of total number of frequency
occurrences, and we have the node (which can be null)


---

Leaves = Dict[str, HuffTerm]

Initial set of leaves set as a dictionary of keys as the term made up of
comma delimited ordinal ASCII values, and the value as the HuffTerm.


---

SortedTree = List[Tuple[str, HuffTerm]]

Huffman tree structure, which is a list of tuples of the term made up of
comma delimited ordinal ASCII values, and the HuffTerm. The list is sorted
by the total number of frequency order in ascending order.


---

HuffTuple = Tuple[str, int, Optional[HuffNode]]

Similar structure to SortedTree where we have a tuple of string term,
total frequency, and the HuffNode (which could be null)


---

HuffCode = Dict[int, str]

Final encoded Huffman encoded sequences with key as the ordinal ASCII value
and the value as the binary sequence string

## Module contents
# huffpress package

## Subpackages


* huffpress.huffman package


    * Submodules


    * huffpress.huffman.HuffNode module


    * huffpress.huffman.hfunctions module


    * huffpress.huffman.htypes module


    * Module contents


## Submodules

## huffpress.compress module


1. 2021 Usman Ahmad [https://github.com/selphaware](https://github.com/selphaware)

compress.py

Contains all compression functions using the Huffman encoding algorithm to
encode most frequently occurring terms with short binary sequences,
and encoding least frequently occurring terms with longer binary sequences.

### Process:

1) Input String -> 2) ASCII ordinal values -> 3) Huffman Encoding
-> 4) Replace characters with Encodings -> NOTE: Most frequent characters
will have shorter encodings than Least frequent characters. The idea is
there will be numerous frequent characters, which can be replaced by a short
binary encoding - and so when we 5) Pack binaries into buckets of
length 8 -> we combine 2 or more characters into a single 8-bit byte,
and hence 6) Convert the binaries of length 8 to decimal and 7) The decimals
are ASCII ordinal values which can be converted to characters
(ASCII values between 1 and 255).


### huffpress.compress.add_huff_map(final_seq: bytearray, huff_map: HuffCode)
Concatenate the final generated Huffman sequence with the Huffman map,
which is required for decoding the Huffman sequence.


* **Parameters**

    
    * **final_seq** – final compressed Huffman sequence binaries computed by
    compress_seq_bins function


    * **huff_map** – Huffman map containing terms and their encoding



* **Returns**

    concatenated final_seq + huff_map in a bytearray sequence



### huffpress.compress.compress(inp: str, verbose: bool = False, mode: huffpress.generic.Mode = <Mode.DEFAULT: 0>)
compress(inp: str, verbose: bool = False,

    mode: Mode = Mode.DEFAULT) -> CompData:

Generic compression function taking in input either filename or
string to compress.


* **Parameters**

    
    * **inp** – filename or string text to compress


    * **verbose** – set to True for printing console outputs


    * **mode** – Mode.DEFAULT –> if file exists, compress file, otherwise

        compress string text

    Mode.FILE    –> compress file
    Mode.RAW     –> compress string text




* **Returns**

    if compressed file, return compressed output filename. otherwise,
    return bytearray compressed data



### huffpress.compress.compress_bytes(inp_bytes: bytes, verbose: bool = False)
Compress input data bytes using the Huffman Encoding algorithm.
Function compress_string takes an input string which transforms to bytes,
then calls this function to compress.


* **Parameters**

    
    * **inp_bytes** – input data bytes to be compressed


    * **verbose** – set to True for printing console outputs



* **Returns**

    Final compressed bytearray sequence



### huffpress.compress.compress_file(inp_file: str, verbose: bool = False)
compress_file(inp_file: str, verbose: bool = False):

Compresses the contents of a file and outputs to a file
with extension “.hac”

e.g. some_file.ext — compressed to –> some_file.ext.hac


* **Parameters**

    
    * **inp_file** – input file to compress


    * **verbose** – set to True for printing console outputs



* **Returns**

    name of the compressed output file



### huffpress.compress.compress_seq_bins(final_bins: List[str], verbose: bool = False)
compress_seq_bins(final_bins: List[str],

    verbose: bool = False) -> bytearray:

From a given list of binaries constructed from the final Huffman sequence
i.e. create_seq_bins function, compress the binaries (converting) to an
ASCII ordinal value.


* **Parameters**

    
    * **final_bins** – list of binary sequences construct from the final
    Huffman sequence


    * **verbose** – set to True for printing console outputs



* **Returns**

    bytearray of ascii ordinal values constructed from the Huffman
    sequence of binaries, which collapses 2 or
    more characters into less number of characters for most frequent
    occurring terms in the original raw data



### huffpress.compress.compress_string(inp_st: str, verbose=False)
Compresses input string using the Huffman Encoding algorithm


* **Parameters**

    
    * **inp_st** – input string to be compressed


    * **verbose** – set to True for printing console outputs



* **Returns**

    compressed data in bytearray format



### huffpress.compress.create_final_sequence(huff_seq_rem: Tuple[int, str], verbose: bool = False)
create_final_sequence(huff_seq_rem: Tuple[int, str],

    verbose: bool = False) -> str:

From a given Huffman encoded sequence (computed by create_huff_sequence
function), convert to a binary sequence.


* **Parameters**

    
    * **huff_seq_rem** – tuple of 0:Huffman sequence and 1:remainder length
    (to be used for ‘0’ padding)


    * **verbose** – set to True for printing console outputs



* **Returns**

    final Huffman sequence converted to a binary sequence



### huffpress.compress.create_huff_sequence(huff: Dict[int, str], inp_data: Union[str, bytes], verbose: bool = False)
create_huff_sequence(huff: HuffCode, inp_data: InputData,

    verbose: bool = False) -> Tuple[int, str]:

Creates an encoded Huffman sequence from a given Huffman tree dictionary
and input data string text.


* **Parameters**

    
    * **huff** – Huffman tree dictionary (encoded sequences per term)
    computed by hfunctions.create_huff_tree


    * **inp_data** – input data string text to be encoded


    * **verbose** – set to True for printing console outputs



* **Returns**

    (number of 0 paddings required, new encoded sequence)



### huffpress.compress.create_seq_bins(final_seq: str, verbose: bool = False)
From a given final Huffman sequence (computed by create_final_sequence
function) extract the sequence of binaries of length 8 and store in a list


* **Parameters**

    
    * **final_seq** – Final Huffman sequence string of binaries


    * **verbose** – set to True for printing console outputs



* **Returns**

    

## huffpress.decompress module


1. 2021 Usman Ahmad [https://github.com/selphaware](https://github.com/selphaware)

decompress.py

Contains all decompression functions by first extracting the Huffman map
from the input data and using the map to convert back the compressed
characters to the original characters.


### huffpress.decompress.decompress(inp: Union[str, bytearray], outfile: Optional[str] = None, verbose=False)
decompress(inp: CompData, outfile: Optional[str] = None, verbose=False):

Decompress bytearray data or contents of a file


* **Parameters**

    
    * **inp** – either bytearray compressed data or the filename containing the
    data


    * **outfile** – name of the output file name (optional)


    * **verbose** – set to True for printing console outputs



* **Returns**

    either decompressed bytearray data or name of decompressed output
    file



### huffpress.decompress.decompress_bytes(inp_bytes: bytes, verbose=False)
Main function to decompress input bytes by extracting the Huffman map
and using the map to replace the encoded sequences with the original
characters.


* **Parameters**

    
    * **inp_bytes** – Input data to be compressed


    * **verbose** – set to True for printing console outputs



* **Returns**

    decompressed bytearray data



### huffpress.decompress.decompress_file(inp_file: str, outfile: Optional[str] = None, verbose=False)
decompress_file(inp_file: str, outfile: Optional[str] = None,

    verbose=False):

Decompress file


* **Parameters**

    
    * **inp_file** – File to be decompressed


    * **outfile** – Output file for decompressed contents to be saved


    * **verbose** – set to True for printing console outputs



* **Returns**

    name and path of the output file



### huffpress.decompress.extract_huff_map(inp_bytes: bytes, verbose: bool = False)
extract_huff_map(inp_bytes: bytes,

    verbose: bool = False) -> Tuple[HuffCode, int]:

Extract Huffman encoding dictionary map from the input data.


* **Parameters**

    
    * **inp_bytes** – input sequence of bytes containing compressed data
    and Huffman map


    * **verbose** – set to True for printing console outputs



* **Returns**

    Huffmann map dictionary and the length of the map



### huffpress.decompress.reverse_final_sequence(bstr: bytearray, verbose: bool = False)
Convert the input (already compressed sequence) of ascii ordinal values to
a binary sequence string, which is the encoded Huffman sequence


* **Parameters**

    
    * **bstr** – input sequence of ascii ordinal values (compressed data
    bytearray format)


    * **verbose** – set to True for printing console outputs



* **Returns**

    binary string of compressed data (Huffman encoded sequence
    of 0’s and 1’s)



### huffpress.decompress.reverse_huff_sequence(huff: Dict[int, str], seq: str, verbose: bool = False)
reverse_huff_sequence(huff: HuffCode, seq: str,

    verbose: bool = False) -> bytearray:

Reverse the input binary string Huffman encoded sequence –> back to the
original characters. This is done by traversing through the sequence in
order and identifying any of the Huffman encoded sequence from the
given (huff) Huffman map. Since all encodings are unique at any length,
we can replace in this forward travelling manner.


* **Parameters**

    
    * **huff** – Huffman map containing the binary encodings to original
    character


    * **seq** – input binary string of Huffman encoded sequence


    * **verbose** – set to True for printing console outputs



* **Returns**

    

## huffpress.decorators module


1. 2021 Usman Ahmad [https://github.com/selphaware](https://github.com/selphaware)

decorators.py

Contains decorators for compressing and decompressing variable objects

e.g.

# Function below with @comp decorator returns the compressed
# byterray of “Hello world”
@comp
def some_fn():

> return “Hello world”

# Function below decompresses contents of var2 first before proceeding
# with the rest of the function
@decomp(“var2”)
def some_fn2(var1, var2):

> …


### huffpress.decorators.comp(fun)
Compression decorator, which compresses final string result


* **Parameters**

    **fun** – Function to be decorated



* **Returns**

    decorator function



### huffpress.decorators.decomp(\*bytearray_vars)
Decompression decorator, which first decompresses given bytearray variable
objects before proceeding with the rest of the function


* **Parameters**

    **bytearray_vars** – Bytearray variables to decompress first



* **Returns**

    decorator function


## huffpress.generic module


1. 2021 Usman Ahmad [https://github.com/selphaware](https://github.com/selphaware)

generic.py

Contains generic functionality (converting decimal <-> binary), and the
compression modes


### class huffpress.generic.Mode(value)
Bases: `enum.Enum`

Compression modes

0 - Default (File or Raw input data)
1 - File compression only
2 - Raw input data compression only


#### DEFAULT( = 0)

#### FILE( = 1)

#### RAW( = 2)

### huffpress.generic.bin_to_dec(in_bin: List[int])
Convert binary list to decimal integer


* **Parameters**

    **in_bin** – binary list of 1’s and 0’s



* **Returns**

    decimal integer converted from input binary



### huffpress.generic.dec_to_bin(num: int)
Convert decimal to binary list


* **Parameters**

    **num** – decimal number



* **Returns**

    binary list of 1’s 0’s


## Module contents
<!-- src documentation master file, created by
sphinx-quickstart on Sat Sep  4 23:52:27 2021.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# Welcome to src’s documentation!

# Contents:


* huffpress package


    * Subpackages


        * huffpress.huffman package


            * Submodules


            * huffpress.huffman.HuffNode module


            * huffpress.huffman.hfunctions module


            * huffpress.huffman.htypes module


            * Module contents


    * Submodules


    * huffpress.compress module


        * Process:


    * huffpress.decompress module


    * huffpress.decorators module


    * huffpress.generic module


    * Module contents


# Indices and tables


* Index


* Module Index


* Search Page
