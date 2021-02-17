set -e 

# Create containers 
sudo docker-compose up -d

# Wait to make sure the django container is started
sleep 12

# Open Django container to run tests
sudo docker exec api python manage.py test

sudo docker exec api coverage run --source='sc2league_server/' manage.py test sc2league_server/

sudo docker exec api coverage xml

sudo docker exec api mv coverage.xml tests/
