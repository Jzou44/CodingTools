const http = require('http');
const fs = require('fs');
const path = require('path');

const dir = path.resolve(__dirname, 'dist');
const mimes = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.json': 'application/json'
};

http.createServer((req, res) => {
  const url = new URL(req.url, 'http://localhost');
  let filePath = path.join(dir, url.pathname === '/' ? 'index.html' : url.pathname);

  // Try file, then try with .html extension
  fs.readFile(filePath, (err, data) => {
    if (err) {
      // Try adding .html
      let htmlPath = filePath + '.html';
      fs.readFile(htmlPath, (err2, data2) => {
        if (err2) {
          res.writeHead(404, {'Content-Type': 'text/plain'});
          res.end('Not found: ' + url.pathname);
          return;
        }
        const ext = path.extname(htmlPath);
        res.writeHead(200, {'Content-Type': mimes[ext] || 'application/octet-stream'});
        res.end(data2);
      });
      return;
    }
    const ext = path.extname(filePath);
    res.writeHead(200, {'Content-Type': mimes[ext] || 'application/octet-stream'});
    res.end(data);
  });
}).listen(5500, () => console.log('Server at http://localhost:5500'));
