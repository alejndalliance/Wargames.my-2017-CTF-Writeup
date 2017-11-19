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
        #os.system(r"Decrypting_a_File.exe"" top_secret_mission.txt.sulit top_secret_mission.txt top_secret_mission.txt")


if __name__ == "__main__": 
    main() 