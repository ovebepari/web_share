### web_share_ftp - A Simple Flask App to Share Files Over the Network

This is a simple flask app / cli tool that serves your current folder to share files from the host to the client browser or upload to host from a client browser.

To install on GNU/Linux, Debian / Ubuntu / Linux Mint:
```bash
sudo python3 -m pip install web_share_ftp
```

To install on Windows:
```bash
python -m pip install web_share_ftp
```

To start the server:
```bash
web_share_ftp serve
```

To access server from another device, find your local ip by checking `ifconfig` in GNU/Linux and `ipconfig` in windows.

And of course I could use `http.server` for serving the files but I somewhat wanted to do it myself.

Here's a web UI view of the flask app:

![*web-share screenshot, check github if png not appears*](web_share_ftp/webshare-ftp.png)