from top3 import *
from new1 import *
from shutil import rmtree

def main():

    main_top3()
    main_new1()

    if "./src/__pycache__":
        rmtree("./src/__pycache__")

main()