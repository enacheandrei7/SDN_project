import unittest
from json import load
from data_structures.datacenter import Datacenter


class TestEntriesValidation(unittest.TestCase):
    """
    Tests if only the Entries with valid IP addresses are kept in the networks lists, and then it verifies if the
    sorting is correctly done
    """

    @classmethod
    def setUpClass(cls):
        """
        Creates the entries lists for the first cluster of the first datacenter
        """
        with open('../response.json', 'r') as f:
            data = load(f)

        datacenter_1 = getattr(Datacenter('Berlin', data['Berlin']), 'cluster_list')[0]
        cls.network_1 = getattr(datacenter_1, 'network_list')[0]
        cls.network_2 = getattr(datacenter_1, 'network_list')[1]

    def test_remove_invalid_records(self):
        """
        Tests if only the entries with valid IPv4 addresses corresponding to the IPV4 network are kept in the
        entries list.
        """
        self.network_1.remove_invalid_records()
        self.network_2.remove_invalid_records()

        net_1_addresses = [getattr(entry, 'address') for entry in getattr(self.network_1, 'entries')]
        net_2_addresses = [getattr(entry, 'address') for entry in getattr(self.network_2, 'entries')]

        net_1_valid_entries = ["192.168.0.1", "192.168.0.4", "192.168.0.2", "192.168.0.3"]
        net_2_valid_entries = ["10.0.11.254", "10.0.8.1", "10.0.8.0"]

        self.assertEqual(net_1_addresses, net_1_valid_entries)
        self.assertEqual(net_2_addresses, net_2_valid_entries)

    def test_sort_entries(self):
        """
        Tests if the entries in the entries list are correctly sorted according to their addresses
        """
        self.network_1.sort_records()
        self.network_2.sort_records()

        net_1_addresses = [getattr(entry, 'address') for entry in getattr(self.network_1, 'entries')]
        net_2_addresses = [getattr(entry, 'address') for entry in getattr(self.network_2, 'entries')]

        net_1_sorted_entries = ["192.168.0.1", "192.168.0.2", "192.168.0.3", "192.168.0.4"]
        net_2_sorted_entries = ["10.0.8.0", "10.0.8.1", "10.0.11.254"]

        self.assertEqual(net_1_addresses, net_1_sorted_entries)
        self.assertEqual(net_2_addresses, net_2_sorted_entries)


if __name__ == '__main__':
    unittest.main()
