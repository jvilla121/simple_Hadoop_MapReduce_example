#!/usr/bin/env python
import sys

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace & lowercase all
    line = line.strip().lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format & removes punctuation + omits stopwords
    from sklearn.feature_extraction import stop_words
    stopwords = set(stop_words.ENGLISH_STOP_WORDS)
    stops = set([';','.',',',':','?','!'])
    for word in words:
        if word not in stopwords and word not in stops:
                print '%s\t%s' % (word, "1")
