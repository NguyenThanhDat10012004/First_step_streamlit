def distance_levenstein(token1, token2):
  arr = [[0] * (len(token1) + 1) for _ in range((len(token2) + 1))]
  for i in range(len(token1) + 1):
    arr[0][i] = i
  for i in range(len(token2) + 1):
    arr[i][0] = i
  for i in range(1, len(token2) + 1):
    for j in range(1, len(token1) + 1):
      if token1[j - 1] == token2[i - 1]:
        arr[i][j] = arr[i - 1][j - 1]
      else:
        a = arr[i - 1][j] + 1
        b = arr[i][j - 1] + 1
        c = arr[i - 1][j - 1] + 1
        arr[i][j] = min(a, b, c)
  return arr[len(token2)][len(token1)]