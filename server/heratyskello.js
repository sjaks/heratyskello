// heratyskello server

const http = require('http');
const url = require('url');
const fs = require('fs');
require('dotenv').config();

let wakeUp = false;
const secret = process.env.SECRET;

const requestListener = function (req, res) {
    // Set defauly HTTP response values
    res.setHeader("Content-Type", "text/html; charset=utf-8");
    let returnCode = 200;
    let responseText = "";

    // Parse URL path and parameters
    const queryObject = url.parse(req.url, true);
    const path = queryObject.pathname.replace(/\//g, "");
    const querySecret = queryObject.query.secret;

    if (path == "") {
        // Load and serve main web front end
        responseText = fs.readFileSync(__dirname + "/index.html", { encoding: "utf8" });
    } else if (path == "get") {
        // Entry point for RPi clients
        responseText = wakeUp.toString();
    } else if (path == "set") {
        // Require authentication
        if (querySecret === secret) {
            // Call for wakeup
            wakeUp = true;
            responseText = "success";
        } else {
            returnCode = 401;
            responseText = "failure";
        }
    } else if (path == "unset") {
        // Require authentication
        if (querySecret === secret) {
            // Disable wakeup
            wakeUp = false;
            responseText = "success";
        } else {
            returnCode = 401;
            responseText = "failure";
        }
    } else {
        returnCode = 404;
        responseText = "404 - not found";
    }

    // Respond
    res.writeHead(returnCode);
    res.end(responseText);
}

const server = http.createServer(requestListener);
server.listen(6699);
