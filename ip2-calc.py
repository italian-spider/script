#!/usr/bin/env python3.6

# Function Block
def create_octet_ls( addr_str ):
     """Razbivka binarnoi stroki na octety i vyvod spiska """
     list_octets = []
     list_octets.append(addr_str[0:8])
     list_octets.append(addr_str[8:16])
     list_octets.append(addr_str[16:24])
     list_octets.append(addr_str[24:32])
     return list_octets
#
def ls_binTodec (listoctet):
     """Bin spisok octetov to dec spisok i vyvod spiska"""
     rezdec = []
     for i in range(4):
         rezdec.append(int(listoctet[i], 2))
     return rezdec
# Check format input
a = 0
while a != 1:
    address = input('Enter ip in format: ')
    if address.count('.') != 3:
        print('Wrong format')
    elif address.count('/') != 1:
        print('Wrong format')
    else:
        print('Calculation...')
        a = 1
#spisok octetov adresa i dlina maski
l_addr_str = []
for i in range(4):
     if i > 2:
         octet = int(address[0:address.find('/')])
         ns = address.find('/') + 1
         address = address[ns:]
         mask = int(address)
         l_addr_str.append(octet)
     else:
         octet = int(address[0:address.find('.')])
         ns = address.find('.') + 1
         address = address[ns:]
         l_addr_str.append(octet)
# editing to binary view
l_addr_b = []
for i in range(4):
    b_octet = str(bin(l_addr_str[i]))
    b_octet = b_octet[b_octet.find('b') + 1:]
    b_octet = '0000000' + b_octet
    l_addr_b.append(b_octet[-8:])
# config spiska octetov maski BIN
bin_addr = l_addr_b[0] + l_addr_b[1] + l_addr_b[2] + l_addr_b[3]
bin_net = bin_addr[0:mask]
host_range = bin_net
c_dbv = 32 - mask
dbv = '0' * c_dbv
bin_net = bin_net + dbv
l_net_b = create_octet_ls(bin_net)
#detect_class
if int(l_addr_str[0]) <= 127:
	detect_cl = 'A'
elif int(l_addr_str[0]) >= 128 and int(l_addr_str[0]) <=191:
	detect_cl = 'B'
elif int(l_addr_str[0]) >= 192 and int(l_addr_str[0]) <= 223:
	detect_cl = 'C'
elif int(l_addr_str[0]) >= 224 and int(l_addr_str[0]) <= 239:
	detect_cl = 'D'
else: detect_cl = 'not classified'
#max and min network host
#host_range = bin_net
c_dbv = 32 - mask
dbv1 = '0' * c_dbv
dbv2 = '1' * c_dbv
host_min = host_range + dbv1
host_max = host_range + dbv2
#
l_host_max_b = create_octet_ls(host_max)
#
l_host_max_d = ls_binTodec(l_host_max_b)
#
l_host_min_b = create_octet_ls(host_min)
#
l_host_min_d = ls_binTodec(l_host_min_b)
#
l_net_dec = ls_binTodec(l_net_b)
#
#config prefix mask
dobav = 32 - mask
bin_mask = '1' * mask
bin_mask = bin_mask + '0' * dobav
l_mask_b = create_octet_ls(bin_mask)
l_mask_d = ls_binTodec(l_mask_b)
#
#Formirovanie vyvoda calculatora
#
#Pole Entered IP Address
ip_str_d = '.'.join([ str(l_addr_str) for l_addr_str in l_addr_str ])
ip_str_split = ' | '
ip_str_b = '.'.join([ str(l_addr_b) for l_addr_b in l_addr_b ])
#
#Pole mask
mask_str_d = '.'.join([ str(l_mask_d) for l_mask_d in l_mask_d ])
mask_str_b = '.'.join([ str(l_mask_b) for l_mask_b in l_mask_b ])
#
#Pole network
net_str_d = '.'.join([ str(l_net_dec) for l_net_dec in l_net_dec ])
net_str_b = '.'.join([ str(l_net_b) for l_net_b in l_net_b ])
#
#Pole min host
mih_str_d =  '.'.join([ str(l_host_min_d) for l_host_min_d in l_host_min_d ])
mih_str_b =  '.'.join([ str(l_host_min_b) for l_host_min_b in l_host_min_b ])
#
#
#Pole max host
mah_str_d =  '.'.join([ str(l_host_max_d) for l_host_max_d in l_host_max_d ])
mah_str_b =  '.'.join([ str(l_host_max_b) for l_host_max_b in l_host_max_b ])
#

print('-' * 56)
print('Entered IP address: ')
print("{:15} {:3} {:35}".format(ip_str_d, ip_str_split, ip_str_b))
print('-' * 56)
print('Mask')
print("{:15} {:3} {:35}".format(mask_str_d, ip_str_split, mask_str_b))
print('-' * 56)
print('Network:')
print("{:15} {:3} {:35}".format(net_str_d, ip_str_split, net_str_b))
print('-' * 56)
print('Minimal host address (network number): ')
print("{:15} {:3} {:35}".format(mih_str_d, ip_str_split, mih_str_b))
print('-' * 56)
print('Maximum host address (broadcast): ')
print("{:15} {:3} {:35}".format(mah_str_d, ip_str_split, mah_str_b))
print('-' * 56)
print('Network class:')
print(detect_cl)
print('-' * 56)

#print('{:b} {:b} {:b} {:b}'.format(oct1, oct2, oct3, oct4))

