const qrcode = require('qrcode-terminal');
const { Client } = require('whatsapp-web.js');

// Configurado para usar o Chrome do seu computador
const client = new Client({
    puppeteer: {
        executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    }
});

client.on('qr', qr => {
    qrcode.generate(qr, {small: true});
});

client.on('ready', () => {
    console.log('Client is ready!');
});

client.on('message', (msg) => {
    if (msg.body.toLocaleLowerCase() == '!boa noite') {
        msg.reply('Olá! seja bem vindo');
    }
});

client.initialize();

