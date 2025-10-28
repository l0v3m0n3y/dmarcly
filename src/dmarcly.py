import requests
class Client():
	def __init__(self):
		self.api="https://dmarcly.com/server"
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def spf_check(self,domain):
		return requests.get(f"{self.api}/spf_check.php?domain={domain}",headers=self.headers).json()
	def generate_dkim(self,domain,selector,length):
		return requests.get(f"{self.api}/generate_dkim.php?domain={domain}&selector={selector}&length={length}",headers=self.headers).json()
	def dkim_check(self,domain,selector):
		return requests.get(f"{self.api}/dkim_check.php?domain={domain}&selector={selector}",headers=self.headers).json()
	def dmarc_check(self,domain):
		return requests.get(f"{self.api}/dmarc_check.php?domain={domain}",headers=self.headers).json()
	def bimi_record_check(self,domain):
		return requests.get(f"{self.api}/bimi_record_check.php?domain={domain}",headers=self.headers).json()
	def blacklist_check(self,domain,part:int=11):
		return requests.get(f"{self.api}/blacklist_check.php?domainorip={domain}&part={part}",headers=self.headers).json()