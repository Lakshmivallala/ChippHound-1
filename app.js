const express = require('express');
const helmet = require('helmet');

const { exec } = require('child_process');

const bodyParser = require("body-parser");
const cors = require("cors");

const app = express();
const port = process.env.PORT || 8006;

const { sendMail } = require("./Utils/sendMail");

app.use(helmet());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(cors());

app.get('/', (req, res) => {
	res.send("wtf");
});

app.get('/call', (req, res) => {
	//run the call script

	exec('cd Utils && python call.py', (err, stdout, stderr) => {
	  if (err) {
	    // node couldn't execute the command
	    res.status(400).send("cant execute command");
	    return;
	  }
	  res.status(200).send("done");
	});

});

app.get('/email', async (req, res) => {
	await sendMail("border");
	await res.status(200).send("mail");
})

app.get('/violence/email', async (req, res) => {
	await sendMail("violence");
	await res.status(200).send("mail");
})

app.get('/violence/sms', async (req, res) => {
	await exec('cd Utils && python message.py', (err, stdout, stderr) => {
	  if (err) {
	    // node couldn't execute the command
	    res.status(400).send("cant execute command");
	    return;
	  }
	  res.status(200).send("done");
	});
})

app.listen(port, () => {
	console.log(`listening on ${port}`);
});