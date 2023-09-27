import fs from 'fs';
import Discord, { Client, TextChannel, MessageEmbed, IntentsBitField } from 'discord.js';

const token: string = fs.readFileSync('token.txt', 'utf8').trim();
const channel_id: number = parseInt(fs.readFileSync('token.txt', 'utf8').trim());

const client: Client = new Discord.Client();
let embed_message_id: string | null = null;

client.on('ready', async (): Promise<void> => {
    const channel: TextChannel | undefined = client.channels.cache.get(channel_id) as TextChannel;
    await channel.messages.fetch();
    await channel.setName('\u2B55 Service-Status');
    const embed: MessageEmbed = new Discord.MessageEmbed()
        .setTitle('Service Status')
        .setDescription(':red_circle: Service Offline')
        .setColor('#ff0000')
        .setAuthor('*This embed updates when the service status changes*');
    const message: Message = await channel.send(embed);
    embed_message_id = message.id;
    fs.writeFileSync('message_id.txt', embed_message_id.toString());
    
    console.log('Bot is ready');
});
client.login(token);