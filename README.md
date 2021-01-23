# Herätyskello
An application for waking up a friend utilizing Raspberry Pi and some buzzers

### Infra
This project consists of a Node.js server that hosts a simple web interface
used for initiating an alarm on remote Raspberry Pi clients. The web interface
is meant to be accessible from `example.com/wakey`.

Entry point for the Raspberry Pi clients is `example.com/wakey/get`.

Since this project is really meant for personal use, you'll need to dive
deep into the implementation and see how it works if you want to use it.
Currently, there is no motivation to make this project work on other systems
than mine :).