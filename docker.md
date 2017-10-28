## Docker

Installation
https://docs.docker.com/engine/installation/

Post Installation
https://docs.docker.com/engine/installation/linux/linux-postinstall/#manage-docker-as-a-non-root-user



### Some Docker Commands

`docker images`   --see all installed docker images

`docker rm -f container_name` --(-f = force) remove image from docker

`docker rmi image_name` --remove image from docker

`docker start image_name` --run image

`docker stop image_name`  --stop image from running

`docker ps`  --show status of images which are running

`docker exec -it <containerIdOrName> bash`  --enter into container using bash

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

`docker run --name "geoserver" -v ~/Users/xxx/docker/geoserver:/geoserver_data/data -d -p 8080:8080 kartoza/geoserver`
  * `/geoserver_data/data`: where all data is stored
  * Username: admin
  * Password: geoserver



