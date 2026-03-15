# Titania

## Description
**Titania – Multilingual Discord Greeting Bot**  

Titania sends friendly, multilingual greetings to your Discord server on a weekly schedule.  
Designed for communities, Titania posts messages in multiple languages with emojis, ensuring everyone feels welcomed.  
Built with **Discord.py** and **APScheduler**, it supports scheduled greetings, immediate test sending, and easy configuration through environment variables.

---

## Contributions

Contributions are welcome!  

If you’d like to contribute to Titania — whether it’s adding new greetings, fixing bugs, or improving documentation — please check out the [Contributors page](https://github.com/yourusername/titania/graphs/contributors) for a list of existing contributors and ways to get involved.

## Table of Contents

<details>
<summary>Table of Contents</summary>

- [Titania](#titania)
- [Description](#description)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [Authors](#authors)
- [License](#license)

</details>

---

## Technology Stack

| Technology        | Description                                                   |
| ----------------- | ------------------------------------------------------------- |
| Python            | Programming language for the bot logic.                      |
| discord.py        | Library for interacting with the Discord API.                |
| APScheduler       | Scheduling library for running weekly greetings automatically.|
| python-dotenv     | Loads environment variables from a `.env` file.              |

---

## Key Features

- **Weekly Greetings**:<br> Automatically sends multilingual greetings with emojis to a designated Discord channel.  

- **Immediate Test Sending**:<br> Allows the greeting to be sent immediately on bot startup for testing purposes.  

- **Multilingual Support**:<br> Greetings are sent in 13+ languages, including English, Spanish, Yuroba, German, and more.  

- **Easy Configuration**:<br> Use a `.env` file to store your Discord bot token securely, keeping your project open-source safe.  

---

## Setup Instructions

1. Clone this repository:

```bash
    git clone https://github.com/yourusername/titania.git
    cd titania
 ```

3. Create and activate a virtual environment:
 ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
 ```

 3. Install required libraries:
    ```bash
        pip install -r requirements.txt
    ```

4. Create a .env file in the project root:

  ```bash
    DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
    CHANNEL_ID=YOUR_TARGET_CHANNEL_ID
    ```
5. Run the bot:
  ```bash
    python bot.py
    ```

## Usage
- Invite Titania to your server via the Discord Developer Portal.
- Ensure the bot has Send Messages permissions in the target channel.
- Use the .env file to change the channel or token as needed.

## Future Enhancements
- Add new greetings in additional languages as the community grows.
- Support custom greetings for holidays or special events
- Add interactive commands for users to request on-demand greetings.

## Authors

| Name            | Link                                        |
| --------------- | ------------------------------------------- |
| Sandra Ashipala | https://www.linkedin.com/in/sandraashipala/ |

## License

[![GitLicense](https://img.shields.io/badge/License-MIT-lime.svg)](https://github.com/sandramsc/Titania/blob/master/LICENSE.md)