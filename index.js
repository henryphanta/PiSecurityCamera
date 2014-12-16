var fs = require('fs');
var url = require('url');
var http = require('http');
var authfile = './auth.txt';
//var filename = './image.jpeg';
var filename = './video.mp4';
console.log(filename);
var timestamp = fs.statSync(filename).mtime.getTime();
console.log(timestamp);

http.createServer(function(req, res) {
	console.log(req.url);
	if (req.url == '/' || req.url == '/index.html') {
		//Serve html page
		console.log("got root request");
		var indx = fs.readFileSync('./index.html').toString();
		res.writeHead(200, {'Content-Type': 'text/html' });
		res.write(indx);
		res.end();
	} else if (req.url == '/update') {
		console.log("Got Update request");
			fs.readFile(filename, function(err, data) {
				if (err) {
					res.writeHead(404);
					res.end();
				} else {
					res.writeHead(200, {'Content-Type': 'video/mp4'});
					res.write(data);
					res.end();
				}
			});
	}else if (req.url == '/info') {
		res.writeHead(200, {'Content-Type':'text/plain'});
		if (fs.existsSync(filename)) {
			var updated = fs.statSync(filename).mtime.toString();
			res.write("Video captured at " + updated);
		} else {
			res.write("Video is currently being processed, try again shortly");
		}
		res.end();
	}
	else {
		var requrl = url.parse(req.url, true);
		console.log(requrl);
		if (requrl.pathname == "/redirect") {
			fs.writeFile(authfile, requrl.query['code'], function(){});
			res.writeHead(200);
			res.end(); 
		} else {
			res.writeHead(404);
			res.end();
		}
	}
}).listen(8080);


