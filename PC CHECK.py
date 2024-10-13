import psutil
import os
import discord
import asyncio
import glob

print("\033[34m" + r'''
  _____   _____    _____ _    _ ______ _____ _  __
 |  __ \ / ____|  / ____| |  | |  ____/ ____| |/ /
 | |__) | |      | |    | |__| | |__ | |    | ' / 
 |  ___/| |      | |    |  __  |  __|| |    |  <  
 | |    | |____  | |____| |  | | |___| |____| . \ 
 |_|     \_____|  \_____|_|  |_|______\_____|_|\_\
                                                  
                                                  
'''+ "\033[0m")

BLUE = "\033[94m"
RESET = "\033[0m"

# Print message in blue
print(f"{BLUE}By Super And Speed{RESET}")



discord_name = input("Enter your Discord name: ")

# List of applications to check for (including executors, Roblox cheats, and auto-clickers)
apps_to_check = [
    'Solara', 'Wave', 'Delta', 'Codex', 'Celery', 'Roapi', 'Nyx',
    'Exploit', 'Bytehub TPS', 'Macro', 'Bootstrapper', 'krnl', 
    'jules', 'hydrogen', 'fluxus', 'Vega X', 'Arceus X', 
    'Valysse', 'Alysse', 'Synapse X',
    # Executors
    'Script-Ware', 'JJSploit', 'Firesploit', 'Kohau', 'Skisploit',
    # Roblox Cheats
    'Fling', 'Speed', 'Infinite Yield', 'Btools', 'God Mode',
    # Auto Clickers
    'OP Auto Clicker', 'Auto Clicker Pro', 'GS Auto Clicker', 'Speed Auto Clicker', 'Fast Auto Clicker'
]

# User IDs for notification
users_to_notify = {
    'realspeed1': 1287388021301317717,
    'os_0o': 1277671308183994398
}

# Function to check running applications
def check_running_apps():
    found_cheats = False
    detected_apps = []
    print("\nChecking running processes for cheats...\n")
    for process in psutil.process_iter(['name', 'exe']):
        for app in apps_to_check:
            if process.info['name'] and app.lower() in process.info['name'].lower():
                found_cheats = True
                detected_apps.append(process.info['name'])
                print(f"Cheat detected: {process.info['name']}")
                print(f"Location: {process.info['exe']}")
    return found_cheats, detected_apps

# Function to search for files by name
def search_files_by_name(root_dir):
    found_files = False
    detected_files = []
    print("\nSearching for files with specific names...\n")
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_without_ext = os.path.splitext(file)[0]  # Get the filename without the extension
            if file_without_ext.lower() in (app.lower() for app in apps_to_check):
                found_files = True
                detected_files.append(file)  # Store just the file name
                print(f"File found: {file}")
                print(f"Location: {os.path.join(root, file)}")
    return found_files, detected_files

# Function to get files from the Recycle Bin
def get_recycle_bin_files():
    recycle_bin_path = os.path.join(os.environ['systemroot'], '$Recycle.Bin', '*')
    recycle_bin_files = glob.glob(recycle_bin_path + '/*')
    return recycle_bin_files

# Function to send DMs to users by ID
async def send_dm(user_ids, message, token):
    intents = discord.Intents.default()
    intents.messages = True
    intents.dm_messages = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        for user_id in user_ids:
            user = await client.fetch_user(user_id)
            await user.send(message)
            print(f"Sent DM to {user.name}: {message}")
        await client.close()

    await client.start(token)

# Asynchronous main function
async def main():
    cheat_detected, detected_apps = check_running_apps()
    suspicious_files_found, detected_files = search_files_by_name("C:\\")

    # Get files from the Recycle Bin
    recycle_bin_files = get_recycle_bin_files()

    if cheat_detected or suspicious_files_found:
        print("\nCheats or suspicious files exist.")

        # Prepare the message with details of detected applications
        app_names = ", ".join(detected_apps) if detected_apps else "No specific applications found."
        message_apps = f"**Detected Applications:**\n```{app_names}```"

        # Prepare message for detected files
        if detected_files:
            file_names = ", ".join(detected_files)
            message_files = f"**Suspicious Files Found:**\n```{file_names}```"
        else:
            message_files = "**Suspicious Files Found:**\n```No suspicious files found.```"

        # Prepare message for Recycle Bin files
        if recycle_bin_files:
            recycle_file_names = ", ".join([os.path.basename(file) for file in recycle_bin_files])
            message_recycle_bin = f"**Files in Recycle Bin:**\n```{recycle_file_names}```"
        else:
            message_recycle_bin = "**Files in Recycle Bin:**\n```No files found in Recycle Bin.```"

        # Combine all messages into one
        full_message = f"{message_apps}\n\n{message_files}\n\n{message_recycle_bin}"

        # Send the combined message
        await send_dm(users_to_notify.values(), full_message, "MTI5MjI0MTMzOTQ5NjQwMjk0NA.GHjDCR.IKEafY1ZNCFNq24_j2Dy9Uq4rREZ16OZQNW7XY")  # Replace YOUR_BOT_TOKEN with your actual bot token

    else:
        print("No cheats or suspicious files detected.")

# Run the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())
