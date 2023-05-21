# InstaPageHandlerBot
A bot telegram for the totally autonomous management of Instagram pages via Deep Learning.

### By [RiccardoDominici](https://github.com/RiccardoDominici)

## Commands
### Start 
Start the bot and instagram login.
### Post_now
Based on a topic, it generates an image with Dall-e, a caption and hashtags with gpt-3, then it posts all immediately on Instagram. 
### Logout 
Delete config files. 
### Help 
View list of comands.
### Post (coming soon)
Start the recurrent publication of generated posts as written before.
### Stop_post (coming soon)
Stop recurrent pubblication.
### View_error (coming soon)
View error files.
### Watch_stories_from_user (coming soon)
Watch all the stories of all the followers of a user you specify

## Getting Started

How setting up your personal bot.

### Install dependencies

```sh
pip3 install -r requirements.txt
```
### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get your OPENAI API Key at [openai.com](https://platform.openai.com/overview)
2. Get your Telegram token at [official guide](https://core.telegram.org/bots#how-do-i-create-a-bot)
3. Clone the repo
   ```sh
   git clone https://github.com/RiccardoDominici/InstaPageHandlerBot
   ```
4. Simply create a ``` secrets.env ``` file and insert all your credentials:
    ```
    TELEGRAM_TOKEN=YOUR_TELEGRAM_TOKEN
    OPENAI_API_KEY=YOUR_OPENAI_KEY
    BOT_USERNAME=@yourTelegramBotUsername
    USERNAME_INSTA=your.instagram.page.nick
    PASSWORD_INSTA=Y0ur1nstagramPag3Psw
    ```