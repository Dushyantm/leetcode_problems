import sys # For getting Python Version
import random 
import math
import heapq
import os
class Node():
    def __init__(self, freq, data, l = None, r = None):
        # Nothing can be added in class Node
        # Must use Node class.Hacker rank fails without this Node
        self.freq= freq #Note public
        self.data=data #Note public
        self.left = l #Note public
        self.right = r #Note public
        
    # Need comparator method at a minimum to work with heapq
    def __lt__(self, other):
        return self.freq < other.freq
    
    def encode(self, encoding):
        """Return bit encoding in traversal."""
        if self.left is None and self.right is None:
            yield (self.data, encoding)
        else:
            for i in self.left.encode(encoding + '0'):
                yield i
            for i in self.right.encode(encoding + '1'):
                yield i
class Huffman():
    def __init__(self,show = False,f = None):
        ##Change this to the place where you write dot file
        self.base = "./dot_files/"
        #Nothing can be changed or added below
        self._s = None
        self._show = show
        if (f):
            self._f = self.base + f
        self._id = []
        ##YOU CAN ADD YOUR PRIVATE VARIABLE HERE
        
    #############################################
    #  All public functions below
    #  NOTHING CAN BE CHANGED BELOW
    #############################################
    def encode(self, s:'str')->'str':
        self._s = s
        return self._encode()

    def decode(self,e:'str')->'str':
        return self._decode(e)


    #############################################
    #  WRITE YOUR CODE BELOW
    #  All private functions below
    #############################################
    
    def _calculate_freq(text):
        freq = {}
        for _ in text:
            if _ in freq:
                freq[_] += 1
            else:
                freq[_] = 1
        return freq
    
    
    def _return_encode_bits(s,encoding):
        bits = ''
        for _ in s:
            if not _ in encoding:
                raise ValueError("'" + _ + "' is not encoded character")
            bits += encoding[_]
        # print("encoded string: " + str(bits))
        return bits
    
    def _traverse_tree(self, node, internal_nodes):
        if node is not None:
            if node.data is None:
                internal_nodes.append(node)
            self._traverse_tree(node.left, internal_nodes)
            self._traverse_tree(node.right, internal_nodes)

    def _encode(self)->'str':
        freq_dict = Huffman._calculate_freq(self._s)
        
        print("-----------Step 1: Character Occurence------------")
        for character, value in freq_dict.items():
            print((character) +' occurs '+ str(value)+" times")
        
        print("-----------Step 2: Tree Leaves are built in this order------------")
        
        for i, (character, value) in enumerate(freq_dict.items(),start =1):
            print("Leaf Node "+ str(i) + " : " + (character)+" "+ str(value))
            
        for symbol in freq_dict:
            self._id.append(Node(freq_dict[symbol], symbol))
        heapq.heapify(self._id)
        
        
        if len(self._id) == 1:
            root = Node(1,None)
            root.left = self._id[0]
            encoding = {symbol: '0'}
            
            return Huffman._return_encode_bits(self._s,encoding)
        
        print("-----------Step 3: Internal nodes of the Tree are built in this order------------")
        node_count = i
        while len(self._id) > 1:
            n1 = heapq.heappop(self._id)
            n2 = heapq.heappop(self._id)
            n3 = Node(n1.freq + n2.freq,None)
            n3.left = n1
            n3.right = n2
            heapq.heappush(self._id, n3)
            node_count += 1
            print(f"Internal Node {node_count:2d}: {n1.data if n1.data is not None else '_'}"
              f"{n2.data if n2.data is not None else '_'} {n3.freq}")

        print(f"Tree has {node_count} nodes")
                
        root = self._id[0]
        encoding = {}
        
        print("-----------Step 4: Code for each character------------")
        for sym,code in self._id[0].encode(''):
            encoding[sym]=code
            print(sym +' code is ' + encoding[sym])
        
        print("-----------Step 5: Encoding------------")
        print("original string: "+ self._s)
        print("encoded string: "+ str(Huffman._return_encode_bits(self._s,encoding)))
        return Huffman._return_encode_bits(self._s,encoding)

        
        

    def _decode(self, e:'str')->'str':
        
        if len(e) == 1:
            node = self._id[0]
            return node.data
        
#         print('Decoding',self._id[0].left.data,self._id[0].right.data)
        node = self._id[0]
        s = ''
        for _ in e:
            if _ == '0':
                node = node.left
            else:
                node = node.right

            if node.data:
                s += node.data
                node = self._id[0]
        print('decoded string: '+s)
        return s
############################################# 
##LEETCODE  
## https://leetcode.com/problems/encode-and-decode-tinyurl/
## Step1: Delete all code and comment in Leetcpde
## Step2: Cut and paste this file in Leetcode
## Step3: Make False to True
## All tests must pass in one shot.
## Post screen shot of Leetcode passed as pdf
#############################################
if (True):
    Codec = Huffman