const nodeMailer = require('nodemailer');
const { borderMail } = require('./view/borderMail');
const { violenceDetection } = require('./view/violenceDetection');

exports.sendMail = (type) => {
	const transporter = nodeMailer.createTransport({
    host: 'smtp.zoho.in',
    port: 465,
    secure: true,  //true for port 465, false for others
    auth: {
      user: 'ztm_opensource@ankuranant.dev',
      pass: 'LaW1cGH8F6CK'
    }
  });
  const mailOptions = {
    from: `"ChippHound" <ztm_opensource@ankuranant.dev>`,
    to: `ankuranant99@gmail.com`,
    subject: 'Alert', // Subject line
    html: type==="border" ? borderMail() : violenceDetection() // mail body
  };
  transporter.sendMail(mailOptions, (error, info) => {
    console.log('yolo')
    if (error) {
      console.log(error);
      // res.status(400).send({success: false});
    } else {
      console.log(info);
      // res.status(200).send({success: true});
    }
  });
}