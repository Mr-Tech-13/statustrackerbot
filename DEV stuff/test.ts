import { Client, Message, MessageEmbed, intents } from 'discord.js';

const client = new Client(intents.ALL);
const prefix = '!';

client.on('ready', () => {
  console.log(`Logged in as ${client.user!.tag}`);
});

client.on('message', (message: Message) => {
  if (!message.content.startsWith(prefix) || message.author.bot) return;

  const args = message.content.slice(prefix.length).trim().split(/ +/);
  const command = args.shift()?.toLowerCase();

  if (command === 'ping') {
    message.channel.send('Pong!');
  } else if (command === 'info') {
    const embed = new MessageEmbed()
      .setTitle('Server Info')
      .setDescription('This is some server info.')
      .addField('Server Name', message.guild?.name)
      .addField('Total Members', message.guild?.memberCount)
      .setFooter('Thanks for using the bot!');
    message.channel.send(embed);
  }
});

client.login('your-token-goes-here');
