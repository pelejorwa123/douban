'代理IP模块'
# IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/
# 仅仅爬取首页IP地址就足够一般使用
__author__='pele'
from bs4 import BeautifulSoup
import requests
import random

def getIpList(url,headers):
	response = requests.get(url,headers=headers)
	soup = BeautifulSoup(response.text,'lxml')
	ips = soup.find_all("tr")
	ipList = []
	for i in range(1,len(ips)):
		ipInfo = ips[i]
		tds = ipInfo.find_all("td")
		# tds[1]是ip地址，tds[2]是端口号
		ipList.append(tds[1].text+":"+tds[2].text)
	return ipList

def getRandomIp(ipList):
	proxyList = []
	for ip in ipList:
		proxyList.append("http://"+ip)
	proxyIp = random.choice(proxyList)
	proxies = {"http":proxyIp}
	return proxies

if __name__=="__main__":
	url = "http://www.xicidaili.com/nn/"
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
					  '(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
	}
	ipList = getIpList(url,headers=headers)
	proxies = getRandomIp(ipList)
	print(proxies)