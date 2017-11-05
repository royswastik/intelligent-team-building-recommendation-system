__author__ = 'Swastik'
import constants
import text_extractor

def extract_publication(pub_id):
    return text_extractor.read_all_text(constants.DATA_PATH+pub_id+'.txt')