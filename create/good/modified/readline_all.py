f = open("/Users/macbook/코드/test/create/good/modified/새파일.txt", 'r')
while True:
  line = f.readline()
  if not line: break
  print(line)
f.close()