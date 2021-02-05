const http = require('http');

const host = '127.0.0.1';
const port = 7000;


function notFound(res){
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Not found\n');
}

const server = http.createServer((req, res) => {
    switch(req.method) {}
})