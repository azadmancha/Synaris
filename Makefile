install:
	python -m pip install -r requirements.txt

frontend-install:
	cd apps/web && npm install

build:
	python -m compileall apps/api/app
	cd apps/web && npm install && npm run build

docker-up:
	docker compose up --build
