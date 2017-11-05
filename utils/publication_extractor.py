import os

__author__ = 'Swastik'
import constants
import utils.text_extractor

def extract_publication(pub_id):
    return utils.text_extractor.read_all_text(os.path.join(constants.DATA_PATH,'papers_text',pub_id+'.txt'))

def __init__():
    extract_publication()