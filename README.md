# InstaPageHandlerBot
A bot telegram for the totally autonomous management of Instagram pages via Deep Learning.

### By [RiccardoDominici](https://github.com/RiccardoDominici)

# Commands
### Start 
Start the bot and instagram login.
### Post_now
Based on a topic, it generates an image with Dall-e, a caption and hashtags with gpt-3, then it posts all immediately on Instagram. 
### Post (coming soon)
Start the recurrent publication of generated posts as written before.
### Stop_post (coming soon)
Stop recurrent pubblication.
### View_error (coming soon)
View error files.
### Logout 
Delete config files. 
### Help 
View list of comands.

# Configuration
## Secrets

You simply have to create a ``` secrets.env ``` file and insert all your credentials:
```
TELEGRAM_TOKEN=YOUR_TELEGRAM_TOKEN
OPENAI_API_KEY=YOUR_OPENAI_KEY
BOT_USERNAME=@yourTelegramBotUsername
USERNAME_INSTA=your.instagram.page.nick
PASSWORD_INSTA=Y0ur1nstagramPag3Psw
```
## Install dependencies

```
pip3 install -r requirements.txt
```
