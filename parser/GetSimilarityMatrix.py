import os
import sys
import difflib
sys.path.insert(0, r'C:\Users\soumy\Desktop\SML\intelligent-team-building-recommendation-system-master\intelligent-team-building-recommendation-system-master')

import constants

author_id = os.path.join(constants.DATA_PATH,'author_ids.txt')
author_collab = os.path.join(constants.DATA_PATH,'networks\\author_collaboration_network.txt')
author_collab_clean = os.path.join(constants.DATA_PATH,'networks\\author_collaboration_network_clean.txt')
author_collab_map = os.path.join(constants.DATA_PATH,'networks\\author_collaboration_map.txt')
author_cite_map = os.path.join(constants.DATA_PATH,'networks\\author_cite_map.txt')
paper_cite_map = os.path.join(constants.DATA_PATH,'networks\\paper_cite_map.txt')
author_cite = os.path.join(constants.DATA_PATH,'networks\\author_citation_network.txt')
author_cite_clean = os.path.join(constants.DATA_PATH, 'networks\\author_citation_network_clean.txt')
paper_author = os.path.join(constants.DATA_PATH,'paper_author_affiliations.txt')
paper_cite = os.path.join(constants.DATA_PATH,'networks\\paper_citation_network.txt')
collaboration_weight = constants.collaborate_weight
citation_weight = constants.citation_weight
paper_citation_weight = constants.paper_citation_weight

def getAuthorIDNameMap():
    with open(author_id, encoding="utf8") as infile:
        authormap = {}
        authorarray = []
        for line in infile:
            if line.strip():
                value, key = line.split("\t")
                key = key.strip('\n')
                authorarray.append(key)
                authormap[key] = value

    return value, authorarray, authormap

def getPaperAuthorMap():
    paperauthormap={}
    with open(paper_author) as infile:
        next(infile)
        for line in infile:
            if (line != '\n'):
                entry = line.split('\t')
                paperid = entry[0]
                authorid = entry[1]
                if (paperid in paperauthormap):
                    (paperauthormap.get(paperid)).append(authorid)
                else:
                    paperauthormap[paperid] = []
                    (paperauthormap.get(paperid)).append(authorid)

    return paperauthormap


def createSimilarityMatrix():
    number_authors, authorarray, authormap = getAuthorIDNameMap()
    #cleanFile(author_collab,authormap,authorarray,author_collab_clean)
    #cleanFile(author_cite,authormap,authorarray,author_cite_clean)
    authorcollabmap = updateSimilarityMatrix(author_collab_clean,authormap,authorarray,collaboration_weight)
    fileid = open(author_collab_map, 'w')
    for k,v in authorcollabmap.items():
        fileid.write(str(k) + "==>" + str(v))
        fileid.write("\n")
    fileid.close()

    authorcitemap = updateSimilarityMatrix(author_collab_clean,authormap,authorarray,citation_weight)
    fileid = open(author_cite_map, 'w')
    for k, v in authorcitemap.items():
        fileid.write(str(k) + "==>" + str(v))
        fileid.write("\n")
    fileid.close()

    papercitemap = createPaperCiteSimilarityMatrix(paper_citation_weight)
    fileid = open(paper_cite_map, 'w')
    for k, v in papercitemap.items():
        fileid.write(str(k) + "==>" + str(v))
        fileid.write("\n")
    fileid.close()


    pass

def createPaperCiteSimilarityMatrix(weight):
    authorcollabarray = {}
    paperauthor = getPaperAuthorMap()
    with open(paper_cite, encoding="utf8") as infile:
        for line in infile:
            if line.strip():
                paper1, paper2 = line.split('==>')
                paper1 = paper1.strip()
                paper2 = paper2.strip()

                try:
                    authorlist1 = paperauthor[paper1]
                    authorlist2 = paperauthor[paper2]
                except KeyError as e:
                    pass

                for author1 in authorlist1:
                    if author1 in authorcollabarray:
                        authorstructarray = authorcollabarray.get(author1)
                        for author2 in authorlist2:
                            if author2 in authorstructarray:
                                authorstructarray[author2] = authorstructarray[author2] + weight
                            else:
                                authorstructarray[author2] = weight
                    else:
                        authorcollabarray[author1] = {}
                        for author2 in authorlist2:
                            authorcollabarray[author1][author2] = weight

    return authorcollabarray



def cleanFile(filename,authormap,authorarray,newfile):
    newline = []
    with open(filename, 'r', encoding="utf8") as infile:
        for line in infile:
            if line.strip():
                author1, author2 = line.split('==>')
                name = author1.split(',',1)
                if len(name) > 1:
                    name[1] = name[1].strip()
                    author1new = name[0] + ',' + name[1]
                name = author2.split(',',1)
                if len(name) > 1:
                    name[0] = name[0].strip()
                    name[1] = name[1].strip()
                    author2new = name[0] + ',' + name[1]
                try:
                    first = (int)(authormap[author1new])
                except KeyError as e:
                    closematch = difflib.get_close_matches(e.args[0],authorarray,1,0.6)
                    if(len(closematch)>0):
                        author1new = closematch[0]
                    pass
                try:
                    second = (int)(authormap[author2new])
                except KeyError as e:
                    closematch = difflib.get_close_matches(e.args[0], authorarray, 1, 0.6)
                    if (len(closematch) > 0):
                        author2new = closematch[0]
                    pass
                updatedline = line.replace(author1,author1new).replace(author2,author2new)+"\n"
                newline.append(updatedline)


    with open(newfile,'w',encoding="utf8") as infile:
        for line in newline:
            infile.write(line)

    pass


def updateSimilarityMatrix(filename,authormap,authorarray,weight):

    authorcollabarray = {}
    with open(filename, encoding="utf8") as infile:
        for line in infile:
            if line.strip():
                author1, author2 = line.split('==>')
                name = author1.split(',',1)
                if len(name) > 1:
                    name[1] = name[1].strip()
                    author1 = name[0] + ',' + name[1]
                name = author2.split(',',1)
                if len(name) > 1:
                    name[0] = name[0].strip()
                    name[1] = name[1].strip()
                    author2 = name[0] + ',' + name[1]
                    first = second = -1
                try:
                    first = (int)(authormap[author1])
                except KeyError as e:
                    closematch = difflib.get_close_matches(e.args[0],authorarray,1,0.6)
                    if(len(closematch)>0):
                        first = (int)(authormap[closematch[0]])
                    pass
                try:
                    second = (int)(authormap[author2])
                except KeyError as e:
                    closematch = difflib.get_close_matches(e.args[0], authorarray, 1, 0.6)
                    if (len(closematch) > 0):
                        second = (int)(authormap[closematch[0]])
                    pass
                if first != -1 and second != -1:
                    if first in authorcollabarray:
                        authorstructarray = authorcollabarray.get(first)
                        if second in authorstructarray:
                            authorstructarray[second] = authorstructarray[second] + weight
                        else:
                            authorstructarray[second] = weight
                    else:
                        authorcollabarray[first] = {}
                        authorcollabarray[first][second] = weight

    return authorcollabarray
if __name__ == "__main__": createSimilarityMatrix()