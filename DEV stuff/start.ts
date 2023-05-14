import * as Discord from 'discord.js';


const client = new Discord.Client({ intents: Discord.Intents.ALL });
const commandPrefix = '$';
let embedMessageId: string | null = null; // define the variable to store the message ID

// Read the token and channel ID from the file
import * as fs from 'fs';
const token = fs.readFileSync('token.txt', 'utf8').split('\n')[0].trim();
const channelId = parseInt(fs.readFileSync('token.txt', 'utf8').split('\n')[1].trim(), 10);

client.on('ready', async () => {
  const channel = client.channels.cache.get(channelId) as Discord.TextChannel;
  await channel?.messages.fetch();
  await channel?.bulkDelete(100); // delete up to 100 previous messages in the channel
  await channel?.setName('\u{1F534} Service-Status');
  const embed = new MessageEmbed()
    .setTitle('Service Status')
    .setDescription(':red_circle: Service Offline')
    .setColor('#FF0000')
    .setAuthor('*This embed updates when the service status changes*');
  const message = await channel?.send({ embeds: [embed] });
  if (message) {
    embedMessageId = message.id;
    fs.writeFileSync('message_id.txt', embedMessageId);
  }

  //  
  //  await channel?.setName('\u{1F7E2} Service-Status');
  //  await channel?.bulkDelete(100); // delete up to 100 previous messages in the channel
  //  const embed = new Discord.MessageEmbed()
  //    .setTitle('Service Status')
  //    .setDescription(':green_circle: Online')
  //    .setColor('#00FF00')
  //    .setAuthor('*This embed updates when the service status changes*');
  //  const message = await channel?.send({ embeds: [embed] });
  //  if (message) {
  //    embedMessageId = message.id;
  //    fs.writeFileSync('message_id.txt', embedMessageId);
  //  }

  console.log('Bot is ready');
});

if (command === 'offline') {
    await message.channel?.bulkDelete(1);
    const channel = message.channel;
    await channel?.setName('🔴 Service-Status');
    const embed = new Discord.MessageEmbed()
      .setTitle('Service Status')
      .setDescription(':red_circle: Service Offline')
      .setColor(0xff0000)
      .setAuthor('*This embed updates when the service status changes*');
    const statusMessage = await message.channel?.send(embed);
    embed_message_id = statusMessage?.id || '';
    await message.channel?.send(embed_message_id);
  }

  if (command === 'warning') {
    await message.channel?.bulkDelete(1);
    const channel = message.channel;
    await channel?.setName('🟠 Service-Status');
    const statusEmbed = new Discord.MessageEmbed()
      .setTitle('Service Status')
      .setDescription(':orange_circle: Service Unstable, see below')
      .setColor(0xffa500)
      .setAuthor('*This embed updates when the service status changes*');
    await message.channel?.send(statusEmbed);
    const warningEmbed = new Discord.MessageEmbed()
      .setTitle(':orange_circle: Warning!')
      .setDescription(args.join(' '))
      .setColor(0xffa500);
    await message.channel?.send(warningEmbed);
  }

  if (command === 'error') {
    await message.channel?.bulkDelete(1);
    const channel = message.channel;
    await channel?.setName('🟡 Service-Status');
    const statusEmbed = new Discord.MessageEmbed()
      .setTitle('Service Status')
      .setDescription(':yellow_circle: Online with errors, see below')
      .setColor(0xffff00)
      .setAuthor('*This embed updates when the service status changes*');
    await message.channel?.send(statusEmbed);
    const cautionEmbed = new Discord.MessageEmbed()
      .setTitle(':yellow_circle: Caution')
      .setDescription(args[0])
      .setColor(0xffff00);
    const errorEmbed = new Discord.MessageEmbed()
      .setTitle(args[0])
      .setDescription(args[1])
      .setColor(0xffff00);
    await message.channel?.send(cautionEmbed);
    await message.channel?.send(errorEmbed);
    const statusMessage = await message.channel?.send(embed_message_id);
    const embed_message_id = statusMessage?.id || '';
  }

  if (command === 'online') {
    const channel = message.channel;
    await message.channel?.bulkDelete(1);
    await channel?.setName('🟢 Service-Status');
    const embed = new Discord.MessageEmbed()
      .setTitle('Service Status')
      .setDescription(':green_circle: Online')
      .setColor(0x00ff00)
      .setAuthor('*This embed updates when the service status changes*');
    const statusMessage = await message.channel?.send(embed);
    const embed_message_id = statusMessage?.id || '';
    await message.channel?.send(embed_message_id);
  }

  client.login(token);