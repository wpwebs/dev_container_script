
### commands
```sh
# Preparing ssh_key
mkdir -p .ssh && cp ~/.ssh/ssh_key* .ssh/

# define project name
project=hotdeals
# build image
docker build -f .devcontainer/Dockerfile  -t $project-image .
# run docker
docker run -d --name $project -p 80:80 $project-image
docker run -d --name $project $project-image

# debug
docker run --name $project -p 80:80 $project-image
# remove docker
docker rm $project -f  

docker image list
docker image rm $project-image

docker run --name $project -it --entrypoint /bin/bash $project-image

docker exec -it $project /bin/zsh

