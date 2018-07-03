import itertools as it
import sys
import json
import re
import collections
import os
from utils import write_to_pickle

path = '../data/raw'
bipartite_path = '..data/bipartite_train'

# Generate BiPartites and save as Objects.

filenames = os.listdir(path)

count = 0

AllDataPidTitleBipartite = {}
AllDataPidTrackListBipartite = {}
AllDataAlbumTrackSetBipartite = {}
AllDataArtistTrackSetBipartite = {}
AllDataTrackArtistBipartite = {}
AllDataTrackAlbumBipartite = {}
AllDataTrackNameBipartite = {}
AllDataAlbumNameBipartite = {}
AllDataAritstNameBipartite = {}
AllDataPidDescriptionBipartite = {}

# read data in
for filename in sorted(filenames):
    if filename.startswith("mpd.slice.") and filename.endswith(".json"):
        fullpath = os.sep.join((path, filename))
        f = open(fullpath)
        js = f.read()
        f.close()
        mpd_slice = json.loads(js)
        for playlist in mpd_slice['playlists']:
            playlistId = str(playlist['pid'])
            playlistTracks = []
            playlistTitle = playlist['name']
            for track in playlist['tracks']:
                trackId = track['track_uri']
                trackName = track['track_name']
                trackArtistId = track['artist_uri']
                trackArtistName = track['artist_name']
                trackAlbumId = track['album_uri']
                trackAlbumName = track['album_name']
                playlistTracks.append(trackId)
                AllDataAlbumTrackSetBipartite.setdefault(
                    trackAlbumId, []).append(trackId)
                AllDataArtistTrackSetBipartite.setdefault(
                    trackArtistId, []).append(trackId)
                AllDataTrackArtistBipartite[trackId] = trackArtistId
                AllDataTrackAlbumBipartite[trackId] = trackAlbumId
                AllDataTrackNameBipartite[trackId] = trackName
                AllDataAlbumNameBipartite[trackAlbumId] = trackAlbumName
                AllDataAritstNameBipartite[trackArtistId] = trackArtistName
            AllDataPidTitleBipartite[playlistId] = playlistTitle
            AllDataPidTrackListBipartite[playlistId] = playlistTracks
            if 'description' in playlist:
                AllDataPidDescriptionBipartite[playlistId] = playlist['description']
            count = count + 1
            if count % 10000 == 0:
                print 'processed' + str(count)


write_to_pickle(bipartite_path, 'AllDataArtistTrackSetBipartite.pkl',
                AllDataArtistTrackSetBipartite)
write_to_pickle(bipartite_path, 'AllDataTrackArtistBipartite.pkl',
                AllDataTrackArtistBipartite)
write_to_pickle(bipartite_path, 'AllDataTrackAlbumBipartite.pkl',
                AllDataTrackAlbumBipartite)
write_to_pickle(bipartite_path, 'AllDataTrackNameBipartite.pkl',
                AllDataTrackNameBipartite)
write_to_pickle(bipartite_path, 'AllDataAlbumNameBipartite.pkl',
                AllDataAlbumNameBipartite)
write_to_pickle(bipartite_path, 'AllDataAritstNameBipartite.pkl',
                AllDataAritstNameBipartite)
write_to_pickle(bipartite_path, 'AllDataPidDescriptionBipartite.pkl',
                AllDataPidDescriptionBipartite)
