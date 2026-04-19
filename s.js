const fs = require("fs");
const crypto = require("crypto");

const inputImg = "index.zip";
const ooutfile = "banner_1.jpg";

function encryptFile(inputFile, key) {
  const cipher = crypto.createCipher("aes-256-cbc", key);
  const input = fs.readFileSync(inputFile);
  return Buffer.concat([cipher.update(input), cipher.final()]);
}

function tomage(plainImagePath, coverImagePath, outputImagePath, key) {
  const encryptedBuffer = encryptFile(plainImagePath, key);
  const imageBuffer = fs.readFileSync(coverImagePath);
  const outputBuffer = Buffer.concat([imageBuffer, encryptedBuffer]);
  fs.writeFileSync(outputImagePath, outputBuffer);
  console.log("Encryption and merge completed.");
}

const encryptionKey = crypto
  .createHash("md5")
  .update(fs.readFileSync(""))
  .digest("hex");

tomage(inputImg, "", ooutfile, encryptionKey);
