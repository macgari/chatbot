import urllib3
import json
from constants import MAX_RECORDS


class Store:
    def __init__(self):
        """
            initialize data store
        """
        self.store_url = "http://localhost:3000/data"
        self.http = urllib3.PoolManager()
        self.get_url = f"{self.store_url}?_sort=id&_order=desc&_end={MAX_RECORDS}"

    def put(self, data):
        """
            store data
            into the data store
            
            data: str()
        """
        encoded_data = json.dumps({'data': data}).encode('utf-8')
        self.http.request('POST',
                          self.store_url,
                          headers={'Content-Type': 'application/json'},
                          body=encoded_data)

    def get(self):
        """
            retrieve last n records
            from the data store
            
            return: list()
        """
        resp = self.http.request('GET', self.get_url)
        if resp.data:
            data = json.loads(resp.data)
            msg_list = [[msg for msg in msg_object.values()][0] for msg_object in data]
            msg_list.reverse()
            return msg_list
        raise urllib3.exceptions.ConnectionError
