import re
class Solution:
    def check4(self, IP):
        l = IP.split('.')
        if len(l) != 4:
            return "Neither"
        # checking for leading 0
        for element in l:
            if(element != '0' and element.startswith('0')):
                print(element)
                return "Neither"
        # check number
        for element in l:
            try:
                if '-' in element or '+' in element:
                    return "Neither"
                if not (int(element) >= 0 and int(element) <= 255):
                    return "Neither"
            except:
                return "Neither"
        return "IPv4"
    
    def check6(self, IP):
        IP = IP.lower()
        l = IP.split(':')
        if len(l) != 8:
            return "Neither"
        # checking for non hexa
        for element in l:
            if(len(element) > 4 or '-' in element or '+' in element):
                return "Neither"
            try:
                x = int(element, 16)
            except:
                return "Neither"
        return "IPv6"
    
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            result = self.check4(IP)
        elif ':' in IP:
            result = self.check6(IP)
        else:
            result = "Neither"
        return result
