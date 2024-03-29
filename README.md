# Herätyskello
An application for waking up a friend utilizing Raspberry Pi and some buzzers

**This project is archived and not suitable for production. A lot of tweaking needs to be done in order to make it work. Dy.fi endpoints are not live anymore.**

### Infra
This project consists of a Node.js server that hosts a simple web interface
used for initiating an alarm on remote Raspberry Pi clients. The web interface
is meant to be accessible from `example.com/wakey`.

Entry point for the Raspberry Pi clients is `example.com/wakey/get`.

Since this project is really meant for personal use, you'll need to dive
deep into the implementation and see how the server works if you want to host it yourself.
Currently, there is no motivation to make this project work on systems other than than mine :).

### How to join? (deprecated)
The API at `https://sjaks.dy.fi/wakey/get` is open, which means anyone can join in
and listen for wake up calls. You just need a Raspberry Pi with a buzzer speaker
connected to it. Then just run `rpi/poller.py`. It is recommended to create a systemd
service with the provided config file.

Buzzer pinout:
- (-) GRND
- (+) GPIO PIN 23

The wakeup initiation via the web interface is limited to authorized users only. Currently [@sjaks](https://github.com/sjaks) and [@basiliski](https://github.com/basiliski) have the ability to make wakeup calls.
