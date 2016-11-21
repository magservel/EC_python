#
#
#
#

import os

class Data:
    def __init__(self, path):
        self.parser(path)
        self.print_data()

    def parser(self, path):
        with open(path, "r") as data_file:
            line = data_file.readline().split("=")
            self.p = int(line[1])
            line = data_file.readline().split("=")
            self.n = int(line[1])
            line = data_file.readline().split("=")
            self.a4 = int(line[1])
            line = data_file.readline().split("=")
            self.a6 = int(line[1])
            line = data_file.readline().split("=")
            self.r4 = int(line[1])
            line = data_file.readline().split("=")
            self.r6 = int(line[1])
            line = data_file.readline().split("=")
            self.gx = int(line[1])
            line = data_file.readline().split("=")
            self.gy = int(line[1])
            line = data_file.readline().split("=")
            self.r = int(line[1])

    def print_data(self):
        print "p  = ", self.p
        print "n  = ", self.n
        print "a4 = ", self.a4
        print "a6 = ", self.a6
        print "r4 = ", self.r4
        print "r6 = ", self.r6
        print "gx = ", self.gx
        print "gy = ", self.gy
        print "r  = ", self.r


