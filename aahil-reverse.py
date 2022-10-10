import os, platform,time
os.system("clear")
print(" or jb new version upload kro fr chalnge kr lena ")
time.sleep(3)
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    import Lite.py
