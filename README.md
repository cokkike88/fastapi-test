## Run app
uvicorn main:app --reload

## Create requirements file
pip freeze > requirements.txt


## Up image to AWS ECR
- If the repository doesn't exist we need to create the repository 
https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html

- login
```
aws ecr get-login-password --region {region} | docker login --username AWS --password-stdin {account-id}.dkr.ecr.{region}.amazonaws.com
```
- tag the image
```
docker tag fastapi-test:latest {account-id}.dkr.ecr.{region}.amazonaws.com/fastapi-test
```
- up the image
```
docker push {account-id}.dkr.ecr.{region}.amazonaws.com/fastapi-test
```