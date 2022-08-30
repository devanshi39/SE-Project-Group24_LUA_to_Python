const express = require('express');
const cors = require("cors");
const path = require('path');
const app = express();

app.use(function (req, res, next) {
	res.setHeader('Access-Control-Allow-Origin', '*');
	res.setHeader(
		'Access-Control-Allow-Methods',
		'GET, POST, OPTIONS, PUT, PATCH, DELETE',
	);
	res.setHeader(
		'Access-Control-Allow-Headers',
		'X-Requested-With,content-type',
	);
	res.setHeader('Access-Control-Allow-Credentials', true);

	// Pass to next layer of middleware
	next();
});
app.use((req, res, next) => {
	console.log("Hello! from middleware ");
	next();

})

app.get('/', (req, res) => {

	let fs = require('fs');
	let filename = "data/input.csv";
	let opfile = "data/output.csv";
	let lines = [];
	fs.readFile(filename, 'utf8', function (err, data) {
		if (err) throw err;
		console.log('Read file - ' + filename);
		lines = data.split(/\r?\n/);
		let final_string = "";
		for (let i = 0; i < lines.length; i++) {
			let val = lines[i].split(',');
			if (val.length < 2)
				continue;
			let a = val[0], b = val[1];
			const c = +a + +b;
			final_string += c + "\n";
		}
		fs.writeFile(opfile, final_string, function (err) {
			if (err)
				return console.error(err);
			console.log("finished writing");
		});
	});
	res.status(200).json({ message: "Output file created at location: /data/output.csv" });
})
module.exports = app;