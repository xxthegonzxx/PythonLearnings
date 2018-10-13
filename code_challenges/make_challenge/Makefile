# Deploys test application on 3 different environments to an s3 example test bucket.

dev:
	git checkout dev
	tar -czf app.tar.gz ./app.py
	aws s3 cp app.tar.gz s3://example-bucket/app-dev.tar.gz

demo:
	git checkout demo
	tar -czf app.tar.gz ./app.py
	aws s3 cp app.tar.gz s3://example-bucket/app-demo.tar.gz

prod:
	git checkout prod
	tar -czf app.tar.gz ./app.py
	aws s3 cp app.tar.gz s3://example-bucket/app-prod.tar.gz

