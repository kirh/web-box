#nginx
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#gunicorn
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart
#mysql
sudo /etc/init.d/mysql start
sudo mysql -uroot -e "CREATE DATABASE ask"
mysql -uroot -e "CREATE USER 'anyuser'@'localhost' IDENTIFIED BY 'any'"
mysql -uroot -e "GRANT ALL PRIVILEGES ON ASK.* TO 'any'@'localhost'"
sudo /home/box/web/ask/manage.py syncdb
