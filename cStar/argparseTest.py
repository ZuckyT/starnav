import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="Makes output more detailed", type=int)
args = parser.parse_args()
if( args.verbosity):
	print("Verbose Now")
