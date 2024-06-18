postgres-up: ## run test postgres
	docker run \
	--name pst \
	-e POSTGRES_USER=pst \
	-e POSTGRES_PASSWORD=pst \
	-e POSTGRES_DB=pst \
	-p 5432:5432 \
	-d postgres:12.5-alpine

postgres-cli:
	docker exec -it pst psql -U pca -d pca