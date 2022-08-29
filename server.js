const express = require("express");
const dotenv = require("dotenv");


dotenv.config({ path: "./config.env" });
const app = require("./index");


//START SERVER
const port = process.env.PORT;
const server = app.listen(port, () => {
  console.log(`App running on port ${port}...`);
});