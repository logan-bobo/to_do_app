env:
	source ./.env.local
	docker-compose up

destroy:
	docker system prune -a -f --volumes