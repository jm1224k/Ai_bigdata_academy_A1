import sys
import os

if len(sys.argv) == 3 and os.path.exists(sys.argv[0]) and os.path.exists(sys.argv[1]) and sys.argv[2][-4:] == '.txt':
    f1 = open(sys.argv[1], "r")
    f2 = open(sys.argv[2], "w")

    lines = f1.read()
    f2.write(lines)

    f1.close()
    f2.close()

else:
    print("error!")