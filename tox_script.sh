# Create containers 
docker-compose up -d

# Open Django container to run tests
docker exec django01 python manage.py test
