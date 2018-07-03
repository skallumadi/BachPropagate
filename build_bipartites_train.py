import itertools as it
import sys
import json
import re
import collections
import os
from utils import write_to_pickle

path = 'data/raw'
bipartite_path = 'data/bipartite_challenge'

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


write_to_pickle(bipartite_path, 'AllDataPidTitleBipartite.pkl',
                AllDataPidTitleBipartite)
write_to_pickle(bipartite_path, 'AllDataPidTrackListBipartite.pkl',
                AllDataPidTrackListBipartite)

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


bipartite_path = 'data/bipartite_train'
filenames = os.listdir(path)

count = 0

pid750 = []
AlbumTrackSetBipartite750 = {}
ArtistTrackSetBipartite750 = {}

for filename in sorted(filenames[:750]):
    if filename.startswith("mpd.slice.") and filename.endswith(".json"):
        fullpath = os.sep.join((path, filename))
        f = open(fullpath)
        js = f.read()
        f.close()
        mpd_slice = json.loads(js)
        for playlist in mpd_slice['playlists']:
            playlistId = str(playlist['pid'])
            pid750.append(playlistId)

            for track in playlist['tracks']:
                trackId = track['track_uri']
                trackName = track['track_name']
                trackArtistId = track['artist_uri']
                trackArtistName = track['artist_name']
                trackAlbumId = track['album_uri']
                trackAlbumName = track['album_name']

                AlbumTrackSetBipartite750.setdefault(
                    trackAlbumId, []).append(trackId)
                ArtistTrackSetBipartite750.setdefault(
                    trackArtistId, []).append(trackId)
            count = count + 1
            if count % 10000 == 0:
                print 'processed' + str(count)

write_to_pickle(bipartite_path, 'AlbumTrackSetBipartite750.pkl',
                AlbumTrackSetBipartite750)
write_to_pickle(bipartite_path, 'ArtistTrackSetBipartite750.pkl',
                ArtistTrackSetBipartite750)


# with normalized text

filenames = os.listdir(path)

count = 0

pid750 = []

TrackIdTitle750 = {}
TitleTrackId750 = {}

TrackIdArtistName750 = {}
TrackIdAbumName750 = {}
TrackIdTrackName750 = {}

AlbumTrackSetBipartite750 = {}
ArtistTrackSetBipartite750 = {}

for filename in filenames:
    if filename.startswith("mpd.slice.") and filename.endswith(".json"):
        fullpath = os.sep.join((path, filename))
        f = open(fullpath)
        js = f.read()
        f.close()
        mpd_slice = json.loads(js)
        for playlist in mpd_slice['playlists']:
            playlistId = str(playlist['pid'])
            pid750.append(playlistId)
            pname = playlist['name']
            normpName = normalize_nameTitle(pname).strip()
            if normpName == '':
                normpName = 'emptyTitle'
            for track in playlist['tracks']:
                trackId = track['track_uri']
                trackName = track['track_name']
                trackArtistId = track['artist_uri']
                trackArtistName = track['artist_name']
                trackAlbumId = track['album_uri']
                trackAlbumName = track['album_name']

                TrackIdTitle750.setdefault(
                    trackId, []).append(normpName)  # --Done
                TitleTrackId750.setdefault(
                    normpName, []).append(trackId)  # --Done

                TrackIdArtistName750[trackId] = trackArtistName  # --meta2
                TrackIdAbumName750[trackId] = trackAlbumName  # --meta2
                TrackIdTrackName750[trackId] = trackName  # --meta2

                AlbumTrackSetBipartite750.setdefault(
                    trackAlbumId, []).append(trackId)  # done
                ArtistTrackSetBipartite750.setdefault(
                    trackArtistId, []).append(trackId)  # done

            count = count + 1
            if count % 10000 == 0:
                print 'processed' + str(count)
