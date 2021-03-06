SERVER_IP=35.233.140.84
CONTAINER_NAME=klt-enigma-shell-mhxn
DOCKER_REPO=arunscape/enigma-shell

#echo $PUBLIC_DEPLOY_KEY > $HOME/.ssh/known_hosts
eval "$(ssh-agent -s)"
chmod 600 ./deploy_key
echo -e "Host $SERVER_IP\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config
ssh-add ./deploy_key
ssh -i ./deploy_key $USER_LOGIN@$SERVER_IP "docker stop $CONTAINER_NAME; docker pull $DOCKER_REPO; docker run --name $CONTAINER_NAME -p 80:80 --rm $DOCKER_REPO"
