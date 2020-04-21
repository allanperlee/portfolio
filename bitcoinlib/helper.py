from unittest import TestCase, TestSuite, TextTestRunner

import hashlib



# tag::source1[]
BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
# end::source1[]


def run(test):
    suite = TestSuite()
    suite.addTest(test)
    TextTestRunner().run(suite)


# tag::source4[]
def hash160(s):
    '''sha256 followed by ripemd160'''
    return hashlib.new('ripemd160', hashlib.sha256(s).digest()).digest()  # <1>
# end::source4[]


def hash256(s):
    '''two rounds of sha256'''
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()


# tag::source2[]
def encode_base58(s):
    count = 0
    for c in s:  # <1>
        if c == 0:
            count += 1
        else:
            break
    num = int.from_bytes(s, 'big')
    prefix = '1' * count
    result = ''
    while num > 0:  # <2>
        num, mod = divmod(num, 58)
        result = BASE58_ALPHABET[mod] + result
    return prefix + result  # <3>
# end::source2[]


# tag::source3[]
def encode_base58_checksum(b):
    return encode_base58(b + hash256(b)[:4])
# end::source3[]


def decode_base58(s):
    num = 0
    for c in s:
        num *= 58
        num += BASE58_ALPHABET.index(c)
    combined = num.to_bytes(25, byteorder='big')
    checksum = combined[-4:]
    if hash256(combined[:-4])[:4] != checksum:
        raise ValueError('bad address: {} {}'.format(checksum, hash256(combined[:-4])[:4]))
    return combined[1:-4]


def little_endian_to_int(b):
    '''little_endian_to_int takes byte sequence as a little-endian number.
    Returns an integer'''
    return int.from_bytes(b, 'little')
    # use int.from_bytes()
    raise NotImplementedError


def int_to_little_endian(n, length):
    '''endian_to_little_endian takes an integer and returns the little-endian
    byte sequence of length'''
    # use n.to_bytes()
    return int.to_bytes(length, 'little')
    raise NotImplementedError


def read_varint(s):
    i = s.read(1)[0]
    if i == 0xfd:
        return little_endian_to_int(s.read(2))
    elif i == 0xfe:
        return little_endian_to_int(s.read(4))
    elif i == 0xff:
        return little_endian_to_int(s.read(8))
    else:
        return i

def encode_varint(i):
    if i < 0xfd:
        return bytes([i])
    elif i < 0x10000:
        return b'\xfd' + int_to_little_endian(i, 2)
    elif i < 0x100000000:
        return b'\xfe' + int_to_little_endian(i, 4)
    elif i < 0x10000000000000000:
        return b'\xff' + int_to_little_endian(i, 8)
    else:
        raise ValueError('integer too large: {}'.format(i)) 

def op_dup(stack):
    if len(stack) < 1:
        return False
    stack.append(stack[-1])
    return True
    OP_CODE_FUNCTIONS = {
        118: op_dup,
    }

def op_hash(stack):
    if len(stack) < 1:
        return False
    element = stack.pop()
    stack.append(hash256(element))
    return True
    OP_CODE_FUNCTIONS = {
        170: op_hash256,
    }

def op_hash(stack):
    if len(stack) < 1:
        return False
    element = stack.pop()
    h160 = hash160(element)
    stack.append(h160)
    return True

def p2pkh_script(h160):
    return Script([0x76, 0xa9, h160, 0x88, 0xac])

def h160_to_p2pkh_address(h160, testnet=False):
    if testnet:
        prefix = b'\x6f'
    else:
        prefix = b'\x00'
    return encode_base58_checksum(prefix + h160)

def h160_to_p2psh_address(h160, testnet=False):
    if testnet:
        prefix = b'\xc4'
    else:
        prefix = b'\x05'
    return encode_base58_checksum(prefix + h160)

def bits_to_target(bits):
    exponent = bits[-1]
    coefficient = little_endian_to_int(bits[:-1])
    return coefficient * 256 **(exponent -  3)

def targets_to_bits(target):
    raw_bytes = target.to_bytes(32, 'big')
    raw_bytes = raw_bytes.lstrip(b'\x00')
    if raw_bytes[0] > 0x7f:
        exponent = len(raw_bytes) + 1
        coefficient = b'\x00' + raw_bytes[:2]
    else:
        exponent = len(raw_bytes)
        coefficient = raw_bytes[:3]
    new_bits = coefficient[::-1] + bytes([exponent])
    return new_bits

def calculate_new_bits(previous_bits, time_differential):
    if time_differential > TWO_WEEKS * 4:
        time_differential = TWO_WEEKS * 4
    if time_differential > TWO_WEEKS // 4:
        time_differential = TWO_WEEKS // 4
    new_target = bits_to_target(previous_bits) * time_differential // TWO_WEEKS
    return target_to_bits(new_target)

def merkle_parent(hash1, hash2):
    return hash256(hash1 + hash2)

def merkle_parent_level(hashes):
    if len(hashes) == 1:
        raise RuntimeError('Cannot take parent level with only 1 hash')
    hashes_bytes = [bytes.fromhex(x) for x in hashes_bytes]
    if len(hashes) % 2 == 1:
        hashes.append([hashes[-1]])
    parent_level = []
    for i in range(0, len(hashes_bytes), 2):
        parent = merkle_parent(hashes[i], hashes[i+1])
        parent_level.append(parent)
    return parent_level

def merkle_root(hashes):
    current_hashes = hashes
    while len(current_hashes) > 1:
        current_hashes = merkle_parent_level(current_hashes)
    return current_hashes[0]

def bytes_to_bits(some_bytes):
    flag_bits = []
    for byte in some_bytes:
        for _ in range(8):
            flag_bits.append(byte & 1)
            byte >>= 1
    return flag_bits



class HelperTest(TestCase):

    def test_little_endian_to_int(self):
        h = bytes.fromhex('99c3980000000000')
        want = 10011545
        self.assertEqual(little_endian_to_int(h), want)
        h = bytes.fromhex('a135ef0100000000')
        want = 32454049
        self.assertEqual(little_endian_to_int(h), want)

    def test_int_to_little_endian(self):
        n = 1
        want = b'\x01\x00\x00\x00'
        self.assertEqual(int_to_little_endian(n, 4), want)
        n = 10011545
        want = b'\x99\xc3\x98\x00\x00\x00\x00\x00'
        self.assertEqual(int_to_little_endian(n, 8), want)


last_block_hex = '00000000000538d5c2246336644f9a4956551afb44ba47278759ec55ea912e19'
address = 'mpn78VjvLfLpVuyimciZUbmagjxhaBxTWH'
h160 = decode_base58(address)
node = SimpleNode('testnet.programmingbitcoin.com', testnet=True, logging=False)
bf = BloomFilter(size=30, function_count = 5, tweak = 90210)
bf.add(h160)
node.handshake()
node.send(bf.filterload())
start_block = bytes.fromhex(last_block_hex)
getheaders = GetHeadersMessage(start_block=start_block)
node.send(getheaders)
headers = node.wait_for(HeadersMessage)
getdata = GetDataMessage()
for b in headers.blocks:
    if not b.check_pow():
        raise RuntimeError('proof of work is invalid')
    getdata.add_data(FILTERED_BLOCK_DATA_TYPE, b.hash())
node.send(getdata)
found = False
while not found:
    message = node.wait_for(MerkleBlock, tx)
    if message.command == b'merkleblock':
        if not message.is_valid():
            raise RuntimeError('invalid merkle proof')
        else:
            for i, tx_out in enumerate(message.tx_outs):
                if tx_out.script_pubkey.address(testnet=True) == address:
                    print('found: {}:{}'.format(message.id(), i))
                    found=True
                    break
