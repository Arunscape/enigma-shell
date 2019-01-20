REPO_NAME=enigma-shell

echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin

# build the docker image and push to an image repository
docker build -t $REPO_NAME .
docker tag $REPO_NAME $DOCKER_USERNAME/$REPO_NAME
docker push $DOCKER_USERNAME/$REPO_NAME
