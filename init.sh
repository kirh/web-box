#nginx
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#gunicorn
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart
#mysql
sudo /etc/init.d/mysql start
sudo mysql -uroot -e "CREATE DATABASE Ask"
sudo /home/box/web/ask/manage.py syncdb