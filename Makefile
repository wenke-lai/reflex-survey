dev:
	reflex run --loglevel debug

requirements:
	poetry export -f requirements.txt --output requirements.txt

build: requirements
	reflex export --no-zip --loglevel debug

deploy: build
	# aws s3 cp .web/_static s3://$(BUCKET_NAME) --recursive
	# docker build -t $(IMAGE_NAME) .
	# docker push $(IMAGE_NAME)
