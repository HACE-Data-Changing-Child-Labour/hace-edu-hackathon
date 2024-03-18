start:
	docker-compose up

stop:
	docker-compose down 

clean:
	docker-compose down -v --rmi all --remove-orphans

