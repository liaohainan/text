const fs = require('fs');
const crypto = require('crypto');

const inputImg = 'banner1.jpg'
const outputImg = 'index_1.jpg'

const ooutfile = 'banner_1.jpg'

fs.writeFileSync(outputImg, '');
function encryptFile(inputFile, outputFile, key) {
  const cipher = crypto.createCipher('aes-256-cbc', key);
  
  const input = fs.createReadStream(inputFile);
  const output = fs.createWriteStream(outputFile);

  input.pipe(cipher).pipe(output);

  output.on('finish', () => {
    console.log('Encryption completed.');
  });
}

encryptFile(inputImg, outputImg, 'encryption_key');

function tomage(zipPath, imagePath, outputImagePath) {
    const zipBuffer = fs.readFileSync(zipPath);
    const imageBuffer = fs.readFileSync(imagePath);

    const outputBuffer = Buffer.concat([imageBuffer, zipBuffer]);
    fs.writeFileSync(outputImagePath, outputBuffer);
}

setTimeout(()=>{
    tomage(outputImg, '123.jpg', ooutfile)
},2000)
