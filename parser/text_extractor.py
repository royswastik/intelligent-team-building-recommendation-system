__author__ = 'Swastik'

def read_all_text(filepath):
    data = ''
    with open(filepath, 'r') as myfile:
        data=myfile.read().replace('\n', '')
    return data