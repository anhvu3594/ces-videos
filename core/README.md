Steps to start

- Start with docker 
-- Read file README.md in .docker folder
Install docker and docker compose
Go to this folder:
cd .docker
docker build -t ces_videos:1.0 . 
cd ..
docker-compose up

- Start with python
python manage.py migrate

python manage.py runserver 0.0.0.0:80
