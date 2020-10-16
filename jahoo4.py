import time
import urllib
import sys
import os
import datetime


os.system('clear')


won_data="""                                         
\033[1;34;40m                  \             /            
\033[1;34;40m                   \___________/    won data 
\033[1;33;40m                   /           \             
\033[1;33;40m                  /   @     @   \            
\033[1;32;40m                 ||             ||          
\033[1;34;40m                  \   \_ __ _/  /            
\033[1;30;40m                   \___________/                        
"""



no_data="""  
\033[1;34;40m                  \             /            
\033[1;34;40m                   \___________/    not data 
\033[1;33;40m                   /           \             
\033[1;33;40m                  /   @     @   \            
\033[1;32;40m                 ||    _ _ _    ||           
\033[1;32;40m                  \   /     \   /            
\033[1;30;40m                   \___________/             
  """



line = """\033[1;36;40m\n___________________________________________________________\n"""


def login():
  os.system('clear')
  aa= str(input("\033[1;36;40mEnter password :- "))
  if aa == 'jahoo9808' or aa == 'jahoo1998' or aa == 'jahoo98' or aa == 'jayashan' or aa == 'jayashan ' :
    print("success")
  else:
    os.system('clear')
    b = str(input("\n\033[1;31;40mWrong password\n\n\033[1;33;40mAre you want Reenter password(y/n) : - "))
    if b == 'y' or b == 'Y' :
      login()
    elif b == 'n' or b == 'N' :
      os.system('clear')
      exit()
    else:
      login()
  
login()

os.system('clear')
ready="\n\n>>>>\033[1;33;40m check device ip\n\033[1;31;40m>>>>\033[1;33;40m connect device ip\n\033[1;31;40m>>>>> \033[1;33;40mhandshake device ip\n\033[1;31;40m\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"

now = datetime.datetime.now()
print("Today is ",end="")
print(now.strftime("%y-%m-%d"))
print("expired date 2021-1-1\n" )
if now.strftime("%m") == '02' or now.strftime("%m") == '01' :
  print("Account is deactivate\nplease Contact owner\ncreate by jayashan😂😂😂😂😂")
  for j in range (10):
    time.sleep(0.3)
  exit()
else:
  print("\033[1;31;40mIp Active\n connect user account")
  for char in ready:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)


try:
    from tqdm import tqdm
  
except ImportError:
    os.system('pip3 install tqdm')
    print('%s Requests installed.')
    os.system('clear')
    from tqdm import tqdm

try:
    f = open("file_auth.txt", "r")
    file_auth = f.read()
    f.close 
except:
    wr = str(input("\033[1;0;40mPaste Your Auth here :- "))
    f = open("file_auth.txt", "w")
    f.write(wr)
    f.close
    f = open("file_auth.txt", "r")
    file_auth = f.read()
    f.close
    
try:
    f = open("file_url.txt", "r")
    file_url1 = f.read()
    f.close
except:
    wr = str(input("Paste Your URL here :- "))
    f = open("file_url.txt", "w")
    f.write(wr)
    f.close
    f = open("file_url.txt", "r")
    file_url1 = f.read()
    f.close


try:
    import requests


except ImportError:
    print('waiting.......')
    os.system('pip3 install requests')
    print('%s Requests installed.')
    os.system('clear')
    import requests

    auth=file_auth
def main():
    os.system("clear")
    head = {"Host": "megarun.dialog.lk",
              "Authorization": file_auth, "X-Unity-Version": "2018.3.0f2"}
    url = file_url1
    
    s = int(input("\033[1;36;40mEnter Amount - "))
    
    os.system('clear')
    
    m=0
    rr=0
    print("programme complete")
    for rr in tqdm(range(rr,s),ascii=" >",desc="process...."):
        print("\n\n\n\n")
        if (rr == 0):
            print("\033[1;30;40mWaiting one and harf minutes opening Algorithm\n\n\n\033[1;34;40m")
            for j in tqdm(range(90),ascii=" >#"):
      
                rrr = j/90*100
                #print("\033[1;36;40m\n>>>",str(int(100-rrr)) +" ",end="")
                time.sleep(1)
                #sys.stdout.write("\033[F")
        else :
            rj = requests.get(url, headers=head)
            request = str(rj)
            if request == '<Response [204]>':
                print(no_data)
            elif request == '<Response [200]>':
                m+=1
                print(won_data)
            else:
                print(line)
                print("\n\033[1;31;40m [retry] Check Again your internet connection... [retry]")
                print(line)

            rr+=1
            
            print("\n\n\n\033[1;32;40m\nNumber of request : ",str(rr-1))
            print("\033[1;32;40m\nNUMBER of Message : ",int(m))
            print("\033[1;33;40m\nWait For Next request\n\033[1;32;40m\n\n\n")
              
            for j in tqdm(range(90)):
      
              rrr = j/90*100
              #print("\033[1;36;40m\n>>> [+]",str(int(rrr)) +"% ",end="")
            
              time.sleep(1)
              #sys.stdout.write("\033[F")
        os.system('clear')
    again()


def again():
    again = input('\033[1;0;40m\nDo Restart Algorithm :  (y/n) - ')
    if again == "y" or again == "Y":
        main()
    elif again == "n" or again == "N":
        quit()
    else:
        print('\033[1;30;40mReEnter')
        again()


if __name__ == "__main__":
    main()
