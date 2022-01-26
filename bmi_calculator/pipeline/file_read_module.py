import pandas as pd

"""Method to read json file
input: jason file path
output: dataframe
"""
def read_json(path):
    print('Reading json files')
    json_data = pd.read_json(path)
    print('File read completed. {} records read.'.format(json_data.shape[0]))
    return json_data