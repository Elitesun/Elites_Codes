# find the possible ip addresses from a given ip address

def ips_between(start, end):
    def Ip(ip):
        octets = list(map(int , ip.split('.')))
        result = 0
        for i in range(len(octets)):
            result += octets[i]*256**(3-i)
        return result
    return Ip(end) - Ip(start)
# i did this .........*

# and i found this......
from ipaddress import ip_address

def ips_betwee(start, end):
    return int(ip_address(end)) - int(ip_address(start))

    # like i didnt even know about ipaddress module until that day . felt useless
    