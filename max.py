#! /usr/bin/env python

import argparse
import os

__author__ = "Gene Blanchard"
__email__ = "me@geneblanchard.com"

'''
DOC:
 

'''

def main():

	# Get command line arguments
	parser = argparse.ArgumentParser(description='MAX IS RAD!')
	
	# Forward read
	parser.add_argument('-f', '--forward', dest='forward', help='The forward read file', required=True)
	# Reverse read
	parser.add_argument('-r', '--reverse', dest='reverse', help='The reverse read file')
	# Output directory
	parser.add_argument('-o', '--output', dest='output', help='The output directory')

	# Parse arguments
	args = parser.parse_args()
	
	# Set arguments 
	forward_path = os.path.abspath(args.forward)
	reverse_path = os.path.abspath(args.reverse)
	output_dir = os.path.abspath(args.output)

	# Error Checks
	ERROR = False

	# Does the forward read file exist
	if not os.path.exists(forward_path):
		ERROR = True
		print "Forward file not found"
	# Does the reverse read file exist
	if not os.path.exists(reverse_path):
		ERROR = True
		print "Reverse file not found"
	# Test write permissions of output
	try:
		os.makedirs(path)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise



if __name__ == '__main__':
	main()
