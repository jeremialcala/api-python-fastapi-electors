#!/bin/bash
rm -rf api-python-fastapi-electors/
git clone https://github.com/jeremialcala/api-python-fastapi-electors.git
cp config.env api-python-fastapi-electors/ || exit
cd api-python-fastapi-electors/ || exit
git checkout develop
git pull

docker rm -f api-python-fastapi-electors
docker rmi api-python-fastapi-electors
docker system prune -a -f
docker build -t api-python-fastapi-electors:latest .
docker run -it -p 5003:5002 --name api-python-fastapi-electors -d api-python-fastapi-electors
