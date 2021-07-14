ECR_URO = ${ECR_URO}

up:
	docker-compose up -d
down:
	docker-compose down
run: 
	uvicorn main:app --reload

build:
	docker build --no-cache -t stanlee321/fastapi_scraper:latest -f ./Dockerfile .

tag:
	docker tag stanlee321/fastapi_scraper:latest ${ECR_URO}/sicoes/fastapi:latest

push:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${ECR_URO}
	docker push ${ECR_URO}/sicoes/fastapi:latest

.PHONY: up down run build tag push