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
app.use((req,res,next) => {
    console.log("Hello! from middleware ");
	next();
    
})

app.get('/', (req,res) => {

	let fs = require('fs');
	// let filename = "test/input.csv";
	let filename = "data/input.csv";
	let lines = [];
	fs.readFile(filename, 'utf8', function(err, data) {
		if (err) throw err;
		console.log('Read file - ' + filename);
		lines = data.split(/\r?\n/);

		for(let i=1;i<=5;i++) {
			let val = lines[i-1].split(',');
			if(val.length<2) continue;
			let a = val[0], b = val[1];
			const c = +a + +b;
			console.log("Result of operation " + i +" = " + c);
		}


	});

	let a=20, b=89;
    const c = a+b;
    console.log("Result of operation = ",c);
	
	res.status(200).json({message : "Result of the operation", data:c})
	
})
module.exports = app;