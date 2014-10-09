#! /usr/bin/env python

import argparse
import os
# STAR module
import star
# Hrrmmmm Do I want to go this route now?
import ConfigParser


__author__ = "Gene Blanchard"
__email__ = "me@geneblanchard.com"

'''
DOC:

See README.md

'''


def main():

	# Calculate 90% of CPU
	cpu_default = int(cpu_count() * .90)

	# Get command line arguments
	parser = argparse.ArgumentParser(description='MAX IS RAD!')
	
	# Forward read
	parser.add_argument('-f', '--forward', dest='forward', help='The forward read file', required=True)
	# Reverse read
	parser.add_argument('-r', '--reverse', dest='reverse', help='The reverse read file')
	# Output directory
	parser.add_argument('-o', '--output', dest='output', help='The output directory')
	# Config file for pipeline
	parser.add_argument('-c', '--config', dest='config', help='The config file containing parameters for downstream analysis')
	# Threads
	parser.add_argument("-t", "--threads", dest="processors", default=cpu_default, help="The number of processors to use. Default is 90 percent of available. i.e. This machine's DEFAULT = %s " % cpu_default)

	# Parse arguments
	args = parser.parse_args()
	
	# Set arguments 
	forward_path = os.path.abspath(args.forward)
	reverse_path = os.path.abspath(args.reverse)
	output_dir = os.path.abspath(args.output)
	config_file = os.path.abspath(args.config)
	threads = arga.threads
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
