## Docker

Installation
https://docs.docker.com/engine/installation/

Post Installation
https://docs.docker.com/engine/installation/linux/linux-postinstall/#manage-docker-as-a-non-root-user
to prevent typing sudo for docker commands use the below to add a user to docker

`sudo groupadd docker`

`sudo usermod -aG docker $USER`


## Some Notes

One of the most important configuration for docker is to create a data folder that links from the os to the container data directory.
This is designated by the `-v path/in/os/folder:/default/path/of/software/data/directory/in/container`

### Some Docker Commands

`docker images`   --see all installed docker images

`docker rm -f container_name` --(-f = force) remove image from docker

`docker rmi image_name` --remove image from docker

`docker start image_name` --run image

`docker stop image_name`  --stop image from running

`docker ps`  --show status of images which are running

`docker exec -it <containerIdOrName> bash`  --enter into container using bash

`docker cp container_name:container_path local_path`  --copy container contents to local drive

`docker cp local_path container_name:container_path`  --copy local drive contents to docker

`exit`  --exit from docker bash

### PostGreSQL
https://hub.docker.com/_/postgres/

Simple Install
  * `docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres`

Detail Install
  * `docker run --name some-postgres -v /home/xxxx/postgresdata:/var/lib/postgresql/data -p 5432:5432 --restart=always -e POSTGRES_DB=postgres -e POSTGRES_USER=xxxx -e POSTGRES_PASSWORD=xxxx -d postgres`   
      * `--name`: name of docker container
      * `-v`: (volume) mount image on a created directory called postgresdata, with container directories /var/lib/postgresql/data
      * `-p`: (port) expose postgres port
      * `restart`: start docker image when os restarts
      * `POSTGRES_PASSWORD`: password
      * `-d`: name of database
      * `postgres`: name of image

  * Note that default username is postgres

  
### GitLab CE
https://docs.gitlab.com/omnibus/docker/README.html#install-gitlab-using-docker-compose


### GeoServer
https://hub.docker.com/r/kartoza/geoserver/

`docker run --name "geoserver" -v /home/xxxx/geoserverdata:/opt/geoserver/data_dir -d -p 8080:8080 kartoza/geoserver`
  * `/opt/geoserver/data_dir`: where all data is stored (note it varies with containers)
  * Url: `localhost:8080/geoserver`
  * Username: admin
  * Password: geoserver




