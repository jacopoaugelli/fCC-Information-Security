import hashlib

def gen_list():
  
  with open('top-10000-passwords.txt') as f:
    lines = f.readlines()
  
  wordlist = []
  
  for i in lines:
    wordlist.append(i.replace("\n" , ""))
  
  return wordlist

def gen_hashlist(wordlist):
  hashlist = []
  for i in wordlist:
    i = hashlib.sha1(i.encode('utf-8'))
    hashlist.append(i.hexdigest())
  return hashlist

def gen_saltedlist():
  
  with open('known-salts.txt') as s:
    temp =  s.readlines()

  salts = []
  for l in temp:
    salts.append(l.replace("\n" , ""))
    
  appended = []
  prepended = []
  
  for i in gen_list():
    for j in salts:
      appended.append(j + i)
      prepended.append(i + j)
  
  return prepended + appended

def crack_sha1_hash(hash , **arg):
  
  
  hashes = gen_hashlist(gen_list())
  salted_hashes = gen_hashlist(gen_saltedlist())
  
  
  if arg:
    
    salts = []
    with open("known-salts.txt" , 'r') as s:
      temp = s.readlines()
    
    for i in temp:
      salts.append(i.replace("\n" , ""))
      
    
    res = ""
    for i in salted_hashes:
      if i == hash:
        index = salted_hashes.index(i)
        res = gen_saltedlist()[index]
        
    if res != "":
      for i in salts:
        res = res.replace(i , "")
      return res
    else:
      return "PASSWORD NOT IN DATABASE"
  
  
  else:
    res = ""
    for i in hashes:
      if hash == i:
        index = hashes.index(i)
        res = gen_list()[index]
    if res != "":
      return res
    else:
      return "PASSWORD NOT IN DATABASE"

