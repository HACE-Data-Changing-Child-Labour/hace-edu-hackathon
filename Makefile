start:
	docker-compose up

stop:
	docker-compose down 

build:
	docker-compose build

clean:
	docker-compose down -v --rmi all --remove-orphans

