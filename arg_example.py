# import argparse

# parser = argparse.ArgumentParser(description='Process some integers.')

# # parser.add_argument('integers', metavar='N', type=int, nargs='+',
# #                     help='an integer for the accumulator')

# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

# parser.add_argument('--data', type=str, default='/this/is/a/test/data/', 
#                         help='data directory for training')



# args = parser.parse_args()
# # print(args.accumulate(args.integers))
# print(args.accumulate(args.data))

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
args = parser.parse_args()

print(args.file.readlines())



# Load old saved model
# Load new saved model
# Training on model
# Testing on model