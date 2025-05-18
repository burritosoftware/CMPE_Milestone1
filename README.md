# Recipe Maker
Share recipes with ease.  

![Icons](https://skillicons.dev/icons?i=py,flask,sqlite)

Created by the following:
- Zyjay C. ([@burritosoftware](https://github.com/burritosoftware))
- Stevie C. ([@xethrus-org](https://github.com/xethrus-org))
- Noah M. ([@N-Menache](https://github.com/N-Menache))

# Requirments
- [Python 3](https://python.org)
- [Git](https://git-scm.com/)
- [Required libraries in requirements.txt](requirements.txt)
# Setup
1. Make sure you have Python, Git, and pip installed on a Linux system.
2. Clone this repository and switch to it.
```bash
git clone https://github.com/burritosoftware/hw3_pythonflask
cd hw3_pythonflask
```
3. Create a virtual environment to run the app and initiate it.
```bash
python3 -m venv venv
source venv/bin/activate
```
4. Install dependencies.
```bash
pip3 install -r requirements.txt
```
5. If you would like to not use the starter database, which has example recipes and example accounts, delete it.
```bash
rm app/app.db
```
5. Initialize the database by running these commands.
```bash
flask shell
from app import db
db.create_all()
exit()
```
6. Run the application with the dev server.
```bash
python3 run.py
```

# Usage
You can sign up for an account or log in to an existing account. Logged in users can create new recipes and delete any recipe. Logged out users can only see the recipe list.

An example account and example recipes are included in the starter database `app.db`.  
Log in using username `testuser` and password `usertest`, or `tacobell` and `belltaco`. You can also sign up for a new account.
