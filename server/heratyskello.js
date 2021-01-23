// heratyskello server

const http = require('http');
const fs = require('fs').promises;

let wakeUp = false;
const secret = "salasana";

const requestListener = function (req, res) {
    if (req.url == "/") {
        fs.readFile(__dirname + "/index.html").then(contents => {
            res.setHeader("Content-Type", "text/html; charset=utf-8");
            res.writeHead(200);
            res.end(contents);
        }).catch(err => {
            res.writeHead(500);
            res.end(err);
            return;
        });
    } else if (req.url.includes("/get")) {
        res.setHeader("Content-Type", "text");
        res.writeHead(200);
        res.end(wakeUp.toString());
    } else if (req.url.includes("/set")) {
        if (req.url.includes(secret)) {
            wakeUp = true;
            res.setHeader("Content-Type", "text");
            res.writeHead(200);
            res.end("success");
        } else {
            res.setHeader("Content-Type", "text");
            res.writeHead(200);
            res.end("failure");
        }
    } else if (req.url.includes("/unset")) {
        if (req.url.includes(secret)) {
            wakeUp = false;
            res.setHeader("Content-Type", "text");
            res.writeHead(200);
            res.end("success");
        } else {
            res.setHeader("Content-Type", "text");
            res.writeHead(200);
            res.end("failure");
        }
    }
}

const server = http.createServer(requestListener);
server.listen(6699);
