#! /usr/bin/env python

import argparse
import os
import ConfigParser
from multiprocessing import cpu_count
import errno

__author__ = "Gene Blanchard"
__email__ = "me@geneblanchard.com"

'''
DOC:

See README.md

'''

def star_command_builder(config, read_1, read_2, threads, output):
	# Read the Star parameters, set defaults if none are listed
	index = config.get('star', 'genome_dir')
	clip5p = config.get('star', 'clip5pNbases')	
	repeat = config.get('star', 'outFilterMultimapNmax')
	
	# Base string
	command_string = "STAR"
	# Index/Genome Location
	command_string += " --genomeDir {}".format(index)
	# Number of bases to clip
	command_string += "--clip5pNbases {}".format(clip5p)
	# outFilterMultimapNmax
	command_string += " --outFilterMultimapNmax {}".format(repeat)
	# Buffer Limit 
	command_string += " --limitIObufferSize 2750000000"
	# Input files NOTE: Will make future change for non-paired data
	command_string += " --readFilesIn {} {}".format(read_1, read_2)
	# Gunzip only if gz'ed
	if read_1.endswith('.gz'):
		command_string += " --readFilesCommand gunzip -c"
	# outReadsUnmapped
	command_string += " --outReadsUnmapped Fastx"
	# Number of processors
	command_string += " --runThreadN {}".format(threads)
	# Output string
	command_string += " --outFileNamePrefix {}".format(output)
	# end of line
	command_string += ";\n"

	print command_string
	return command_string

def rsem_command_builder(input_file, annotation, output, threads):
	rsem_command = 'rsem-calculate-expression -p {} --no-bam-output {} {} {}'.format(threads, input_file, annotation, output)

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
	threads = args.processors

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
		os.makedirs(output_dir)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

	# Read the config file
	config = ConfigParser.RawConfigParser()
	config.read(config_file)

	# STAR
	star_command_builder(config, forward_path, reverse_path, threads, output_dir)

if __name__ == '__main__':
	main()
