Python script to abuse the XMLRPC.php server on a typical wordpress website.

[Install]

```
Clone or download the wp-artillery.py
```

[Usage]

```
python3 wp-artillery.py targetURL threads runForever
```

[Example]

Using the script with TOR and ProxyChains on Kali Linux
```
proxychains python3 wp-artillery.py https://somewordpresssite.com/xmlrpc.php 500 true
```
The above will run the dos script through TOR with 500 threads with the final arg "true" it will run forever

```
python3 wp-artillery.py https://somewordpresssite.com/xmlrpc.php 500 false
```
The above will run without using TOR, using 500 threads and the false flag at the end will stop the script when it has run through its task



[Effectiveness]
```
To effectively take out a target 500 threads work However! 1 thread is enough to cause a bottleneck 
and slow it right down. This has been tested against a target server with the script running 
through proxychains in 2 terminals. For a long term solution the script could be modified 
to open itself over and over refreshing the settings and connections.
```


[Online or Offline]
```
If you have run the attack and it shows offline on DownOrNot etc but the website is still up 
then there is a cached version either on your computer or online.Try and access the website 
from another browser or private window where its not cached.
```


[Concept]
```
The concept is really simple, it spams the living piss out of listMethods with a small 
request the response is amplified. As long as we request more from the webserver than
what we put in it will always result in a DOS
```

![Capture1](https://user-images.githubusercontent.com/38970826/226070691-6fc84415-8f21-4e1f-a7c7-9454c79d0d6d.PNG)

![Capture2](https://user-images.githubusercontent.com/38970826/226070700-74a2bf7c-576b-44d7-90ad-1089c7842303.PNG)

