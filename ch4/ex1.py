"""
Input:
array of binary word: "0001" of 64 bits,
represented as integers

For each compute the parity of it, ie does it
have an odd or even number of bits
"""

    

def parity_of_word_lowest_bit(i):
    # i represents binary word in base 10 integer 
    # form
    # loop over each bit 
    # if bit is 1 add it to count
    # return % 2 of the count
    
    # we can improve the efficiency if we
    # only consider the lowest bit equal to 1
    current_parity = 0
    while(i):
        current_parity ^= 1
        i = i & (i - 1)
    return current_parity


assert parity_of_word_lowest_bit(5) == 0
assert parity_of_word_lowest_bit(4) == 1
assert parity_of_word_lowest_bit(64) == 1
assert parity_of_word_lowest_bit(15) == 0

# we can group it by bytes and create a lookup by byte
PRECOMPUTED_PARITY = []
MAX_BIT_CHUNK = 2 ** 16
for i in range(MAX_BIT_CHUNK):
    PRECOMPUTED_PARITY.append(parity_of_word_lowest_bit(i))

def parity_of_word(x):
    # word has 4 chunks
    BIT_MASK = 0xFFFF # can be & with x to get the lowest 4 bits
    MASK_SIZE = 16

    parity_0 = PRECOMPUTED_PARITY[x & BIT_MASK]
    parity_1 = PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK]
    parity_2 = PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK]
    parity_3 = PRECOMPUTED_PARITY[(x >> (3 * MASK_SIZE)) & BIT_MASK]

    return parity_0 ^ parity_1 ^ parity_2 ^ parity_3

assert parity_of_word(4234) == parity_of_word_lowest_bit(4234)
assert parity_of_word(18446744073409531616) == parity_of_word_lowest_bit(18446744073409531616)
assert parity_of_word(14446744073409531616) == parity_of_word_lowest_bit(14446744073409531616)

def parity_of_word_xor(x):
   # x is 64 bit
    x ^= x >> 32 # only last 32 bits matter now
    x ^= x >> 16 # only last 16 bits
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1

assert parity_of_word_xor(18446744073409531616) == parity_of_word_lowest_bit(18446744073409531616)
assert parity_of_word_xor(14446744073409531616) == parity_of_word_lowest_bit(14446744073409531616)


def right_prop(x):
    value_of_rightmost = x & ~(x - 1)
    return x | (value_of_rightmost - 1)

assert right_prop(0b01010000) == 0b01011111

def mod_power_of_two(target, dividor):
    # dividor must be power of 2
    # extract all bits smaller than that
    # make mask out of dividor
    mask = dividor - 1
    return target & mask

assert mod_power_of_two(77, 64) == 13
assert mod_power_of_two(35, 32) == 3
assert mod_power_of_two(15, 16) == 15

def is_power_of_two(x):
    # check if it has only a signle bit
    # remove rightmost bit
    # check if result is 0
    x = x & (x - 1)
    return x == 0

assert is_power_of_two(5) == False
assert is_power_of_two(256) == True
assert is_power_of_two(54352) == False

