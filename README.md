# InstaPageHandlerBot
A bot telegram for the totally autonomous management of Instagram pages via Deep Learning.

### By [RiccardoDominici](https://github.com/RiccardoDominici)

## Commands
* Start: Start the bot and instagram login.
* Post_now: Based on a topic, it generates an image with Dall-e, a caption and hashtags with gpt-3, then it posts all immediately on Instagram. 
* Logout: Delete config files. 
* Help: View list of comands.
* Post (coming soon): Start the recurrent publication of generated posts as written before.
* Stop_post (coming soon): Stop recurrent pubblication.
* View_error (coming soon): View error files.
* Watch_stories_from_user (coming soon): Watch all the stories of all the followers of a user you specify

## Getting Started
How to set up your personal bot.

### Install dependencies
```sh
pip3 install -r requirements.txt
```

### Installation and configuration
1. Get your OPENAI API Key at [openai.com](https://platform.openai.com/overview)
2. Get your Telegram token by following the [official guide](https://core.telegram.org/bots#how-do-i-create-a-bot)
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
5. Write your personal prompt in data.json file:
   ```json
   {
   "image_prompt": "description of the image background",
   "text_prompt": "explanation of the text you want above the image",
   "caption_prompt": "explanation of the caption and the type of hashtags you want"
   }

   ```
   

### Example
   prompt:
   ```json
   {
   "image_prompt": "mountains in sunrise with rice field, ultrawide, trees, river, and a road, oil painting style",
   "text_prompt": "write a mock motivational sentence where instead of motivating you jokingly insult your readers. do not use punctuation",
   "caption_prompt": "create a short description of an instagram post for a motivational page, add hashtags"
   }
   ```
   <p align="center">
   
   Watch page: <a href="https://instagram.com/4u.word" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" height="30" width="40" />
   </a>
    </p>
