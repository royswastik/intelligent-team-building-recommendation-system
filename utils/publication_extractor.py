import os

__author__ = 'Swastik'
import constants
import utils.text_extractor

def extract_publication(pub_id):
    return utils.text_extractor.read_all_text(os.path.join(constants.DATA_PATH,'papers_text',pub_id+'.txt'))

def extract_corrected_text(pub_id):
    text = extract_publication(pub_id)
    replaced = text.replace("- ","")
    return replaced


