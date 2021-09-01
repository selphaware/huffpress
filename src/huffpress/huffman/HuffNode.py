class HuffNode(object):
    """
    A class representing a Huffman Binary tree

    ...

    Attributes
    ----------
    term : str
        ordinal character terms i.e. ascii values delimited by comma
    freq : int
        total number of occurrences of this term
    left_child : HuffNode
        left child node / recursive left branch
    right_child : HuffNode
        right child node / recursive right branch

    Methods
    -------
    is_leaf():
        Returns True if leaf node, otherwise False
    """
    def __init__(self, term: str, freq: int, left_child=None, right_child=None):
        """
        Constructs HuffNode with all necessary attributes
        :param term: (str) ordinal character terms i.e. ascii values delimited by comma
        :param freq: (int) total number of occurrences of this term
        :param left_child: (HuffNode) left child node / recursive left branch
        :param right_child: (HuffNode) right child node / recursive right branch
        """
        self.term = term
        self.freq = freq
        self.left_child = left_child
        self.right_child = right_child

    @property
    def is_leaf(self):
        """
        checks if current node is a leaf node
        :return: True if leaf, False otherwise
        """
        return (self.left_child is None) and (self.right_child is None)
