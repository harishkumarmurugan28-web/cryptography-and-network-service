def pad(data,size):
 if size<=0:raise ValueError("Size must be positive")
 return data+b'\x80'+b'\x00'*((size-(len(data)+1)%size)%size)
text=input("Plaintext: ").encode();size=int(input("Block size in bytes: "))
out=pad(text,size);print("Padded hex:",out.hex());print("Length:",len(out))
print("Always padding, even for aligned messages, makes the padding/end-of-message unambiguous.")
