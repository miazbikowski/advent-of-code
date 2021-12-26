from collections import namedtuple
from math import prod

TRANSMISSION = "020D708041258C0B4C683E61F674A1401595CC3DE669AC4FB7BEFEE840182CDF033401296F44367F938371802D2CC9801A980021304609C431007239C2C860400F7C36B005E446A44662A2805925FF96CBCE0033C5736D13D9CFCDC001C89BF57505799C0D1802D2639801A900021105A3A43C1007A1EC368A72D86130057401782F25B9054B94B003013EDF34133218A00D4A6F1985624B331FE359C354F7EB64A8524027D4DEB785CA00D540010D8E9132270803F1CA1D416200FDAC01697DCEB43D9DC5F6B7239CCA7557200986C013912598FF0BE4DFCC012C0091E7EFFA6E44123CE74624FBA01001328C01C8FF06E0A9803D1FA3343E3007A1641684C600B47DE009024ED7DD9564ED7DD940C017A00AF26654F76B5C62C65295B1B4ED8C1804DD979E2B13A97029CFCB3F1F96F28CE43318560F8400E2CAA5D80270FA1C90099D3D41BE00DD00010B893132108002131662342D91AFCA6330001073EA2E0054BC098804B5C00CC667B79727FF646267FA9E3971C96E71E8C00D911A9C738EC401A6CBEA33BC09B8015697BB7CD746E4A9FD4BB5613004BC01598EEE96EF755149B9A049D80480230C0041E514A51467D226E692801F049F73287F7AC29CB453E4B1FDE1F624100203368B3670200C46E93D13CAD11A6673B63A42600C00021119E304271006A30C3B844200E45F8A306C8037C9CA6FF850B004A459672B5C4E66A80090CC4F31E1D80193E60068801EC056498012804C58011BEC0414A00EF46005880162006800A3460073007B620070801E801073002B2C0055CEE9BC801DC9F5B913587D2C90600E4D93CE1A4DB51007E7399B066802339EEC65F519CF7632FAB900A45398C4A45B401AB8803506A2E4300004262AC13866401434D984CA4490ACA81CC0FB008B93764F9A8AE4F7ABED6B293330D46B7969998021C9EEF67C97BAC122822017C1C9FA0745B930D9C480"

Packet = namedtuple("Packet", ("version", "type_id", "value", "sub_packets"))

class PacketAnalyzer:

    def __init__(self, hex_packet):
        h_size = len(hex_packet) * 4
        self.bin_packet = ( bin(int(hex_packet, 16))[2:] ).zfill(h_size)

    def version(self, bin_packet, i):
        end_i = i+3
        return int(str(bin_packet)[i:end_i], 2), end_i

    def type_id(self, bin_packet, i):
        end_i = i+3
        return int(str(bin_packet)[i:end_i], 2), end_i

    def length_type_id(self, bin_packet, i):
        end_i = i+1
        return int(str(bin_packet)[i:end_i], 2), end_i

    def length_in_bits(self, bin_packet, i):
        end_i = i+15
        return int(str(bin_packet)[i:end_i], 2), end_i

    def get_sub_packets_by_length(self, bin_packet, length_in_bits, i):
        sub_packets = []
        # length_of_sub_packets = int(bin_packet[i:(i + 15)], 2)
        # i += 15
        length_used = 0
        while length_used < length_in_bits:
            sub_packet, new_i = self.analyze(bin_packet, i)
            sub_packets.append(sub_packet)
            length_used += new_i - i
            i = new_i
        return sub_packets, i

    def get_sub_packets_by_number(self, transmission, i):
        sub_packets = []
        number_of_sub_packets = int(transmission[i:(i + 11)], 2)
        i += 11
        for _ in range(number_of_sub_packets):
            sub_packet, i = self.analyze(transmission, i)
            sub_packets.append(sub_packet)
        return sub_packets, i

    def get_literal_value(self, bin_packet, i):
        value = ""
        while True:
            last_group = bin_packet[i] == "0"
            value += bin_packet[(i + 1):(i + 5)]
            i += 5
            if last_group:
                break
        return int(value, 2), i

    def calculate_value(self, type_id, sub_packets):
        value = 0
        if type_id <= 3:
            values = (sub_packet.value for sub_packet in sub_packets)
            if type_id == 0:
                value = sum(values)
            elif type_id == 1:
                value = prod(values)
            elif type_id == 2:
                value = min(values)
            elif type_id == 3:
                value = max(values)
        else:
            sub_a, sub_b = sub_packets
            if type_id == 5:
                value = sub_a.value > sub_b.value
            elif type_id == 6:
                value = sub_a.value < sub_b.value
            elif type_id == 7:
                value = sub_a.value == sub_b.value
            value = int(value)
        return value

    def sum_versions(self, packet):
        total = packet.version
        for sub_packet in packet.sub_packets:
            total += self.sum_versions(sub_packet)
        return total

    def analyze(self, bin_packet, i=0):
        version, i = self.version(bin_packet, i)
        type_id, i = self.type_id(bin_packet, i)
        # print(f"Version: {version}")
        # print(f"Type ID: {type_id}")

        if type_id != 4: # subpackets
            length_type_id, i = self.length_type_id(bin_packet, i)

            if length_type_id == 0:
                # then the next 15 bits are a number that represents 
                # the total length in bits of the sub-packets contained by this packet.
                length_in_bits, i = self.length_in_bits(bin_packet, i)
                sub_packets, i = self.get_sub_packets_by_length(bin_packet, length_in_bits, i)
            else:
                sub_packets, i = self.get_sub_packets_by_number(bin_packet, i)
            value = self.calculate_value(type_id, sub_packets)
            return Packet(version, type_id, value, sub_packets), i
        else: # literal
            value, i = self.get_literal_value(bin_packet, i)
            # print(f"Found literal packet with value {value}")
            return Packet(version, type_id, value, []), i


def part_1(transmission):
    pa = PacketAnalyzer(transmission)
    outer_packet = pa.analyze(pa.bin_packet)[0]
    return pa.sum_versions(outer_packet)

print(part_1(TRANSMISSION))

def part_2(transmission):
    pa = PacketAnalyzer(transmission)
    outer_packet = pa.analyze(pa.bin_packet)[0]
    return outer_packet.value

print(part_2(TRANSMISSION))

