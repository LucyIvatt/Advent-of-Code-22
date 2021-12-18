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
        string = "\n   " * self.depth + self.__class__.__name__ + "{" + "Version: " + str(self.ver) + ", Type ID: " + str(
            self.type_id) + ", Type: " + str(self.type) + "Contents: "
        if self.type == PACKET_TYPE.literal:
            string += str(self.contents) + "}"
        return string

    def print_children(self):
        print(self)
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
        if (i + VER_LEN + ID_LEN) >= length:
            if(len(packets) == 1):
                return packets[0]
            else:
                return packets

        # Header parses
        ver = int(binary_string[i:i+VER_LEN], 2)
        type_id = int(binary_string[i + ID_INDEX: i+ID_INDEX+ID_LEN], 2)
        type = PACKET_TYPE.literal if type_id == LIT_ID else PACKET_TYPE.operator
        end_bit = None

        # Contents parse for literal packets
        if type == PACKET_TYPE.literal:
            data_bits = ""
            start_bit = i + ID_INDEX + ID_LEN
            last_packet = False
            while not last_packet:
                data_bits += binary_string[start_bit+1:start_bit+LIT_GRP_LEN]
                # If final group
                if binary_string[start_bit] == "0":
                    last_packet = True
                    end_bit = start_bit+LIT_GRP_LEN
                    value = int(data_bits, 2)
                    packets.append(Packet(ver, type_id, type, value, depth))

                else:
                    start_bit += LIT_GRP_LEN
            i = end_bit
        # Contents parse for operator packets
        else:
            start_bit = ID_INDEX + ID_LEN

            if binary_string[start_bit] == "0":
                start_bit += 1
                len_subpackets = int(
                    binary_string[start_bit:start_bit+OPR_LT_ID_0], 2)
                start_bit += OPR_LT_ID_0
                # recursive
                sub_packets = parse_packets(
                    binary_string[start_bit:], len_subpackets, maxsize, depth + 1)
                packets.append(
                    Packet(ver, type_id, type, sub_packets, depth))

            else:
                start_bit += 1
                num_sub_packets = int(
                    binary_string[start_bit:start_bit + OPR_LT_ID_1], 2)
                start_bit += OPR_LT_ID_1
                sub_packets = parse_packets(binary_string[start_bit:], len(
                    binary_string[start_bit:]), num_sub_packets, depth + 1)
                packets.append(
                    Packet(ver, type_id, type, sub_packets, depth))
            i = len(binary_string) - 1
        num_sub_packets -= 1
    return packets


def part_one(binary_string):
    root_packet = parse_packets(binary_string, len(binary_string))
    root_packet.print_children()
    version_num_sums = root_packet.version_num_sums()
    return version_num_sums


binary_string = importList("Day 16 Packet Decoder\input.txt")

print("--------------------------------------")
print("DAY 16: PACKET DECODER")
print("Part One Answer: ", part_one(binary_string))
print("Part Two Answer: ")
print("--------------------------------------")
