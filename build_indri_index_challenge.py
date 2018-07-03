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
