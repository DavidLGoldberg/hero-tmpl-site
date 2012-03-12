Initial Steps:
=============
* ensure:
    sudo apt-get install python-dev libevent-dev
* ensure:
    sudo gem install watchr
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
* Fix baseurl to not redirect to index.html
