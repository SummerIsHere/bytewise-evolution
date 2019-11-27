#! python3

import binascii as bin
import itertools, os

import logging
logging.basicConfig(filename='logging.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# Initialize basic set of bytes
hex_tuple = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')
b = list(itertools.product(hex_tuple,repeat=2))
byte_list = []
for i in range(0,len(b),1):
    hexbyte = bin.unhexlify(''.join(b[i]))
    byte_list.append(hexbyte)

logging.debug('start functoin defintion')
# Function to create next level of bytes
def mutate(b1,b2):
    nl = []
    for i in b1:
        for j in b2:
            nl.append(i+j)
    return(nl)

l=1
while 1==1:
    m = 1
    for i in byte_list:
        logging.debug('l: '+str(l) + ', m: '+str(m))
        species = 'L'+str(l)+'M'+str(m)+'.exe'
        dna = open(species, 'wb')
        dna.write(i)
        dna.close()
        ms = os.system(species)
        logging.debug('os.system return value: ' + str(ms))
        # It should not move on to this removal part until the program has finished executing
        if ms != 0:
            os.remove(species)
        m = m+1
    # Create byte list
    # TODO: output the byte combinations one at a time instead of all at once in a list
    byte_list = mutate(byte_list.copy(), byte_list.copy())
    l = l+1

