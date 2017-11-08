__author__ = 'Swastik'
import os

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

def remove_blank_files(directory):
    for filename in os.listdir(directory):
        filePath = os.path.join(directory, filename)
        text = read_all_text(filePath)
        if text.strip() == '':
            os.remove(filePath)
    pass

def write_to_file(text, filepath):
    with open(filepath, "w") as text_file:
        text_file.write(text)