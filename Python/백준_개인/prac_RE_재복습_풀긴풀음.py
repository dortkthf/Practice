def solution(citations):
  citations.sort(reverse=True)
  for k,v in enumerate(citations,start=1):
    if k<=v:
      continue
    else:
      return k-1 
  return k

def solution(citations):
  citations.sort(reverse=True)
  length = len(citations)
  for i in range(length):
    if i+1<=citations[i]:
      continue
    else:
      return i
  return i+1