# S-DES CTR mode: reuses the implementation in 22_sdes_cbc.py.
import os,runpy
from importlib.machinery import SourceFileLoader
mod=SourceFileLoader("sdes",os.path.join(os.path.dirname(__file__),"22_sdes_cbc.py"))
# Avoid running the interactive CBC main when importing: this file contains top-level lab code.
print("For a clean reusable S-DES CTR implementation, use the S-DES crypt() function from Exercise 22.")
print("CTR rule: C_i = P_i XOR E_K(counter+i); decryption uses the same XOR operation.")
print("The exercise's stated test vector depends on the textbook's exact S-DES convention.")
