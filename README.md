# contigFinder

suite of python scripts to get the start and end points of each contig in a sorted list

Contents:

- getContigs.py: gets the endpoints of each contig in a given sorted list
- getContigs_evaluation.py performs a unit test on hard-coded lists and generates lists of lengths 10, 100, and 1000 and runs getContigs() on each of them. Tracks performance time and the contig endpoints. In the evaluation at the time of writing, I also output the number of contigs in each list, for possible downstream analysis (e.g. is this number of contigs what we expect, given the way we're sampling the numbers)
