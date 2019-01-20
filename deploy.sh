SERVER_IP=35.233.140.84
CONTAINER_NAME=klt-enigma-shell-mhxn
DOCKER_REPO=arunscape/enigma-shell

ssh $SERVER_IP "docker stop $CONTAINER_NAME; docker pull $DOCKER_REPO; docker run -p 80:80 --rm $DOCKER_REPO"
