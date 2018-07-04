#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

stop = 'stopwords.txt'
emojiSynonyms = 'emojiWords.txt'
stopList = []
emojiMap = {}
emojis = []
f = codecs.open(stop, 'r', encoding='utf-8')

for line in f.readlines():
    stopList.append(line.strip())

f = codecs.open(emojiSynonyms, 'r', encoding='utf-8')
for line in f.readlines():
    emoji, meaning = line.strip().split()
    emojiMap[emoji.strip()] = ' '.join(meaning.strip().split(','))
    emojis.append(emoji.strip())


def normalize_dates(title):
    fullDecades = ['1930', '1940', '1950', '1960',
                   '1970', '1980', '1990', '2000', '2010']
    truncDecades = ['30', '40', '50', '60', '70', '80', '90', '00', '10']
    year = ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
            '2009', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
    truncYear = ['02', '03', '04', '05', '06', '07', '08',
                 '09', '11', '12', '13', '14', '15', '16', '17']
    seasons = ['spring', 'summer', 'fall',
               'winter', 'sommer', 'autumn', 'verano']
    months = ['january', 'jan', 'february', 'feb', 'march', 'april', 'may', 'june', 'july',
              'august', 'aug', 'spetember', 'sep', 'october', 'oct', 'novemeber', 'nov', 'december', 'dec']
    monthPairs = [('january', 'jan'), ('february', 'feb'), ('august', 'aug'), ('september', 'sept'),
                  ('september', 'sep'), ('october', 'oct'), ('november', 'nov'), ('december', 'dec')]

    title = title.lower().strip()
    for decade in fullDecades:
        if decade in title:
            newTitle = ''
            for word in title.split():
                if decade in word:
                    word = word.replace(decade + "'", decade)
                    word = word.replace(decade + "s", decade)
                    word = word.replace(decade, ' ' + decade + 's ')
                newTitle = newTitle + ' ' + word
            # print title+'------'+newTitle
            title = newTitle.strip()
    for truncDecade in truncDecades:
        if truncDecade in title and ('19' + truncDecade not in title) and ('20' + truncDecade not in title):
            newTitle = ''
            for word in title.split():
                if truncDecade + "'" in word or truncDecade + "s" in word or truncDecade + u"´s" in word or truncDecade + "'s" in word or truncDecade + " s " in word or truncDecade + "ies" in word:
                    word = word.replace(truncDecade + "'", truncDecade)
                    word = word.replace(truncDecade + "s", truncDecade)
                    word = word.replace(truncDecade + " s", truncDecade)
                    word = word.replace(truncDecade + u"´s", truncDecade)
                    word = word.replace(truncDecade + "ies", truncDecade)
                    if truncDecade in truncDecades[:7]:
                        century = '19'
                    else:
                        century = '20'
                    word = word.replace(
                        truncDecade, ' ' + century + truncDecade + 's ')
                newTitle = newTitle + ' ' + word
            title = newTitle.strip()
    if title.strip() in ['70-80', '70,80,90', '90/00', '70 80 90', '90 00', '80 90', '80-90', '90-00', '60-70', '70 80']:
        for truncDecade in truncDecades:
            if truncDecade in truncDecades[:7]:
                century = '19'
            else:
                century = '20'
            title = title.replace(
                truncDecade, ' ' + century + truncDecade + 's ')
    title = title.strip()
    for yr in year:
        if yr in title:
            title = title.replace(yr, ' ' + yr + ' ')
    for yr in truncYear:
        if yr in title and '20' + yr not in title:
            if "'" + yr in title:
                # print title
                title = title.replace("'" + yr, ' 20' + yr + ' ')
                # print title
            if yr + "'" in title:
                # print title
                title = title.replace(yr + "'", ' 20' + yr + ' ')
                # print title
            if '2k' + yr in title or '2K' + yr in title:
                # print title
                title = title.replace('2k' + yr, ' 20' + yr + ' ')
                # print title
            if '-' + yr in title:
                # print title
                title = title.replace('-' + yr, ' 20' + yr + ' ')
                # print title
        if yr in title and '20' + yr not in title:
            for season in seasons:
                if season in title:
                    # print title
                    title = title.replace(yr, ' 20' + yr + ' ')
                    # print title
            for month in months:
                if month in title and '20' + yr not in title:
                    # print title
                    title = title.replace(yr, ' 20' + yr + ' ')
                    # print '-'+title
    for month, shortMonth in monthPairs:
        newTitle = ''
        if shortMonth in title and month not in title:
            # print title
            for word in title.split():
                if shortMonth == word:
                    newTitle = newTitle + ' ' + month
                else:
                    newTitle = newTitle + ' ' + word
            title = newTitle
            # print '-'+title
    title = title.strip()
    title = ' '.join(title.split())
    return title


def handle_emojis(title):
    for emo in emojis:
        if emo in title:
            title = title.replace(emo, ' ')
            title = title + ' ' + emojiMap[emo] + ' '

    title = title.replace(u'\U0001f3fc', '')
    title = title.replace(u'\U0001f3fd', '')
    title = title.replace(u'\U0001f3fb', '')
    title = title.replace(u'\U0001f3fe', '')
    title = title.replace(u'\u200d', '')
    title = title.replace(u'\ufe0f', '')
    title = title.replace(u'oshrug', 'shrug')
    title = title.replace(u'\ufffd', '')
    title = title.replace(u'\U0001f37b', '')
    title = title.replace(u'\u200d', '')
    title = title.replace(u'\u2640', '')
    title = title.replace(u'\u2642', '')
    title = title.replace(u'\U0001f3b6', '')
    title = title.replace(u'\u2728', '')
    title = title.replace(u'\U0001f449', '')
    title = title.replace(u'\U0001f3ff', '')
    title = title.replace(u'\U0001f38a', '')
    title = title.replace(u'\U0001f445', '')
    title = title.replace(u'\U0001f608', '')
    title = title.replace(u'\U0001f381', '')
    title = title.replace(u'\U0001f60f', '')
    title = title.replace(u'\U0001f4a8', '')
    title = title.replace(u'�', '')
    title = title.replace('<3', ' heart love ')
    title = title.replace(':)', ' smile happy ')
    title = title.replace(';)', ' smirk happy ')
    title = title.replace(':-)', ' smile happy ')
    title = title.replace(': )', ' smile happy ')
    title = title.replace(u'😋', ' smile happy ')
    title = title.replace(u'\u263a\ufe0f', ' smile happy ')
    title = title.replace('r&b', ' randb ')
    title = title.replace('r & b', ' randb ')
    title = title.replace('rnb', ' randb ')
    title = title.replace(u'•', ' ')
    title = title.replace(u'\u263a\ufe0f', ' death poison ')
    title = title.replace(u'\u2615\ufe0f', ' coffee tea morning ')
    title = title.replace(u'💩', ' poop ')
    title = title.strip()
    title = ' '.join(title.split())
    return title


import re


def normalize_name_title(name):
    name = name.lower()
    name = NormalizeDates(name)
    name = handleEmojis(name)
    name = name.replace('happysmile', 'happy smile')
    name = re.sub(r"[.,\/#\'?\&\-!$%\^\*;:{}=\_`~()@]", ' ', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def normalize_name(name):
    name = name.lower()
    name = re.sub(r"[.,\/#\'?\&\-!$%\^\*;:{}=\_`~()@]", ' ', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


import nltk


def title_plus_bigrams(title):
    bigrm = list(nltk.bigrams(title.split()))
    bis = ''
    for x1, x2 in bigrm:
        bis = bis + ' ' + x1 + x2
    return title + ' ' + bis.strip()
