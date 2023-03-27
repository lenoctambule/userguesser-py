from generators import generators
import sys

if "__main__" == __name__ :
    if len(sys.argv) != 3 :
        print("Usage : python3 "+sys.argv[0]+" <first_name> <last_name>")
        exit(-1)

    for f in generators :
        print(f(sys.argv[1], sys.argv[2]))