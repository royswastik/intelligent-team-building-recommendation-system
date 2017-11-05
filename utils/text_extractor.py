__author__ = 'Swastik'

def read_all_text(filepath):
    data = ''
    with open(filepath, 'r') as myfile:
        data=myfile.read().replace('\n', '')
    return data

def extract_corrected_text(filepath):
    """For papers"""
    text = read_all_text(filepath)
    replaced = text.replace("- ","")
    return replaced

def write_to_file(text, filepath):
    with open(filepath, "w") as text_file:
        text_file.write(text)