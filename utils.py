import pickle

# IO stuff


def write_to_pickle(path, filename, data):
    """
    write to data to pickle file
    """
    fullpath = os.sep.join((path, filename))
    fileObj = open(fullpath, 'w')
    pickle.dump(data, fileObj)
    fileObj.close()


import codecs

# indri stuff


def entry(docId, docContent):
    entry = '<DOC>\n<DOCNO>' + docId + '</DOCNO>\n<TEXT>' + \
        docContent + '\n</TEXT>\n</DOC>'
    return entry


def writeIndexToFile(indexDocsList, writePath):
    count = 0
    errors = []
    with codecs.open(writePath, "w", encoding='utf-8') as f:
        for line in indexDocsList:
            try:
                f.write(line + "\n")
                count = count + 1
            except:
                errors.append(line)
    print count
    return errors
