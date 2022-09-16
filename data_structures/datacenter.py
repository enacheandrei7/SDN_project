import re
from data_structures.cluster import Cluster


class Datacenter:
    def __init__(self, name, cluster_list):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """
        self.name = name
        self.cluster_list = [Cluster(key, value['networks'], value['security_level'])
                             for key, value in cluster_list.items()]

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """
        invalid_clusters = []

        for cluster in self.cluster_list:
            cluster_name = getattr(cluster, 'name')
            reg_exp = re.compile(f'^{self.name[:3].upper()}-(\\d\\d?\\d?)$')
            match_name = reg_exp.match(cluster_name)
            if not match_name:
                invalid_clusters.append(cluster)

        self.cluster_list = [cluster for cluster in self.cluster_list if cluster not in invalid_clusters]
