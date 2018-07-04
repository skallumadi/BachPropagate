import itertools as it
import sys
import json
import re
import collections
import os
from utils import write_to_pickle
from utils_text import normalize_name_title

path = 'data/raw'
bipartite_path = 'data/bipartite_challenge'

# Generate BiPartites and save as Objects.

filenames = os.listdir(path)

count = 0

AllDataPidTitleBipartite = {}
AllDataPidTrackListBipartite = {}

AllDataTrackArtistBipartite = {}
AllDataTrackAlbumBipartite = {}
AllDataTrackNameBipartite = {}
AllDataAlbumNameBipartite = {}
AllDataAritstNameBipartite = {}
AllDataPidDescriptionBipartite = {}

AlbumTrackSetBipartite = {}
ArtistTrackSetBipartite = {}
AllDataAlbumTrackSetBipartite = {}
AllDataArtistTrackSetBipartite = {}

TrackIdTitle = {}
TitleTrackId = {}

TrackIdArtistName = {}
TrackIdAbumName = {}
TrackIdTrackName = {}

AlbumTrackSetBipartiteNorm = {}
ArtistTrackSetBipartiteNorm = {}

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
            pname = playlist['name']
            normpName = normalize_name_title(pname).strip()
            if normpName == '':
                normpName = 'emptyTitle'
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

                TrackIdTitle.setdefault(
                    trackId, []).append(normpName)  # --Done
                TitleTrackId.setdefault(
                    normpName, []).append(trackId)  # --Done

                TrackIdArtistName[trackId] = trackArtistName  # --meta2
                TrackIdAbumName[trackId] = trackAlbumName  # --meta2
                TrackIdTrackName[trackId] = trackName  # --meta2

            AllDataPidTitleBipartite[playlistId] = playlistTitle
            AllDataPidTrackListBipartite[playlistId] = playlistTracks
            if 'description' in playlist:
                AllDataPidDescriptionBipartite[playlistId] = playlist['description']
            count = count + 1
            if count % 10000 == 0:
                print 'processed' + str(count)


write_to_pickle(bipartite_path, 'AllDataPidTitleBipartite.pkl',
                AllDataPidTitleBipartite)
write_to_pickle(bipartite_path, 'AllDataPidTrackListBipartite.pkl',
                AllDataPidTrackListBipartite)
write_to_pickle(bipartite_path, 'AllDataAlbumTrackSetBipartite.pkl',
                AllDataAlbumTrackSetBipartite)
write_to_pickle(bipartite_path, 'AllDataArtistTrackSetBipartite.pkl',
                AllDataArtistTrackSetBipartite)
write_to_pickle(bipartite_path, 'TitleTrackId.pkl',
                TitleTrackId)
write_to_pickle(bipartite_path, 'TrackIdTitle.pkl',
                TrackIdTitle)
write_to_pickle(bipartite_path, 'TrackIdTrackName.pkl',
                TrackIdTrackName)
write_to_pickle(bipartite_path, 'TrackIdAbumName.pkl',
                TrackIdAbumName)
write_to_pickle(bipartite_path, 'TrackIdArtistName.pkl',
                TrackIdArtistName)


# todo: check if used.. or delete
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
