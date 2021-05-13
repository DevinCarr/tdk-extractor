from bs4 import BeautifulSoup
import requests
import json

def get_pid(part_no):
    """Extract the PID from the part number page"""
    url = 'https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info?part_no=' + part_no
    page = requests.get(url)
    if (page.status_code != 200):
        print('Error getting page({}): {}'.format(page.status_code, url))
        return None
    soup = BeautifulSoup(page.text, 'html.parser')
    pid_input = soup.find(id='pid')
    if pid_input is None:
        return None
    return pid_input['value']

def get_graph_data(pid):
    """Get the graph datasets from the api"""
    url = 'https://product.tdk.com/pdc_api/en/search/capacitor/ceramic/mlcc/info/graph'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'https://product.tdk.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4121.0 Safari/537.36 Edg/84.0.495.2',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'X-Requested-With': 'XMLHttpRequest'
    }
    payload = { 'graph_kind[0]': '1007', 'graph_kind[1]': '1008', 'pid[]': pid }
    response = requests.post(url, headers=headers, data=payload)
    if (response.status_code != 200):
        print('Error getting graphs({}): {}'.format(response.status_code, url))
        return None
    try:
        dcbias_data = parse_dcbais_data(response.json()['graph'])
        temp_data = parse_temp_data(response.json()['graph'])
    except:
        return None
    
    return dcbias_data, temp_data

def clean_data(data):
    """Clean data tuples returned from api"""
    return list(map(lambda entry: [str(entry[0]), str(entry[1])], data))

def parse_dcbais_data(json_graph):
    """Parse the dc bias data"""
    return clean_data(json_graph['graph_kind_1007'][0]['data'])

def parse_temp_data(json_graph):
    """Parse the temp data"""
    temp_list = list(filter(lambda x: '100kHz' in x['label'], json_graph['graph_kind_1008']))
    if len(temp_list) == 0:
        return None
    return clean_data(temp_list[0]['data'])

def get_part_graph(part_no):
    pid = get_pid(part_no)
    if pid is None:
        return None
    return get_graph_data(pid)

