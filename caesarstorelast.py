import sys
import os
if "CaesarStore" not in os.listdir():
    os.mkdir("CaesarStore")
with open("CaesarStore/caesarstorelast.txt","a+") as f:
    f.write("{}\n".format(sys.argv[1]))