# Daily Quotes

Get every day a new citation popping in a notification



## Launch 



Firstly: Create Account, and get your API key and create a `.env` file to provide it. :https://api-ninjas.com/

`.env` file : 
```
API_KEY= YOUR_API_KEY

```



Launch as cron job using `gui_launcher.sh`, `maintain_log_file` and `get_citation.sh`
```
sudo apt install crontab
chmod +x get_citation.sh
chmod +x gui_launcher.sh
chmod +x maintain_log_file.sh
crontab crontab_files.sh
```

You can choose your citation category, and modify it in the `config-api.ini`. Default category is "happiness"

List of possibles categories :
category (optional) - category to limit results to. Possible values are:

   - age
   - alone
   - amazing
   - anger
   - architecture
   - art
   - attitude
   - beauty
   - best
   - birthday
   - business
   - car
   - change
   - communications
   - computers
   - cool
   - courage
   - dad
   - dating
   - death
   - design
   - dreams
   - education
   - environmental
   - equality
   - experience
   - failure
   - faith
   - family
   - famous
   - fear
   - fitness
   - food
   - forgiveness
   - freedom
   - friendship
   - funny
   - future
   - god
   - good
   - government
   - graduation
   - great
   - happiness
   - health
   - history
   - home
   - hope
   - humor
   - imagination
   - inspirational
   - intelligence
   - jealousy
   - knowledge
   - leadership
   - learning
   - legal
   - life
   - love
   - marriage
   - medical
   - men
   - mom
   - money
   - morning
   - movies
   - success

