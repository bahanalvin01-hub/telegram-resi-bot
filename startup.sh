#!/bin/bash

# Pterodactyl Bot Startup Script

# Ensure the script stops on any error
set -e

# Navigate to the bot directory
cd /path/to/your/bot/directory

# Activate the Python virtual environment (modify as necessary)
source venv/bin/activate

# Start the bot
python bot.py
