import ipaddress


class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """
        self.address = address
        self.available = available
        self.last_used = last_used

    def __lt__(self, other):
        return ipaddress.ip_address(self.address) < ipaddress.ip_address(other.address)
