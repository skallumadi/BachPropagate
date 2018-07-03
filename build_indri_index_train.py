import pickle
import os
from utils import write_index

# get title bipartite
bipartite_path = 'data/bipartite_challenge'
index_path = 'data/indexes_challenge'

PidTitleBipartite = pickle.load(
    open(os.sep.join(bipartite_path, 'AllDataPidTitleBipartite.pkl'), 'rb'))

PidTrackListBipartite = pickle.load(
    open(os.sep.join(bipartite_path, 'PidTrackListBipartite.pkl'), 'rb'))

# buildIndexPidAsDocTracksAsTerms

index_name = 'All1MIndexPidAsDocTracksAsTerms.txt'

pidDocs = []
for pid in PidTitleBipartite:
    trackList = PidTrackListBipartite[pid]
    pidDocs.append(entry(str(pid), ' '.join(
        [item.replace('spotify:track:', '') for item in trackList])))

write_index(index_path, index_name, pidDocs)


# train data
bipartite_path = 'data/bipartite_train'
index_path = 'data/indexes_train'

AlbumTrackSetBipartite750 = pickle.load(
    open(os.sep.join(bipartite_path, 'AlbumTrackSetBipartite750.pkl'), 'rb'))

index_name = '1MIndexAlbumAsDocNonNormTracksListAsTerms.txt'
index_name_norm = '1MIndexAlbumAsDocNonNormTracksListAsTerms.txt'

albumDocsNormalbumDoc = []
albumDocsNonNorm = []
for albumid, tracks in AlbumTrackSetBipartite750.items():
    normTracks = list(set(tracks))
    albumDocsNonNorm.append(entry(albumid.strip(), ' '.join(
        list([item.replace('spotify:track:', '') for item in tracks]))))
    albumDocsNorm.append(entry(albumid.strip(), ' '.join(
        list([item.replace('spotify:track:', '') for item in normTracks]))))


write_index(index_path, index_name, albumDocsNonNorm)
write_index(index_path, index_name_norm, albumDocsNorm)
