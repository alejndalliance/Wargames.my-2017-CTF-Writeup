## Challenge 8 Ran$0m-n00b-w4r3

**Category :** Binary

**Points :** 150

**Solves :** 2

**Description :**

![image](8.png)

### Write-up

For this challenge we have binary called "sulit.exe" and encrypted file "top_secret_mission.txt.sulit" the explanation is already at [klks blog here](http://security.my/post/167643301287/wargamesmy-2017-rans0me-n00b-w4r3)

so basically we need the key to decrypt encrypted, [@mokhdzanifaeq](https://github.com/mokhdzanifaeq) found out the encryption are same as this [MSDN Dev Center](https://msdn.microsoft.com/en-us/library/windows/desktop/aa382358(v=vs.85).aspx) and the how it use the password for encrypt and decrypt.

So we compile de decryption code and try the password which is original filename of the file "top_secret_mission.txt" with added key as first character, so our bruteforcer looks like this

```python
import os
import sys 
import time

#correcrt key is 0xb9

start = 0x1  # hex literal, gives us a regular integer
end = 0xFF

def main(): 
    print ("[+] Brute Now: ") 
    for line in xrange(start,end+1):
        print (line) 
        [decrypt] = chr(line)
        #time.sleep(0.2)
        os.system(r"Decrypting_a_File.exe top_secret_mission.txt.sulit "+decrypt+"top_secret_mission.txt "+decrypt+"op_secret_mission.txt")

if __name__ == "__main__": 
    main() 
```
got a file with the output

```text
This is a super secret file. The flag you are looking for is: L4m3R4n$0mwAr31zL4m3

Regards,
Kuehtiow
```

Flag : L4m3R4n$0mwAr31zL4m3