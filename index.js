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
	let a=20, b=89;
    const c = a+b;
    console.log("Result of operation = ",c);
	
	res.status(200).json({message : "Result of theoperation", data:c})
	
})
module.exports = app;