# stagelight_docker

alias killdocker='docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q) && docker rmi $(docker images -a -q) && docker volume prune'
