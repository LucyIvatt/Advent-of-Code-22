from enum import Enum
from sys import maxsize
import time

HEX_TO_BITS = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110",
               "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}
# Constants & Enums
VER_IND, VER_LEN = 0, 3
ID_INDEX, ID_LEN, LIT_ID = 3, 3, 4
LIT_GRP_LEN = 5
OPR_LT_ID_0, OPR_LT_ID_1 = 15, 11
PACKET_TYPE = Enum("PACKET_TYPE", "literal, operator")


class Packet():
    def __init__(self, ver, type_id, type, contents, depth):
        self.ver = int(ver)
        self.type_id = int(type_id)
        self.type = type
        self.contents = contents
        self.depth = depth

    def __str__(self):
        string = self.__class__.__name__ + "{" + "Version: " + str(self.ver) + ", Type ID: " + str(
            self.type_id) + ", Type: " + str(self.type) + " Depth: " + str(self.depth) + " Contents: "
        if not isinstance(self.contents, list):
            string += str(self.contents)
        else:
            string += "\n"
            for packet in self.contents:
                string += ("   " * (self.depth + 1)) + str(packet) + "\n"
        return string

    def value(self):
        if self.type == PACKET_TYPE.literal:
            return self.contents

        elif isinstance(self.contents, Packet):
            return self.contents.value()

        else:
            if self.type_id == 0:
                sum = 0
                for packet in self.contents:
                    sum += packet.value()
                return sum

            elif self.type_id == 1:
                prod = 1
                for packet in self.contents:
                    prod *= packet.value()
                return prod

            elif self.type_id == 2:
                return min([packet.value() for packet in self.contents])

            elif self.type_id == 3:
                return max([packet.value() for packet in self.contents])

            elif self.type_id == 5:
                return 1 if (self.contents[0].value() > self.contents[1].value()) else 0

            elif self.type_id == 6:
                return 1 if (self.contents[0].value() < self.contents[1].value()) else 0

            elif self.type_id == 7:
                return 1 if (self.contents[0].value() == self.contents[1].value()) else 0

    def print_children(self):
        print(self.contents)
        for child in self.contents:
            print("   " * self.depth + str(child))

    def version_num_sums(self):
        total = self.ver
        if self.type == PACKET_TYPE.operator:
            for sub_packet in self.contents:
                total += sub_packet.version_num_sums()
        return total


def importList(filename):
    with open(filename, "r") as file:
        hex_string = file.readline()
    binary_string = ""
    for char in hex_string:
        binary_string += HEX_TO_BITS[char]
    return binary_string


def parse_packets(binary_string, length, num_sub_packets=maxsize, depth=0):
    packets = []
    i = 0
    while num_sub_packets > 0 and i < length:
        if (i + 7) >= length:
            return i, packets

        ver = int(binary_string[i:i+VER_LEN], 2)
        type_id = int(binary_string[i + ID_INDEX: i+ID_INDEX+ID_LEN], 2)
        type = PACKET_TYPE.literal if type_id == LIT_ID else PACKET_TYPE.operator
        i += VER_LEN + ID_LEN

        # Contents parse for literal packets
        if type == PACKET_TYPE.literal:
            data_bits = ""
            last_packet = False
            while not last_packet:
                data_bits += binary_string[i+1:i+LIT_GRP_LEN]
                # If final group
                if binary_string[i] == "0":
                    last_packet = True
                    value = int(data_bits, 2)
                    packets.append(
                        Packet(ver, type_id, type, int(value), depth))
                i += LIT_GRP_LEN

        # Contents parse for operator packets
        else:
            if binary_string[i] == "0":
                i += 1
                len_subpackets = int(
                    binary_string[i:i+OPR_LT_ID_0], 2)
                i += OPR_LT_ID_0
                # recursive
                end_index, sub_packets = parse_packets(
                    binary_string[i:], len_subpackets, maxsize, depth + 1)
                packets.append(
                    Packet(ver, type_id, type, sub_packets, depth))
                i += end_index

            else:
                i += 1
                new_sub_packets = int(
                    binary_string[i:i + OPR_LT_ID_1], 2)
                i += OPR_LT_ID_1
                end_index, sub_packets = parse_packets(binary_string[i:], len(
                    binary_string[i:]), new_sub_packets, depth + 1)
                packets.append(
                    Packet(ver, type_id, type, sub_packets, depth))
                i += end_index
        num_sub_packets -= 1
    return i, packets


def part_one(binary_string):
    start_time = time.time()
    root_packet = parse_packets(binary_string, len(binary_string))[1][0]
    version_num_sums = root_packet.version_num_sums()
    end_time = time.time()
    return str(version_num_sums) + ", time taken: " + "{:.4f}".format(end_time - start_time) + "s"


def part_two(binary_string):
    start_time = time.time()
    root_packet = parse_packets(binary_string, len(binary_string))[1][0]
    root_packet_value = root_packet.value()
    end_time = time.time()
    return str(root_packet_value) + ", time taken: " + "{:.4f}".format(end_time - start_time) + "s"


binary_string = importList("Day 16 Packet Decoder\input.txt")

print("--------------------------------------")
print("DAY 16: PACKET DECODER")
print("Part One Answer: ", part_one(binary_string))
print("Part Two Answer: ", part_two(binary_string))
print("--------------------------------------")
