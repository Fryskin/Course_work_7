Useful habit tracker:
The project has:
1. Two apps ('users' and 'useful_habits').
    1.1. The app 'useful_habits' has one custom command 'bot.py' for mailing about habits with tegram bot. If you want to launch the command, you supposed to perform 'python manage.py bot'.
    1.2. Model 'UsefulHabit' with all necessary fields for creating a habit. 
    1.3. Two tasks in 'tasks.py' ('request_telegram_names', 'remind'). 'request_telegram_names' for scanning the telegram bot and associate usernames with chat_id and 'remind' for mailing.
    1.4. The app 'users' has one custom command 'create_superuser.py' for creating a superuser which can be used in admin page. If you want to launch the command, you supposed to perform 'python manage.py create_superuser'.
2. '.enw.example' (this is the sample of environment variables).
3. 'requirements.txt'.

How to launch Project:
1. Open Ubuntu and perform "curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg ".
2. Perform "sudo apt-get update" and then "sudo apt-get install redis".
3. Perform "sudo service redis-server start".
4. Perform in the terminal "python manage.py runserver".
5. Perform 'celery -A config worker -l INFO'.
6. Perform 'celery -A config worker -P eventlet'.
