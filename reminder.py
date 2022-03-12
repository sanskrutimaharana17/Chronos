import discord
import os
import time

client= discord.Client()

@client.event
async def on_ready():
  print("Logged in as {0.user}"
       .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  channel= message.channel

#main menu for selection
  if message.content.startswith('$remind'):
    await channel.send('Hello! \nWhat should I remind you about? Choose from:\n1. Education\n2. Health\n3. Create your own')

    def check(m):
      return m.content in ['Education', 'Health', 'Create your own'] and m.channel==channel
    
    msg= await client.wait_for('message', check=check)

    #Education menu
    if msg.content == 'Education':
      await channel.send("Cool :)\nHere's things you can do!!\n1. Homework")
      
    #Health menu
    elif msg.content == 'Health':
      await channel.send("Cool :)\nHere's things you can do!!\n1. Water Reminder\n2. Medications")

      def check(m):
        return m.content == 'Water Reminder' and m.channel==channel
    
      msg= await client.wait_for('message', check=check)
      
      if msg.content == 'Water Reminder':

        msg= await client.wait_for('message')
        interval= int(msg.content)
        
        timer = time.time()
        while True:
          if time.time() - timer > 10:
            return # time to exit from this function
          await channel.send("Reminder!!!\nDrink Water :)")
          time.sleep(2)
          #await asyncio.sleep(2)
      
    else :
      await channel.send("What should I remind you about?")
    
#running the bot
my_secret = os.environ['TOKEN']
client.run(my_secret)

