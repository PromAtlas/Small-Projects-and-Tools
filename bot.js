const {Client, Attachment} = require('discord.js');
const client = new Client();
const auth = require('./auth.json')

client.on('ready', () => {
console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg=>{
if(msg.content ==='!pizzatime'){
  const attachment = new Attachment('./Peter.gif');
msg.channel.send('It\'s pizza time!', attachment);
}
})

client.login(auth.token);
