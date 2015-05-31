#!/bin/bash
BASHRCFILE=/home/vagrant/.bashrc
PROJECT=learntime
apt-get update
apt-get -y install less gcc build-essential g++ libncurses5-dev openssl libssl-dev libxml2-dev libxslt1-dev zlib1g-dev libreadline-dev python-pip freetype* libpng* python-dev python-matplotlib libpq-dev python-dev

##
## Create a location for downloading and building packages.
##
if [ ! -d /tmp/packages ]; then
    mkdir /tmp/packages
else
    echo -*- Skipping /tmp/packages folder creation.
fi

cd /tmp/packages

if [ ! -f /opt/python34/bin/python3.4 ]; then
	##
	## Fetch the Python source.
	##
	if [ ! -f Python-3.4.2.tgz ]; then
		wget -q --no-check-certificate https://www.python.org/ftp/python/3.4.2/Python-3.4.2.tgz
	else
		echo -*- Skipping Python-3.4.1.tgz download.
	fi

	##
	## Unpack the Python tarball.
	##
	if [ ! -d Python-3.4.2 ]; then
		tar xzf Python-3.4.2.tgz
	else
		echo -*- Skipping Python tarball extraction.
	fi

	##
	## Build Python.
	##
    cd /tmp/packages/Python-3.4.2
    ./configure --prefix=/opt/python34
    make
    make install
else
    echo -*- Skipping Python 3.4 compile.
fi

cd /tmp/packages

if [ ! -f /opt/python27/bin/python2.7 ]; then
	##
	## Fetch the Python source.
	##
	if [ ! -f Python-2.7.9.tgz ]; then
		wget -q --no-check-certificate https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz
	else
		echo -*- Skipping Python-2.7.9.tgz download.
	fi

	##
	## Unpack the Python tarball.
	##
	if [ ! -d Python-2.7.9 ]; then
		tar xzf Python-2.7.9.tgz
	else
		echo -*- Skipping Python tarball extraction.
	fi

	##
	## Build Python.
	##
    cd /tmp/packages/Python-2.7.9
    ./configure --prefix=/opt/python27
    make
    make install
else
    echo -*- Skipping Python 2.7.9 compile.
fi

cd /tmp/packages

if [ ! -f /opt/postgres94/bin/psql ]; then
	##
	## Fetch the PostgreSQL source.
	##
	if [ ! -f postgresql-9.4.tar.gz ]; then
		wget -q https://ftp.postgresql.org/pub/source/v9.4.0/postgresql-9.4.0.tar.gz
	else
		echo -*- Skipping postgresql-9.4.tar.gz download.
	fi

	##
	## Unpack the PostgreSQL tarball.
	##
	if [ ! -d postgresql-9.4 ]; then
		tar xzf postgresql-9.4.0.tar.gz
	else
		echo -*- Skipping PostgreSQL tarball extraction.
	fi

	##
	## Build PostgreSQL.
	##
    cd /tmp/packages/postgresql-9.4.0
	make clean
    ./configure --prefix=/opt/postgres94 --with-openssl --with-libxml --with-libxslt
    make
    make install

else
    echo -*- Skipping PostgreSQL 9.4 compile.
fi

##
## Create a cluster.
##
pkill -9 postgres
rm -rf /var/opt/postgres94
userdel postgres
useradd postgres
mkdir /var/opt/postgres94
mkdir /var/opt/postgres94/data
chown -R postgres /var/opt/postgres94
sudo -u postgres /opt/postgres94/bin/initdb -D /var/opt/postgres94/data
PG_CONF="/var/opt/postgres94/data/postgresql.conf"
PG_HBA="/var/opt/postgres94/data/pg_hba.conf"
# Edit postgresql.conf to change listen address to '*':
sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/" "$PG_CONF"
# Append to pg_hba.conf to add password auth:
echo "host    all             all             all                     trust" >> "$PG_HBA"
# Restart so that all new config is loaded:
sudo -u postgres /opt/postgres94/bin/postgres -D /var/opt/postgres94/data -i > /var/opt/postgres94/postgres94.log 2>&1 &
##########################################################
sleep 5
sudo -u postgres /opt/postgres94/bin/createuser $PROJECT
sudo -u postgres /opt/postgres94/bin/createdb $PROJECT
#Install virtual env for python 2.7 then run using appropraite interpreter
pip install virtualenv
mkdir /var/venv
virtualenv -p /opt/python27/bin/python /var/venv/$PROJECT
export PATH=$PATH:/opt/postgres94/bin/
export LD_LIBRARY_PATH=/opt/postgres94/lib/
export DJANGO_SETTINGS_MODULE=$PROJECT.dev_vagrant

grep -q 'export PATH=$PATH:/opt/postgres94/bin' $BASHRCFILE || echo 'export PATH=$PATH:/opt/postgres94/bin' >> $BASHRCFILE
echo "PATH set"
grep -q 'export LD_LIBRARY_PATH=/opt/postgres94/lib/' $BASHRCFILE || echo 'export LD_LIBRARY_PATH=/opt/postgres94/lib/' >> $BASHRCFILE
echo "LD_LIBRARY_PATH set"
grep -q 'export DJANGO_SETTINGS_MODULE=$PROJECT.dev_vagrant' $BASHRCFILE || echo 'export DJANGO_SETTINGS_MODULE=$PROJECT.dev_vagrant' >> $BASHRCFILE
echo "DJANGO_SETTINGS set"
grep -q "alias ACTIVATE_$PROJECT='source /var/venv/$PROJECT/bin/activate'" $BASHRCFILE || echo "alias ACTIVATE_$PROJECT='source /var/venv/$PROJECT/bin/activate'" >> $BASHRCFILE
echo "ACTIVATE script set"
grep -q "alias START_$PROJECT='python /var/wwwapps/$PROJECT/$PROJECT/manage.py runserver 192.168.33.10:8000 --settings=$PROJECT.dev_vagrant'" $BASHRCFILE || echo "alias START_$PROJECT='python /var/wwwapps/$PROJECT/$PROJECT/manage.py runserver 192.168.33.10:8000 --settings=$PROJECT.dev_vagrant'" >> $BASHRCFILE
echo "Start script set"
grep -q 'sudo -u postgres /opt/postgres94/bin/postgres -D /var/opt/postgres94/data -i > /var/opt/postgres94/postgres94.log 2>&1 &' /etc/rc.local || sed --in-place '/^exit 0/i\sudo -u postgres /opt/postgres94/bin/postgres -D /var/opt/postgres94/data -i > /var/opt/postgres94/postgres94.log 2>&1 &' /etc/rc.local
echo "start postgres script set"

echo "Use ACTIVATE_$PROJECT to activate the virtual environment\n Use START_$PROJECT to start the Django server on the appropriate port \n User: root Password: root" > /etc/motd

#Activate virtual env and install pip packages
source /var/venv/$PROJECT/bin/activate
cd /var/wwwapps/$PROJECT/
sudo easy_install -U distribute
pip install -r requirements.txt

#Syncronize database and add superuser
cd $PROJECT
python ./manage.py migrate --settings=$PROJECT.dev_vagrant --noinput
python -c "from django.db import DEFAULT_DB_ALIAS as database; from django.contrib.auth.models import User; User.objects.db_manager(database).create_superuser('root', 'root@aihs.ca', 'root')"
#Start Django Server
#echo "Server is starting"
#echo "Server can be reached at 192.168.33.10:8000/monitoring"
#python ./manage.py runserver 192.168.33.10:8000 --settings=dev_vagrant
