# Group 5 - Telegram Bot

## Installation Instructions

### Purpose of this Document

This README file provides comprehensive installation and operating instructions for the **Job Application Bot**, a Telegram bot project developed as coursework for the course 5G00FT06-3002 Software Project.

### Table of Contents

1. [Introduction](#introduction)
2. [System Context](#system-context)
3. [SW Architecture based on the C4-model](#sw-architecture-based-on-the-c4-model)
4. [Installation and Operating Instructions](#installation-and-operating-instructions)
   - [Installing, Setting Up, and Starting the Containers](#installing-setting-up-and-starting-the-containers)
   - [Demonstration Instructions](#demonstration-instructions)
5. [Developer Instructions](#developer-instructions)

### Introduction

The Telegram Bot project aims to create a versatile and user-friendly bot for the Telegram messaging platform, allowing students to search for jobs in their field posted on the job teaser website. This README serves as a guide for developers and IT personnel responsible for system development, maintenance, and deployment.

For detailed documentation, refer to [Confluence Pages](https://sw-requirements-2023.atlassian.net/wiki/spaces/PS/overview).

### System Context

- C4 model system level
  - Containers
  - Code
    - Class diagram for the code

### SW Architecture based on the C4-model

For detailed information on the software architecture, follow the C4 model. The documentation includes component interaction as a sequence diagram.

### Installation and Operating Instructions

#### Installing, Setting Up, and Starting the Containers

1. Clone the repository or extract the code from the provided zip file:
   ```bash
   git clone ssh://git@gitlab.tamk.cloud:1022/sw-project-group-5/group-5-telegram-bot.git customer-side-installation
   unzip customer-side-installtion.zip
   ```
2. cd into the directory

```bash
cd customer-side-installtion
```

3. Run pip install to get all the dependencies

```bash
pip3 install –r requirements.txt
```

4. env file
   Follow .env-example fileto have all variables for the application

   - TELEGRAM_TOKEN=<your_telegram_token>
   - TELEGRAM_LINK=<your_telegram_bot_name>
   - TEST_API_ID=<your_test_api_id>
   - TEST_API_HASH=<your_test_api_hash>
   - SESSION_STR=<your_session_string>

5. Setting Up Telegram Credentials

- **TELEGRAM_TOKEN:** Create a Telegram Bot with [BotFather](https://t.me/BotFather). Replace `<your_telegram_token>` with the generated token.

- **TELEGRAM_LINK:** This is the Telegram bot name when created with [BotFather](https://t.me/BotFather). When entered into the browser or Telegram chat search, the bot should show up.

- **TEST_API_ID and TEST_API_HASH:** These are tokens created from your own Telegram account. For testing, you need these so that the application can send messages to your Telegram bot using your account.

- **SESSION_STR:** This is an option of Telethon to format your session data into a not-so-long string that can be easily fit into an environment variable. To get SESSION_STR, you can run the provided code or visit [this website tutorial](https://blog.1a23.com/2020/03/06/how-to-write-integration-tests-for-a-telegram-bot/) for better understanding.

5. Restore the database from the backup file

```bash
mysql -u sql -p sqlpass user_infodb < backup.sql
```

6. Run the service

```bash
python3 jobteaser_data.py
```

#### Demonstration Instructions

1. After setting up the code and adding credentials to the .env file, run the bot

```bash
python3 bot.py
```

2. Add the bot on Telegram by searching for the nickname @JobTeaser_bot
3. Verify the successful setup by checking the output of bot.py.
4. Use the bot for job search and application.

#### Developer Instructions

1. For backend testing, access to the VM must be granted. To demonstrate, run jobteaser.py with the following command

```bash
python3 jobteaser.py
```

2. Access the database using the "sql" user:

```bash
USE user_infodb;
```

Results can be visualized from the database.
