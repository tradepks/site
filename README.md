# site
Install Python35 to c:\Python35 (installation dir can be choosen during installation steps)

Open command prompt and execute below 

set PATH=c:\python35;c:\python35\scripts;%PATH%

git clone https://github.com/tradepks/site.git

cd site

pip install -r requirements.install

python manage.py migrate

python manage.py runserver


#check 

http://localhost:8000/

http://localhost:8000/environ


Above would ask for login, Signup, it sends activation mail , Activate and then access 



#After Any Change 

git add -A

#config only for one time
git config --global user.email "tradepksfounder@gmail.com"

git commit -m "some comment"

git push origin master

