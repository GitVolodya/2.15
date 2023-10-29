#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    fileptr = open("file2.txt", "w")

    fileptr.write(
        "Python is the modern day language. It makes things so simple.\n"
        "It is the fastest-growing programing language"
    )

    fileptr.close()
