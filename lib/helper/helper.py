'''
XSSCon - 2019/2020
This project was created by menkrep1337 with 407Aex team. 
Copyright under the MIT license
'''
import requests, json
##### Warna ####### 
N = '\033[0m'
W = '\033[1;37m' 
B = '\033[1;34m' 
M = '\033[1;35m' 
R = '\033[1;31m' 
G = '\033[1;32m' 
Y = '\033[1;33m' 
C = '\033[1;36m' 
##### Styling ######
underline = "\033[4m"
##### Default ######
agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} 
line="—————————————————" 
#####################
def session(proxies,headers,cookie):
	r=requests.Session()
	r.proxies=proxies
	r.headers=headers
	r.cookies.update(json.loads(cookie))
	return r

logo=G+"""
             .-***-.     
            /       \    
            \       /    
     .-***-.-`.-.-.<  _  
    /      _,-\ O_O-_/ )  
    \     / ,  `   . `|       TELEGRAM CH 1: @program_masa & TELEGRAM CH 2 : @Minds_Tech  & TELEGRAM CONTACT 1 : @Dr_Masa_Dr &  CONTACT 2 : @DXDMASA  
     '-..-| \-.,__~ ~ /                    FACEBOOK PAGE : @Masaaofficial FACEBOOK CONTACT : @DXDMASA 
           \ `-.__/  /                     INSTAGRAM : @dxd_masa & GITHUB : @DrMasaDr & TWITTER : @DXDMASA 
          / `-.__.-\`-._    ,*,                                                                     
         / /|    ___\-._`-.;  , .----.██████╗░██╗░░██╗██████╗░  ███╗░░░███╗░█████╗░░██████╗░█████╗░ 
        ( ( |.-*`   `'\ '-(     -.---'██╔══██╗╚██╗██╔╝██╔══██╗  ████╗░████║██╔══██╗██╔════╝██╔══██╗ 
         \ \/    {}{}  |   \.__.-'    ██║░░██║░╚███╔╝░██║░░██║  ██╔████╔██║███████║╚█████╗░███████║ 
         \|           /              ██║░░██║░██╔██╗░██║░░██║  ██║╚██╔╝██║██╔══██║░╚═══██╗██╔══██║  
           \        , /               ██║░░██║░██╔██╗░██║░░██║  ██║╚██╔╝██║██╔══██║░╚═══██╗██╔══██║ 
           ( __`;-;'__`)              ██████╔╝██╔╝╚██╗██████╔╝  ██║░╚═╝░██║██║░░██║██████╔╝██║░░██║ 
           `//'`   `||`               ╚═════╝░╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝ 
	
##=======
	
"""
