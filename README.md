### HTTP server

-----------

Sophia Davis
Summer 2014

------------

This simple, heavily-commented HTTP server serves two static pages and a css file. 

The primary goal of this project was to start learning about network programming, sockets, etc. This [tutorial](http://www.binarytides.com/python-socket-programming-tutorial/) was very helpful.

To run:  

``` 
python httpServer.py
```
and navigate to **localhost:8000**. The server responds to GET requests for root ('/') and '/picture'. All other requests are redirected to a third static page. 

