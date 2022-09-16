import requests
import time
from data_structures.datacenter import Datacenter


URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """
    data = dict()

    try:
        response = requests.get(url)

        if response.ok:
            data = response.json()
        else:
            for i in range(max_retries):
                time.sleep(delay_between_retries)
                response = requests.get(url)
                if response.ok:
                    data = response.json()
                    break
                else:
                    print(f'Try #{i}')
                    continue
    except requests.exceptions.MissingSchema as err:
        print('Please check the URL, it may be empty: ' + str(err))
    except requests.exceptions.ConnectionError as err:
        print('Network or URL Problem: ' + str(err))

    return data


def main():
    """
    Main entry to our program.
    """
    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    display_datacenters(datacenters)


def display_datacenters(datacenters):
    """
    Displays the datacenters along with their afferent information
​
    Args:
        datacenters (list): List of Datacenter objects
    """
    for datacenter in datacenters:
        datacenter.remove_invalid_clusters()
        print('Datacenter: ', getattr(datacenter, 'name'))
        for cluster in getattr(datacenter, 'cluster_list'):
            print('--Cluster: ', getattr(cluster, 'name'))
            print('----Security level: ', getattr(cluster, 'security_level'))
            print('------Networks: ')
            for index_net, network in enumerate(getattr(cluster, 'network_list')):
                network.remove_invalid_records()
                network.sort_records()
                print(f'--------ipv4 network {index_net+1}: ', getattr(network, 'ipv4_network'))
                for index_ent, entry in enumerate(getattr(network, 'entries')):
                    print(f'----------Entry {index_ent+1}: ')
                    print('------------Address: ', getattr(entry, 'address'))
                    print('------------Available: ', getattr(entry, 'available'))
                    print('------------Last used: ', getattr(entry, 'last_used'))


if __name__ == '__main__':
    main()
