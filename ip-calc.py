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

bin_addr = b_oct1 + b_oct2 + b_oct3 + b_oct4
bin_net = bin_addr[0:mask]
host_range = bin_net
c_dbv = 32 - mask
dbv = '0' * c_dbv
bin_net = bin_net + dbv
net_oct1 = bin_net[0:8]
net_oct2 = bin_net[8:16]
net_oct3 = bin_net[16:24]
net_oct4 = bin_net[24:32]
#print(int(net_oct1, 2), int(net_oct2, 2), int(net_oct3, 2), int(net_oct4, 2))

#detect_class
if oct1 <= 127:
	detect_cl = 'A'
elif oct1 >= 128 and oct1 <=191:
	detect_cl = 'B'
elif oct1 >= 192 and oct1 <= 223:
	detect_cl = 'C'
elif oct1 >= 224 and oct1 <= 239:
	detect_cl = 'D'
else: detect_cl = 'not classified'
#print(detect_cl)
#
#max and min network host
#host_range = bin_net
c_dbv = 32 - mask
dbv1 = '0' * c_dbv
dbv2 = '1' * c_dbv
host_min = host_range + dbv1
host_max = host_range + dbv2
#
#print("#" * 40)
print('Entered IP address: ')
print(oct1, oct2, oct3, oct4)
print('Binary view:')
print(b_oct1, b_oct2, b_oct3, b_oct4)
print('Network:')
print(int(net_oct1, 2), int(net_oct2, 2), int(net_oct3, 2), int(net_oct4, 2))
print('Binary view:')
print(bin_net)
print('Network class:')
print(detect_cl)
print('Minimal host address (network number): ')
print(int(host_min[0:8], 2), int(host_min[8:16], 2), int(host_min[16:24], 2), int(host_min[24:32], 2))
print('Maximum host address (broadcast): ')
print(int(host_max[0:8], 2), int(host_max[8:16], 2), int(host_max[16:24], 2), int(host_max[24:32], 2))
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

