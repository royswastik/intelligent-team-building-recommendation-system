import sys
import _system_path
import os
import shutil

paper_author_aff = '..\Resources'+'\\paper_author_affiliations.txt'

def compileallpapers():
    folderpath = "..\\Resources\\authors_text\\"
    if os.path.exists(folderpath):
        shutil.rmtree(folderpath)
    with open(paper_author_aff) as infile:
        next(infile)
        for line in infile:
            if (line != '\n'):
                entry = line.split('\t')
                paperid = entry[0]
                authorid = entry[1]
                paperlocation = "..\\Resources\\papers_text\\"+paperid+".txt"
                authordir = "..\\Resources\\authors_text\\"
                authortext = authordir+authorid+".txt"
                authordirectory = os.path.dirname(authordir)
                if not os.path.exists(authordirectory):
                    os.makedirs(authordirectory)
                authorfileid = open(authortext,'a+')
                if os.path.exists(paperlocation):
                    with open(paperlocation) as paperfile:
                        for line in paperfile:
                            authorfileid.write(line)
                authorfileid.close()
    pass


if __name__ == "__main__": compileallpapers()

