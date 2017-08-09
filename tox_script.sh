# Create containers 
sudo docker-compose up -d

# Wait to make sure the django container is started
sleep 12

# Open Django container to run tests
sudo docker exec django01 python manage.py test

sudo docker exec django01 coverage run --source='.' manage.py test
