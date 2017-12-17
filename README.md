# SubnetGenerator
- This tool allows a user to grab information when using or creating a subnet using subnet/IP information
- Information:
    - Number of Networks
    - Number of Hosts allowed per network
    - Network ID, Range, and Broadcast address for each network

**Sample Output**
```
Network Information:
Number of Networks: 8
Number of IPs/Network: 32

Available Networks:
Network:   Network ID:          Range:          Broadcast:
1          192.168.1.0          1 - 30          192.168.1.31
2          192.168.1.32         33 - 62         192.168.1.63
3          192.168.1.64         65 - 94         192.168.1.95
4          192.168.1.96         97 - 126        192.168.1.127
5          192.168.1.128        129 - 158       192.168.1.159
6          192.168.1.160        161 - 190       192.168.1.191
7          192.168.1.192        193 - 222       192.168.1.223
8          192.168.1.224        225 - 254       192.168.1.255

Subnet Mask: 255.255.255.224

CIDR Notation: /27
```

### Functions
1. Get network information using the network IP and number of networks desired
2. Get network information using the network IP and a subnet mask
3. Get network information using the network IP and the CIDR notation
4. Find whether two known IPs are on the same network using IP addresses and CIDR notation