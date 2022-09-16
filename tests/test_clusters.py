import unittest
from json import load
from data_structures.datacenter import Datacenter


class TestClustersValidation(unittest.TestCase):
    """
    Tests if only the clusters with valid names are kept in the cluster lists
    """

    def setUp(self):
        """
        Sets up the datacenter lists needed for the test
        """
        with open('../response.json', 'r') as f:
            data = load(f)
            
        self.datacenter_1 = Datacenter('Berlin', data['Berlin'])
        self.datacenter_2 = Datacenter('Paris', data['Paris'])

    def test_remove_invalid_clusters(self):
        """
        Verifies if only the clusters with valid names are kept in the clusters lists
        """
        self.datacenter_1.remove_invalid_clusters()
        self.datacenter_2.remove_invalid_clusters()

        clusters_objects_list_d1 = getattr(self.datacenter_1, 'cluster_list')
        clusters_objects_list_d2 = getattr(self.datacenter_2, 'cluster_list')

        clusters_d1 = [getattr(cluster, 'name') for cluster in clusters_objects_list_d1]
        clusters_d2 = [getattr(cluster, 'name') for cluster in clusters_objects_list_d2]

        valid_names_d1 = ['BER-1', 'BER-203']
        valid_names_d2 = ['PAR-1']

        self.assertEqual(clusters_d1, valid_names_d1)
        self.assertEqual(clusters_d2, valid_names_d2)


if __name__ == '__main__':
    unittest.main()
