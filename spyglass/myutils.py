"""
Utilities for spyglass
"""
import math
import numpy as np
import pandas
import pyfaidx
import scipy.stats
import seqlogo
import sys

# Global vars
nucs = {"A": 0, "C": 1, "G": 2, "T": 3}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def ERROR(msg):
	"""
	Print an error message and die

	Parameters
	----------
	msg : str
	   Error message to print
	"""
	sys.stderr.write(bcolors.FAIL + "[ERROR]: " + bcolors.ENDC + "{msg}\n".format(msg=msg) )
	sys.exit(1)

def RetrieveFastaSeq(fasta, chromosome, start, end):
	"""
	Helper for LoadSeqs; find a specific region of given genome

	Parameters
	----------
	p1 : name
	   p1 description
	p1 : name
	   p1 description
	"""
	# CODE HERE
	
def LoadSeqs(fasta, peakBed, bgBed):
	"""
	Return a list of peak sequences specified in peaks file and a list of bg seqs if specified or randomly generated bg seqs

	Parameters
	----------
	p1 : name
	   p1 description
	p1 : name
	   p1 description
	"""
	# CODE HERE

# -------------------- Score sequences --------------------
def ScoreSeq(pwm, seq):
	"""
	Description

	Parameters
	----------
	p1 : name
	   p1 description
	"""
	# CODE HERE
	
def ReverseComplement(seq):
	"""
	Description

	Parameters
	----------
	p1 : name
	   p1 description
	p1 : name
	   p1 description
	"""
	# CODE HERE

def FindMaxScore(pwm, seq):
	"""
	Description

	Parameters
	----------
	p1 : name
	   p1 description
	p1 : name
	   p1 description
	"""
	# CODE HERE

# -------------------- Set the threshold --------------------

def ComputeNucFreqs(fasta, seq):
	"""
	Return freqs of ACGT

	Parameters
	----------
	fasta : str
	   p1 description
	seq : str
	   p1 description
	"""
	# CODE HERE
	
def RandomSequence(n, seq):
	"""
	Description

	Parameters
	----------
	p1 : name
	   p1 description
	p1 : name
	   p1 description
	"""
	# CODE HERE
	
def GetThreshold(pvalue):
	"""
	Score threshold for p-value

	Parameters
	----------
	pvalue : float
	   p1 description
	p1 : name
	   p1 description
	"""
	# CODE HERE
	
# -------------------- Test Enrichment --------------------	
def ComputeEnrichment(peak_total, peak_motif, bg_total, bg_motif):
	"""
	Description

	Parameters
	----------
	peak_total : int
	   number of peaks
	peak_motif : int
	   number of peaks matching motif 
	bg_total : int
		number of background sequences
	bg_motif : int
		number of background sequences matching motif
	"""
	# CODE HERE
