#reference http://had00b.blogspot.com/2013/07/random-subset-in-mapreduce.html

import sys, random

k = int(sys.argv[1])

line = sys.stdin.readline()
while line:
  # Aggregate Mappers information
  less_count, upto_count = 0, 0
  (j, r, x) = line.split('t', 2)
  while float(r) == -1:
    l, u = x.split('t', 1)
    less_count, upto_count = less_count + int(l), upto_count + int(u)
    (j, r, x) = sys.stdin.readline().split('t', 2)
  n = upto_count - less_count # elements in bucket j

  # Proceed with one of the three cases
  if upto_count <= k: # in this case output the whole bucket
    print x,
    for i in range(n-1):
      (j, r, x) = sys.stdin.readline().split('t', 2)
      print x,

  elif less_count >= k: # in this case do not output anything
    for i in range(n-1):
      line = sys.stdin.readline()

  else: # run reservoir sampling picking (k-less_count) elements
    k = k - less_count
    S = [x]
    for i in range(1,n):
      (j, r, x) = sys.stdin.readline().split('t', 2)
      if i < k:
        S.append(x)
      else:
        r = random.randint(0,i-1)
        if r < k: S[r] = x
    print ''.join(S),

  line = sys.stdin.readline()
