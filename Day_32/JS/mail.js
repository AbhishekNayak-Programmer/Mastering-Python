const nodemailer = require("nodemailer");

async function sendEmail() {
  // Create reusable transporter object using Gmail SMTP
  let transporter = nodemailer.createTransport({
    service: "gmail",
    auth: {
      user: "sahilservice300@gmail.com", // your Gmail address
      pass: "ldxlnrloejkpxzmt", // your app password for Gmail
    },
  });

  // Set up email data
  let mailOptions = {
    from: "sahilservice300@gmail.com",
    to: "webcoder41@gmail.com",
    subject: "Greetings",
    text: "Hello Abhishek Nayak Sir!",
  };

  // Send mail with defined transport object
  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      return console.log("Error occurred:", error);
    }
    console.log("Email sent:", info.response);
  });
}

sendEmail();
