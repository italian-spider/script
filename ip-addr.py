#!/usr/bin/env python3

address = input('Enter ip address / prefix length: ')
oct1 = int(address[0:address.find('.')])
ns = address.find('.') + 1
address = address[ns:]
oct2 = int(address[0:address.find('.')])
ns = address.find('.') + 1
address = address[ns:]
oct3 = int(address[0:address.find('.')])
ns = address.find('.') + 1
address = address[ns:]
oct4 = int(address[0:address.find('/')])
ns = address.find('/') + 1
address = address[ns:]
mask = int(address)

# editing to binary view
b_oct1 = str(bin(oct1))
b_oct1 = b_oct1[b_oct1.find('b') + 1:]
b_oct1 = '0000000' + b_oct1
b_oct1 = b_oct1[-8:]

b_oct2 = str(bin(oct2))
b_oct2 = b_oct2[b_oct2.find('b') + 1:]
b_oct2 = '0000000' + b_oct2
b_oct2 = b_oct2[-8:]

b_oct3 = str(bin(oct3))
b_oct3 = b_oct3[b_oct3.find('b') + 1:]
b_oct3 = '0000000' + b_oct3
b_oct3 = b_oct3[-8:]

b_oct4 = str(bin(oct4))
b_oct4 = b_oct4[b_oct4.find('b') + 1:]
b_oct4 = '0000000' + b_oct4
b_oct4 = b_oct4[-8:]

#print("#" * 40)
print('Network:')
print(oct1, oct2, oct3, oct4)
print('Binary view:')
print(b_oct1, b_oct2, b_oct3, b_oct4)
#print('{:b} {:b} {:b} {:b}'.format(oct1, oct2, oct3, oct4))
#print("#" * 40)
#mask = int(input('Enter prefix length: '))
dobav = 32 - mask
bin_mask = '1' * mask
bin_mask = bin_mask + '0' * dobav
mask_oct1 = bin_mask[0:8]
mask_oct2 = bin_mask[8:16]
mask_oct3 = bin_mask[16:24]
mask_oct4 = bin_mask[24:32]
print('Mask:')
print(int(mask_oct1, 2), int(mask_oct2, 2), int(mask_oct3, 2), int(mask_oct4, 2))
print('Binary view:')
print(mask_oct1, mask_oct2, mask_oct3, mask_oct4)
