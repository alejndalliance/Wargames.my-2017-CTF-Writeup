## Challenge 12 ezFile Sharing

**Category :** Web

**Points :** 100

**Solves :** 11

**Description :**

![image](https://raw.githubusercontent.com/alejndalliance/Wargames.my-2017-CTF-Writeup/master/Challenge%2012%20-%20ezFile%20Sharing/12.PNG)

### Write-up

For this challenge we presented with this website :

![image](https://raw.githubusercontent.com/alejndalliance/Wargames.my-2017-CTF-Writeup/master/Challenge%2012%20-%20ezFile%20Sharing/ez1.PNG)


Not so much can be found it robots.txt, try uploading some file to check if there is some remote execution happened but no luck. Then, we try some of the common directory on the website and we found this!

![image](https://raw.githubusercontent.com/alejndalliance/Wargames.my-2017-CTF-Writeup/master/Challenge%2012%20-%20ezFile%20Sharing/ez2.PNG)

Its a .git folder which the web adminnistrator forget to remove

using tools from here
https://github.com/internetwache/GitTools

```bash
./gitdumper.sh http://ezfile-sharing.wargames.my/.git/ ezfile
```

![image](https://raw.githubusercontent.com/alejndalliance/Wargames.my-2017-CTF-Writeup/master/Challenge%2012%20-%20ezFile%20Sharing/ez3.PNG)

We succesfully dump the repo and do 
```bash
git checkout .
```
![image](https://raw.githubusercontent.com/alejndalliance/Wargames.my-2017-CTF-Writeup/master/Challenge%2012%20-%20ezFile%20Sharing/ez4.PNG)

open index.php

![image](https://raw.githubusercontent.com/alejndalliance/Wargames.my-2017-CTF-Writeup/master/Challenge%2012%20-%20ezFile%20Sharing/ez5.PNG)

Flag : wgmy:{AdminGitGudPlease}
