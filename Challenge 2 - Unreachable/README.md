## Challenge 2 Unreachable

**Category :** Network

**Points :** 100

**Solves :** 5

**Description :**

![image](https://raw.githubusercontent.com/alejndalliance/Wargames.my-2017-CTF-Writeup/master/Challenge%202%20-%20Unreachable/2.PNG)

### Write-up

For this challenge we have pcap to analyze which have a lot of tcp syn packet which to make it harde to analyze

![image](https://raw.githubusercontent.com/alejndalliance/Wargames.my-2017-CTF-Writeup/master/Challenge%202%20-%20Unreachable/pcap1.PNG)

because there is a hint to RFC 792 which clearly about ICMP. We filter out the packet to icmp only packet and found flow between 192.168.1.10 and 192.168.1.8

![image](https://raw.githubusercontent.com/alejndalliance/Wargames.my-2017-CTF-Writeup/master/Challenge%202%20-%20Unreachable/pcap2.PNG)

I use tshark to get the data in the ICMP packet for easier read
```bash
tshark -r icmp.pcap -x 'icmp and ip.src==192.168.1.8' | grep 0010
```

![image](https://raw.githubusercontent.com/alejndalliance/Wargames.my-2017-CTF-Writeup/master/Challenge%202%20-%20Unreachable/pcap3.PNG)

you will found this flag_is_p!ngp0ng~

Flag : p!ngp0ng~