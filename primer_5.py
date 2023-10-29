#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    fileptr = open("newfile.txt", "x")
    print(fileptr)
    if fileptr:
        print("File created successfully")

    fileptr.close()