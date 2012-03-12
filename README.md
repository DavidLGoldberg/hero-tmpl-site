Initial Steps:
=============
* ensure:
    sudo apt-get install python-dev libevent-dev
* run:
    heroku create --stack cedar
* run:
    heroku scale web=1
* Add title
* Adjust humans.txt


After launch:
==============
* index.html: remove NOINDEX, NOFOLLOW
* robots.txt: remove disallow /

TODO:
==============
* Actually, it works, if I add in /public/index.html! (Fix this!)
