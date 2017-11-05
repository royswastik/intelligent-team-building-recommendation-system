import sys
import os
import shutil
import constants

paper_author_aff = os.path.join(constants.DATA_PATH,'paper_author_affiliations.txt')

def compileallpapers():
    folderpath = os.path.join(constants.DATA_PATH,"authors_text")
    if os.path.exists(folderpath):
        shutil.rmtree(folderpath)
    with open(paper_author_aff) as infile:
        next(infile)
        for line in infile:
            if (line != '\n'):
                entry = line.split('\t')
                paperid = entry[0]
                authorid = entry[1]
                paperlocation = os.path.join(constants.DATA_PATH, "papers_text",paperid+".txt")
                authordir = os.path.join(constants.DATA_PATH,"authors_text")
                authortext = os.path.join(constants.DATA_PATH,authordir,authorid+".txt")
                # authordirectory = os.path.dirname(authordir)
                if not os.path.exists(authordir):
                    os.makedirs(authordir)
                authorfileid = open(authortext,'a+')
                if os.path.exists(paperlocation):
                    with open(paperlocation) as paperfile:
                        for line in paperfile:
                            authorfileid.write(line)
                authorfileid.close()
    pass


if __name__ == "__main__": compileallpapers()

