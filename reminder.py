import discord
import os
import time
from datetime import datetime
import pytz

client= discord.Client()

#smaller values are assigned for the sake of testing
seconds_in_year=20
#31536000
seconds_in_day= 5
#86400
seconds_in_hour=4
#3600

#function to check if it's time to give a reminder
def time_module(user_time_input):
    print("time module in use...")
  
    while True:
        #finds out the current time in the provided timezone
      tz_IN = pytz.timezone('Asia/Kolkata') 
      datetime_IN = datetime.now(tz_IN)
      current_time = datetime_IN.strftime("%H:%M")
      #print(current_time)
      #check if it's time for the reminder to start
      if current_time == user_time_input:
          print("time module ended...")
          break

 #shows that bot is activated
@client.event
async def on_ready():
  print("Logged in as {0.user}"
       .format(client))

#to prevent the bot from replying to itself
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  channel= message.channel

#main menu for selection
  if message.content.startswith('!remind'):
    await channel.send('\nHello :) \nWhat should I remind you about? Choose from:\n\n !education\n !health\n !custom')

    def check(m):
      return m.content in ['!education', '!health', '!custom'] and m.channel==channel
    
    msg= await client.wait_for('message', check=check)

    #Education menu
    if msg.content == '!education':
      await channel.send("\nCool :)\nHere's a list of things you can do!!\n\n !homework\n !meet\n !test")
    
       #if user selects Homework
      def check(m):
        return m.content in ['!homework', '!meet', '!test'] and m.channel==channel
    
      msg= await client.wait_for('message', check=check)
      
      if msg.content == '!homework':
        await channel.send("\nCool :)\nShould I remind you !hourly or !daily ?")
        
        def check(m):
          return m.content in ['!hourly', '!daily'] and m.channel==channel
    
        msg= await client.wait_for('message', check=check)

        #if user wants hourly reminders
        if msg.content == '!hourly':
        
          timer = time.time()
          while True:
            if time.time() - timer > seconds_in_day:
              return # time to exit from this function
            await channel.send("Reminder!!!\nDo your homework :)") #gives a reminder
            time.sleep(seconds_in_hour)
          #await asyncio.sleep(2)

         #if user wants daily reminders
        elif msg.content == '!daily':
        
          timer = time.time()
          while True:
            if time.time() - timer > seconds_in_year:
              return # time to exit from this function
            await channel.send("Reminder!!!\nDo your homework :)") #gives a reminder
            time.sleep(seconds_in_day)

        else:
          await channel.send("Invalid choice :(")

      #when user selects meet reminder
      elif msg.content == '!meet':
        
          #taking input for the time to set reminder
        await channel.send("Enter time in HH:MM")
        def check(m):
          return m.channel==channel
        msg= await client.wait_for('message', check=check)
        await channel.send("Reminder set!")
        timer= str(msg.content)
        time_module(timer)
        await channel.send("Reminder!!!\n You have a meet :)") #gives a reminder

      #when user selects test reminder
      elif msg.content == '!test':
        
          #taking input for the time to set reminder
        await channel.send("Enter time in HH:MM")
        def check(m):
          return m.channel==channel
        msg= await client.wait_for('message', check=check)
        await channel.send("Reminder set!")
        timer= str(msg.content)
        #schedule.every().day.at(timer).do(homework)
        time_module(timer)
        await channel.send("Reminder!!!\n You have a test :)") #gives a reminder

      else:
        await channel.send("Invalid Input :(")
        
    #Health menu
    elif msg.content == '!health':
      await channel.send("Cool :)\nHere's things you can do!!\n !water\n !medicines\n !sleep")

      #if user selects water reminder
      def check(m):
        return m.content in ['!water', '!medicines','!sleep'] and m.channel==channel
    
      msg= await client.wait_for('message', check=check)
      
      if msg.content == '!water':
        await channel.send("Cool :)\nShould I remind you !hourly or !daily ?")
        
        def check(m):
          return m.content in ['!hourly', '!daily'] and m.channel==channel
    
        msg= await client.wait_for('message', check=check)

        #for hourly reminders
        if msg.content == '!hourly':
        
          timer = time.time()
          while True:
            if time.time() - timer > seconds_in_day:
              return # time to exit from this function
            await channel.send("Reminder!!!\nDrink Water :)") #gives a reminder
            time.sleep(seconds_in_hour)
          #await asyncio.sleep(2)

        #for daily reminders
        elif msg.content == '!daily':
        
          timer = time.time()
          while True:
            if time.time() - timer > seconds_in_year:
              return # time to exit from this function
            await channel.send("Reminder!!!\nDrink Water :)") #gives a reminder
            time.sleep(seconds_in_day)

        else:
          await channel.send("Invalid choice :(")

       #if user selects medicine 
      elif msg.content == '!medicines':
        
          #taking input for the time to set reminder
        await channel.send("Enter time in HH:MM")
        def check(m):
          return m.channel==channel
        msg= await client.wait_for('message', check=check)
        await channel.send("Reminder set!")
        timer= str(msg.content)
        #schedule.every().day.at(timer).do(homework)
        time_module(timer)
        await channel.send("Reminder!!!\n Have your medicines :)") #gives a reminder

         #if user selects sleep
      elif msg.content == '!sleep':
        
        #taking input for the time to set reminder
        await channel.send("Enter time in HH:MM")
        def check(m):
          return m.channel==channel
        msg= await client.wait_for('message', check=check)
        await channel.send("Reminder set!")
        timer= str(msg.content)
        #schedule.every().day.at(timer).do(homework)
        time_module(timer)
        await channel.send("Reminder!!!\n Time to sleep :)") #gives a reminder

      else:
        await channel.send("Invalid selection :(")
      
     #custom part implementation
    else :
      await channel.send("What should I remind you about?")
      
      def check(m):
        return m.channel==channel
      text= await client.wait_for('message', check=check)
       
      await channel.send("Enter time in HH:MM")
      def check(m):
        return m.channel==channel
      msg= await client.wait_for('message', check=check)
      await channel.send("Reminder set!")
      timer= str(msg.content)
        
      time_module(timer)
      await channel.send("Reminder!!!")
      await channel.send(text.content)
        
    
#running the bot
my_secret = os.environ['TOKEN']
client.run(my_secret)

