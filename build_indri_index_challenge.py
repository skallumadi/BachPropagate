#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import os
from utils import write_index
from utils_text import title_plus_bigrams

# IndPidAsDocTracksAsTerms.txt
# get title bipartite
bipartite_path = 'data/bipartite_challenge'
index_path = 'data/indexes_challenge'

PidTitleBipartite = pickle.load(
    open(os.sep.join((bipartite_path, 'AllDataPidTitleBipartite.pkl')), 'rb'))

PidTrackListBipartite = pickle.load(
    open(os.sep.join((bipartite_path, 'AllDataPidTrackListBipartite.pkl')), 'rb'))

# buildIndexPidAsDocTracksAsTerms

index_name = 'All1MIndexPidAsDocTracksAsTerms.txt'

pidDocs = []
for pid in PidTitleBipartite:
    trackList = PidTrackListBipartite[pid]
    pidDocs.append(entry(str(pid), ' '.join(
        [item.replace('spotify:track:', '') for item in trackList])))

write_index(index_path, index_name, pidDocs)

# IndAlbumAsDocNormTracksAsTerms

AllDataAlbumTrackSetBipartite = pickle.load(
    open(os.sep.join((bipartite_path, 'AllDataAlbumTrackSetBipartite.pkl')), 'rb'))

index_name_norm = '1MIndexAlbumAsDocNormTracksListAsTerms.txt'

albumDocsNorm = []
albumDocsNonNorm = []
for albumid, tracks in AllDataAlbumTrackSetBipartite.items():
    normTracks = list(set(tracks))
    albumDocsNonNorm.append(entry(albumid.strip(), ' '.join(
        list([item.replace('spotify:track:', '') for item in tracks]))))
    albumDocsNorm.append(entry(albumid.strip(), ' '.join(
        list([item.replace('spotify:track:', '') for item in normTracks]))))

write_index(index_path, index_name_norm, albumDocsNorm)

# IndTitsAsDocNormTracksAsTerms.txt
AllDataArtistTrackSetBipartite = pickle.load(
    open(os.sep.join((bipartite_path, 'AllDataArtistTrackSetBipartite.pkl')), 'rb'))

index_name_norm = '1MIndexArtistsAsDocNormTracksSetAsTerms.txt'

artistDocsNorm = []
artistDocsNonNorm = []
for albumid, tracks in AllDataArtistTrackSetBipartite.items():
    normTracks = list(set(tracks))
    artistDocsNonNorm.append(entry(albumid.strip(), ' '.join(
        list([item.replace('spotify:track:', '') for item in tracks]))))
    artistDocsNorm.append(entry(albumid.strip(), ' '.join(
        list([item.replace('spotify:track:', '') for item in normTracks]))))

write_index(index_path, index_name_norm, artistDocsNorm)


# normalized text stuff
TitleTrackId = pickle.load(
    open(os.sep.join((bipartite_path, 'TitleTrackId.pkl')), 'rb'))

index_name_norm = '1MIndexTitlesAsDocNormTracksSetAsTerms.txt'
index_name = '1MIndexTitlesAsDocNonNormTracksListAsTerms.txt'

titleDocsNorm = []
titletDocsNonNorm = []
for title, tracks in TitleTrackId.items():
    normTracks = list(set(tracks))
    titletDocsNonNorm.append(entry(title.strip(), ' '.join(
        list([item.replace('spotify:track:', '') for item in tracks]))))
    titleDocsNorm.append(entry(title.strip(), ' '.join(
        list([item.replace('spotify:track:', '') for item in normTracks]))))

write_index(index_path, index_name_norm, titleDocsNorm)
write_index(index_path, index_name, titletDocsNonNorm)


TrackIdTitle = pickle.load(
    open(os.sep.join((bipartite_path, 'TrackIdTitle.pkl')), 'rb'))

index_name = '1MIndexTracksAsDocTitlesAsTerms.txt'

trackTitleDocs = []
for trackId, titleList in TrackIdTitle.items():
    truncTrackId = trackId.replace('spotify:track:', '')
    concatTitle = ''
    for title in titleList:
        concatTitle = concatTitle + ' ' + title_plus_bigrams(title)
    trackTitleDocs.append(entry(truncTrackId.strip(), concatTitle))

write_index(index_path, index_name, trackTitleDocs)


index_name = '1MIndexTracksAsDocMeta2AsTerms.txt'
TrackIdTrackName = pickle.load(
    open(os.sep.join((bipartite_path, 'TrackIdTrackName.pkl')), 'rb'))
TrackIdAbumName = pickle.load(
    open(os.sep.join((bipartite_path, 'TrackIdAbumName.pkl')), 'rb'))
TrackIdArtistName = pickle.load(
    open(os.sep.join((bipartite_path, 'TrackIdArtistName.pkl')), 'rb'))

meta2trackDocs = []
for trackId, trackname in TrackIdTrackName.items():
    truncTrackId = trackId.replace('spotify:track:', '')
    normTrackName = normalize_nameTitle(trackname)
    normAlbumName = normalize_nameTitle(TrackIdAbumName[trackId])
    normArtistName = normalize_nameTitle(TrackIdArtistName[trackId])
    meta2trackDocs.append(
        entry(truncTrackId, normTrackName + ' ' + normAlbumName + ' ' + normArtistName))

write_index(index_path, index_name, meta2trackDocs)
