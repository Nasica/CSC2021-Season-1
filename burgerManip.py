import base64
import binascii

first = b'Sesame seed bun'
second = b'Chicken breast'
third = b'Veggie patty'
fourth = b'Special sauce'
fifth = b'No cheese print("test")'

header = b'\x80\x04\x95'
padding = b'\x00\x00\x00\x00\x00\x00\x00'
startOfString = b'\x5d\x94\x28\x8c'
firstString = str(binascii.hexlify(first))
sizeOfFirstString = '{:02x}'.format(len(first))
secondString = str(binascii.hexlify(second))
sizeOfSecondString ='{:02x}'.format(len(second)) 
thirdString = str(binascii.hexlify(third))
sizeOfThirdString = '{:02x}'.format(len(third)) 
fourthString = str(binascii.hexlify(fourth))
sizeOfFourthString = '{:02x}'.format(len(fourth)) 
fifthString = str(binascii.hexlify(fifth))
sizeOfFifthString = '{:02x}'.format(len(fifth)) 
filler = b'\x94\x8c'
footer = b'\x94\x65\x2e'


total = header.hex() + "XX" + padding.hex() + startOfString.hex() + sizeOfFirstString + firstString[2:-1] + filler.hex() + sizeOfSecondString + secondString[2:-1] + filler.hex() + sizeOfThirdString + thirdString[2:-1] + filler.hex() + sizeOfFourthString + fourthString[2:-1] + filler.hex() + sizeOfFifthString + fifthString[2:-1] + footer.hex()
sizeOfAllString = '{:02X}'.format((len(total) - 22 ) // 2)
total = header.hex() + sizeOfAllString + padding.hex() + startOfString.hex() + sizeOfFirstString + firstString[2:-1] + filler.hex() + sizeOfSecondString + secondString[2:-1] + filler.hex() + sizeOfThirdString + thirdString[2:-1] + filler.hex() + sizeOfFourthString + fourthString[2:-1] + filler.hex() + sizeOfFifthString + fifthString[2:-1] + footer.hex()
print(total)
