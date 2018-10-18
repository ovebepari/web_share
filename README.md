### webshare - A Simple Flask App to Share Files Over the Network

This is a simple flask app / cli tool that serves your current folder to share files from the host to the client browser or upload to host from a client browser.

To install on GNU/Linux, Debian / Ubuntu / Linux Mint:
```bash
sudo python3 -m pip install web-share
```

To install on Windows:
```bash
python -m pip install web-share
```

To start the server:
```bash
web-share serve
```

To access server from another device, find your local ip by checking `ifconfig` in GNU/Linux and `ipconfig` in windows.

And of course I could use `http.server` for serving the files but I somewhat wanted to do it myself.

Here's a web UI view of the flask app:

![*web-share screenshot*](web-share/webshare-ftp.png)