# Ross Moriwaki
# Ver 1.0 12/16/17
# network Generator
# This script determines the number of Networks, the ranges, and usable IPs for a user

import os


# Function: getIPstring
# This function converts the user input network IP and converts it into a substring to be used later
# Also does some error handling for incorrect formatting
def getIPstring(userIP):
    try:
        parts = userIP.split(".")
        IPstring = str(int(parts[0]))+"."+str(int(parts[1]))+"."+str(int(parts[2]))+"."
        return IPstring
    except (IndexError, ValueError):
        print("Error: Incorrect IP format.  Format should be xxx.xxx.xxx.x (ex. 192.168.1.0)")
        print("Please restart. Exiting...")
        exit(0)

# Function: getNumNetworks
# This function takes the input for desired number of networks and calculates the least number of networks required
# Returns result as an int
def getNumNetworks(networkInput):
    for x in range(8):
        if networkInput <= 2**x:
            numNetworks = 2**x
            break
    return int(numNetworks)

# Function: isFlagOn
# This function toggles the flag for whether the user wants to see the main network in results
def isFlagOn(flagInput):
    if flagInput == "y":
        return 1
    if flagInput == "n":
        return 0
    else:
        return -1

# Function: getNumHosts
# This function calculates the number of hosts belonging to each network
# Returns result as an int
def getNumHosts(numNetworks):
    numHosts = 256/numNetworks
    return int(numHosts)

# Function: getCIDR
# This function calculates the CIDR (/xx) based on the number of networks
# Returns result as an int
def getCIDR(numNetworks):
    for x in range(8):
        if 2**x == numNetworks:
            CIDR = 24+x
            break
    return int(CIDR)

# Function: getRangeList
# This function creates a list of all network ranges of IPs from 0-255
# Returns result as a list
def getRangeList(numHosts, numNetworks):
    rangeList = []
    addr = 0
    for x in range(0, numNetworks):
        rangeList.append(addr)
        addr += numHosts
    return rangeList

# Function: printAvailableNetworks
# This function formats and prints a list of network IPs, the ranges, and broadcast IPs
# Prints directly to the stdout
def printAvailableNetworks(IPstring, rangeList, numHosts, networkFlag):
    startList = 0

    print("{:10s} {:20s} {:15s} {:20s}".format("Network:", "Network ID:", "Range:", "Broadcast:"))
    if networkFlag == 0:
        startList = 1
        print("{:10s} {:20s}".format("1", "Main Network omitted"))
    for x in range(startList, len(rangeList)):
        print("{:10s} {:20s} {:15s} {:20s}".format( str(x+1), IPstring+str(rangeList[x]), str(rangeList[x]+1)+" - "+ str((rangeList[x]+numHosts-2)), IPstring+str((rangeList[x]+numHosts-1))))

# Function: getSubnetMask
# This function calculates the subnet mask using the CIDR, therefore the CIDR must be defined before using this function
# Returns as an int
def getSubnetMask(CIDR):
    CIDR = CIDR-24
    subnetMask = 0
    for x in range(0,CIDR):
        subnetMask += 256/(2**(x+1))
    return int(subnetMask)

# Function: getMaskNumNetworks
# This function calculates the number of networks using the subnet mask
# Returns as an int
def getMaskNumNetworks(maskInput):
    numNetworks = 0
    check = 0
    try:
        parts = maskInput.split(".")
        mask = int(parts[3])
    except (IndexError, ValueError):
        print("Error: Incorrect IP format.  Format should be xxx.xxx.xxx.x (ex. 192.168.1.0)")
        print("Please restart. Exiting...")
        exit(0)

    if mask == check:
        return int(numNetworks)
    for x in range(8):
        check += 256/(2**(x+1))
        if mask == check:
            numNetworks = 2**(x+1)
            return int(numNetworks)
        if x == 8:
            print("Error: Invalid subnet mask! (mask must be a valid bit value in the CIDR format)")
            print("Exiting...")
            exit(0)

def formatCIDRinput(CIDRinput):
    try:
        if int(CIDRinput) >= 24 and int(CIDRinput) <= 30:
            return int(CIDRinput)
    except ValueError:
        print("Error: CIDR should be an int value between 24 and 30!")
        return -1

while True:
    print("\n")
    print("Choose your operation using the numbered selection below: ")
    print("1 : Get network information by inputting network IP and number of networks needed")
    print("2 : Get network information by inputting network IP and subnet mask")
    print("3 : Get network information by inputting network IP and CIDR notation")
    print("4 : Input two IP addresses and CIDR notation to determine if on same network")
    print("5 : Exit")
    try:
        choice = int(input())
        if choice < 1 or choice > 5:
            print("Error: input must be an int between 1 and 5!")
            continue
    except ValueError:
        print("Error: input must be an int between 1 and 5!")
        continue
    if choice == 1:
        print("Input the network IP address (ex. 192.168.0.1)")
        IPinput = input()
        while True:
            print("Input the number of networks required (# of networks should be between 0 and 64)")
            try:
                networkInput = int(input())
                if networkInput >= 0 and networkInput <= 64:
                    break
                else:
                    print("Error: Number of networks should be between 0 and 64!")
            except ValueError:
                print("Error: Input should be an integer!")


        print("Would you like to show the main .0 network in network range results? (y/n)")
        flagInput = input()

        # All variables to be used in output are initialized using functions above
        IPstring = getIPstring(IPinput)
        networkFlag = isFlagOn(flagInput)
        numNetworks = getNumNetworks(networkInput)
        numHosts = getNumHosts(numNetworks)
        CIDR = getCIDR(numNetworks)
        rangeList = getRangeList(numHosts, numNetworks)
        subnetMask = getSubnetMask(CIDR)

        print("\n"*2)
        print("Network Information:")
        print("Number of Networks: "+str(numNetworks))
        print("Number of IPs/Network: "+str(numHosts))
        print("")

        print("Available Networks:")
        printAvailableNetworks(IPstring, rangeList, numHosts, networkFlag)

        print("\nSubnet Mask: 255.255.255." + str(subnetMask))
        print("\nCIDR Notation: " "/"+str(CIDR))

        input("Press any key to continue...")

    if choice == 2:
        print("Input the network IP address (ex. 192.168.0.1)")
        IPinput = input()
        print("Input the subnet mask (ex. 255.255.255.192)")
        maskInput = input()
        print("Would you like to show the main .0 network in network range results? (y/n)")
        flagInput = input()

        # All variables to be used in output are initialized using functions
        IPstring = getIPstring(IPinput)
        networkFlag = isFlagOn(flagInput)
        numNetworks = getMaskNumNetworks(maskInput)
        numHosts = getNumHosts(numNetworks)
        CIDR = getCIDR(numNetworks)
        rangeList = getRangeList(numHosts, numNetworks)
        subnetMask = getSubnetMask(CIDR)

        print("\n" * 2)
        print("Network Information:")
        print("Number of Networks: " + str(numNetworks))
        print("Number of IPs/Network: " + str(numHosts))
        print("")

        print("Available Networks:")
        printAvailableNetworks(IPstring, rangeList, numHosts, networkFlag)

        print("\nSubnet Mask: 255.255.255." + str(subnetMask))
        print("\nCIDR Notation: " "/" + str(CIDR))

        input("Press any key to continue...")

    if choice == 3:
        print("Input the network IP address (ex. 192.168.0.1)")
        IPinput = input()
        CIDR = -1
        while(CIDR == -1):
            print("Input the CIDR notation (ex. if /24 notation type 24)")
            CIDRinput = input()
            CIDR = formatCIDRinput(CIDRinput)
        print("Would you like to show the main .0 network in network range results? (y/n)")
        flagInput = input()

        # All variables to be used in output are initialized using functions
        IPstring = getIPstring(IPinput)
        networkFlag = isFlagOn(flagInput)
        subnetMask = getSubnetMask(CIDR)
        numNetworks = getMaskNumNetworks("255.255.255." + str(subnetMask))
        numHosts = getNumHosts(numNetworks)
        rangeList = getRangeList(numHosts, numNetworks)

        print("\n" * 2)
        print("Network Information:")
        print("Number of Networks: " + str(numNetworks))
        print("Number of IPs/Network: " + str(numHosts))
        print("")

        print("Available Networks:")
        printAvailableNetworks(IPstring, rangeList, numHosts, networkFlag)

        print("\nSubnet Mask: 255.255.255." + str(subnetMask))
        print("\nCIDR Notation: " "/" + str(CIDR))

        input("Press any key to continue...")

    if choice == 4:
        print("Input the first IP address (ex. 192.168.0.12)")
        IPinput1 = input()
        CIDRinput1 = -1
        while (CIDRinput1 == -1):
            print("Input the CIDR notation for the first IP (ex. if /24 notation type 24)")
            CIDRinput1 = input()
            CIDRinput1 = formatCIDRinput(CIDRinput1)
        print("Input the second IP address (ex. 192.168.0.15)")
        IPinput2 = input()
        CIDRinput2 = -1
        while (CIDRinput2 == -1):
            print("Input the CIDR notation for the second IP (ex. if /24 notation type 24)")
            CIDRinput2 = input()
            CIDRinput2 = formatCIDRinput(CIDRinput2)

        IPstring1 = getIPstring(IPinput1)
        IPstring2 = getIPstring(IPinput2)
        subnetMask1 = getSubnetMask(CIDRinput1)
        subnetMask2 = getSubnetMask(CIDRinput2)

        if IPstring1==IPstring2 and subnetMask1==subnetMask2:
            print("The IPs are on the same network")
        else:
            print("The IPs are not on the same network")

        input("Press any key to continue...")



    if choice == 5:
        print("Exiting...")
        exit(0)