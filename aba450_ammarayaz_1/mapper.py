#reference http://had00b.blogspot.com/2013/07/random-subset-in-mapreduce.html
import sys, random

l = int(sys.argv[1])
S = [0 for j in range(l)]

for x in sys.stdin:
  (j,r) = (random.randint(0,l-1), random.random())
  S[j] += 1
  print '%dt%ft%s' % (j, r, x),

for j in range(l): # compute partial sums
  prev = 0 if j == 0 else S[j-1]
  S[j] += prev # number of elements with key less than j
  print '%dt-1t%dt%d' % (j, prev, S[j]) # secondary key is -1 so reducer gets this first
