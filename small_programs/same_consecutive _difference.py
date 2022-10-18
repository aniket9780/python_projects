from collections import deque
def solve(N, K):
   if N == 1:
      return 'No number'
   queue = deque(list(range(1, 10)))
   for n in range(N - 1):
      len_queue = len(queue)
      for j in range(len_queue):
         num = queue.popleft()
         lsd = num % 10
         if lsd - K >= 0:
            queue.append( num * 10 + lsd - K )
         if K and lsd + K <= 9:
            queue.append( num * 10 + lsd + K )
   return list(queue)

N = 10
K = 2
print(solve(N, K))
