## Challenge 12 ezFile Sharing

**Category :** Web

**Points :** 100

**Solves :** 11

**Description :**

![image](12.png)

### Write-up

For this challenge we presented with this website :

![image](ez1.png)


Not so much can be found it robots.txt, try uploading some file to check if there is some remote execution happened but no luck. Then, we try some of the common directory on the website and we found this!

![image](ez2.png)

Its a .git folder which the web adminnistrator forget to remove

using tools from here
https://github.com/internetwache/GitTools

```bash
./gitdumper.sh http://ezfile-sharing.wargames.my/.git/ ezfile
```

![image](ez3.png)

We succesfully dump the repo and do 
```bash
git checkout .
```
![image](ez4.png)

open index.php

![image](ez5.png)

Flag : wgmy:{AdminGitGudPlease}