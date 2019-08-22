#!/usr/bin/python3
import sys
from operator import itemgetter
from itertools import groupby
from itertools import islice

def read(file):
    """ read the source file, and return iterator for dictionary
	Input format: key \t value
	Output format: dictionary with format as: {key:key1, val:val1}

	"""
    for line in islice(file, 1, None):#ignore the first row which is the headers of columns
        items = line.strip().split(',')
        yield {'key':"{},{},{}".format(items[3],items[0],items[11]),'val':items[11]}#reformat the mutikey as the output key

def video_mapper():
	"""this mapper return the stdout with trending video information
	Output format:	key \t value pair

	"""
	for key, group in groupby(read(sys.stdin),itemgetter('key')):#grouping the data by the reformatted key
   		print("{}\t{}".format(key, list(group)[0]['val']))#stdout data with format: 'category,video_id,country	country'

if __name__ == "__main__":
    video_mapper()