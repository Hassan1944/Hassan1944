import requests 

def request (url):
	try:
		req = requests.get("https://"+url)
		print(req)

	except requests.exceptions.ConnectionError:
		pass
target_url = "www.google.com"

request(target_url)

# with open("C:\\Users\\shaik ali\\Desktop\\scrapy\\rugstore\\rugstore\\spiders\\2.1 subdomains.txt.txt",'r') as file :
# 	for line in file:
# 		word =line.strip()
# 		test_url =word +"." +target_url
# 		response =request(test_url) 
		
		
# 		if response :
# 			print(f"subdomain {test_url} exist !") 
		
# 		else:
# 			print(f"subdomain {test_url} do not  exist !") 


