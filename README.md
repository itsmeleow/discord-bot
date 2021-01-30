# Discord Bot
Simple discord bot for moderation. Built on [discord.py](https://pypi.org/project/discord.py/).

## Features
Here are some commands. Command prefix can be changed my replacing value inside of command_prefix.

- `.help` -> Lists all of the commands

Moderation
- `.clear [x amount]` -> clears x amount of messages in channel
- `.kick [@user]` -> kicks tagged user 
- `.ban [@user]` -> bans tagged user 

Other
- `.ping` -> simple ping command to test if bot is working or check client latency
- `.av` -> returns clients discord avatar
- `.ball [yes/no question]` -> returns yes/no replys

## Setup - Windows
1. Install [Python](https://www.python.org/)
2. Run `python` in cmd and check if installed. It should return python version number.
3. Run `py -m pip --version` in cmd to check if pip is installed. It should return pip version number. Pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4
4. Set up your `token` by replacing 'ENTER_TOKEN_HERE' with your [bot token](https://discord.com/developers/applications)
5. Run `python main.py` to start your bot!

## Help
Check if dependencies are properly installed discord.py. If not, run `pip install discord.py` or read more about discord.py [here](https://pypi.org/project/discord.py/)