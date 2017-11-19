## Challenge 1 I open at the close

**Category :** Network

**Points :** 200

**Solves :** 8

**Description :**

![image](https://raw.githubusercontent.com/alejndalliance/Wargames.my-2017-CTF-Writeup/master/Challenge%201%20-%20I%20open%20at%20the%20close/1.PNG)

### Write-up

By opening the URL it shows some old-skool designed website. Nothing interesting much.

![image](https://raw.githubusercontent.com/alejndalliance/Wargames.my-2017-CTF-Writeup/master/Challenge%201%20-%20I%20open%20at%20the%20close/site1.png)

Except in the source code, where you can see this here:

![image](https://raw.githubusercontent.com/alejndalliance/Wargames.my-2017-CTF-Writeup/master/Challenge%201%20-%20I%20open%20at%20the%20close/site2.png)

Well, we have an image file here! Let's try to download it shell we?

Then we hit another roadblock...

![image](https://raw.githubusercontent.com/alejndalliance/Wargames.my-2017-CTF-Writeup/master/Challenge%201%20-%20I%20open%20at%20the%20close/site3.png)

No matter how fast your internet is, the download speed is limited to <= 1kbps. Hmm

Let us do some math, let's say the download speed is 1kbps, it will take approximately 12 days to download the file completely! Well, we only get 24 hours for the competition, right?!

So, what can we do? Well let us try to look inside partially downloaded images.img.

![image](https://raw.githubusercontent.com/alejndalliance/Wargames.my-2017-CTF-Writeup/master/Challenge%201%20-%20I%20open%20at%20the%20close/site4.png)

Hmm all zero bytes only.

Maybe there are some bytes located at the random location inside the images.img?

But how can we download at the arbitrary location inside images.img? The answer to this is [HTTP Range header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Range_requests)!

We constructed a simple script python for this task:

```python
import urllib.request

url = 'http://1511.wargames.my/images.img'

print("Filesize: 1073741857")
start = input("Enter start position : ")
end = input("Enter end position : ")

header = {"Range": "bytes={}-{}".format(start, end)}
req = urllib.request.Request(url=url, headers=header)
req = urllib.request.urlopen(req)

data = req.read().decode('utf-8')

print("Data : " + " ".join("{:02x}".format(ord(c)) for c in data))
```

We know that initial position of images.img contains no data.

Let's try to peek at the middle?

![image](https://raw.githubusercontent.com/alejndalliance/Wargames.my-2017-CTF-Writeup/master/Challenge%201%20-%20I%20open%20at%20the%20close/site5.png)

Hmm, still zero bytes.

Peek at the back of file?

![image](https://raw.githubusercontent.com/alejndalliance/Wargames.my-2017-CTF-Writeup/master/Challenge%201%20-%20I%20open%20at%20the%20close/site6.png)

We found some data!

`3d3d6743394e585a736c6d5a6e6c6d596c745761735633623539475a377054626e4a33640a`

The pattern looks like our beloved ASCII numbers, right?

Decode it into ASCII will return us reversed-base64-string,

`==gC9NXZslmZnlmYltWasV3b59GZ7pTbnJ3d`

Well, we can get the final flag with:

`$ echo -n "==gC9NXZslmZnlmYltWasV3b59GZ7pTbnJ3d" | rev | base64 -d`

Flag: `wrgm:{doyoulikebigfiles}`