REPO_NAME=enigma-shell

docker login --username $DOCKER_HUB_USER --password $DOCKER_HUB_PSW

# build the docker image and push to an image repository
docker build -t $REPO_NAME .
docker tag $REPO_NAME $DOCKER_HUB_USER/$REPO_NAME
docker push $DOCKER_HUB_USER/$REPO_NAME
