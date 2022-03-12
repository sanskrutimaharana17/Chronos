# Nitya's code
import discord
import os
import time



client = discord.Client()
@client.event
async def on_ready():
  print("{0.user} is summoned!!".format(client))
  @client.event
  async def on_message(message):
    flag=1

    welcome="Hey there!! Here's a list of things you can do :)\n1. Schedule and Track your progress with---  !track\n2. Calculate and make your maths easy with---  !calc\n3. Try to play songs and lighten up---  !play\n\n!exit can be used to quit"

    
    if message.author == client.user: 
      return 
      
    channel= message.channel
    while flag==1:
      
    #wake up to chronos
      if message.content.startswith('!chronos'):
        await channel.send(welcome)
  
        def check(m):
          return m.content in ['!track', '!calc', '!play','!exit'] and m.channel==channel
        
        msg= await client.wait_for('message', check=check)
    
        if msg.content == '!track':
          await channel.send("STUFF FOR TRACKING")
          #!track
          #reminder will be incorporated here 
        
        
        
        elif msg.content=="!calc":
          await channel.send("matlab nd calc integrated")
          #!calc
          #matlab integration!!!!
        
        
        
        elif msg.content=="!play":
          await channel.send("play pause skip features for bot")
        #!play song name
        #!pause and !skip features are to be added too!!
        
        
        
        
        elif msg.content=="!exit":
          flag=0
          await msg.content.send("Have a good time :) ")
          break
        
        
        
        else:
          await msg.content.send("Looks like smthg went wrong???")
          time.sleep(2)
my_secret = os.environ['TOKEN']
client.run(my_secret)
