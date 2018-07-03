import pickle


def write_to_pickle(path, filename, data):
    """
    write to data to pickle file
    """
    fullpath = os.sep.join((path, filename))
    fileObj = open(fullpath, 'w')
    pickle.dump(data, fileObj)
    fileObj.close()
