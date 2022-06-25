# Bash

# Print Contents of File

 * `cat <filename>`: prints whole file contents
 * `head -10 <filename>`: prints first 10 lines of file
 * `tail -10 <filename>`: prints last 10 lines of file
 * `grep -R "<string>" "<filename>"`: prints contents in file that contains <string>

# Delete

 * `rm -rf /path/dir`: delete directory and contents

# File Manipulation

 * `touch Dockerfile`: create new file if not exist
 * `echo FROM python:3.7 > Dockerfile`: add echoed line to new file, replace if exist
 * `echo FROM python:3.7 >> Dockerfile`: add echoed line to existing file as new line

## Zip Files

 * `zip --encrypt secure.zip file1 file2`: enter & it will prompt u for password

## DATETIME

 * `$(date)`: display datetime

## DU

**Disk Usage**

 * `du -sh .git`: check total file size
 * `du -h -d1`: file sizes of all top level directories
 * `du -csh`: show file size in MB

## MEMORY

**Memory Usage**

 * `free`: show free & used memory
    * `free -t -g`: show total & also in gigabytes
    * `watch -n 1 free -m`: check memory every 1 sec, in Mb
    * `free -m | grep "Mem" | awk '{ print $3 }'`: output only used memory
    * `free -m | grep "Mem" | awk '{ print $4 }'`: output only free memory
 * `top`: check cpu & memory for each process [link](https://linuxaria.com/howto/understanding-the-top-command-on-linux)
    * `top -p PID`: check for specific PID
    * `top -o %MEM`: sort by memory usage
    * `top | grep python`: check by process name
    * in Live View
        * `SHIFT + e`: change size from Kb to Mb to Gb etc...
        * `SHIFT + l`: search & highlight process name 


## SCP

**Secure Copy**

 * `scp /path/to/file username@ipaddress`: copy paste files to remote server. need enter pw.
 * `scp -r directory username@ipaddress`: copy paste directory to server

## SSHPASS

**Sending Shell Commands Through SSH**

 * `sshpass -p $password ssh ubuntu@ipaddress`: ssh to server
 * `sshpass -p $password scp -r scene-understanding ubuntu@ipaddress`: copy 
 * multiple commands

```bash
sshpass -p $password ssh ubuntu@$ip <<EOF
    docker rm -f $module
    wait
    docker build -t $module $module
    wait
    yes | docker image prune
    wait
    docker run -d -p 80:$port --log-opt max-size=5m --log-opt max-file=5 --restart always --name $module $module
    docker ps
EOF
```

## JQ

**JSON Parser**

 * `cat /tmp/curl_body | jq '.'`: prints entire json file from curl_body
 * `mask=$(cat /tmp/curl_body | jq '.FACEMASK_DETECTION[0]')`: get 1st array within the value of `FACEMASK_DETECTION`
 * `mask=$(cat /tmp/curl_body | jq '.FACEMASK_DETECTION[0] .boundingPoly .normalizedVertices | length')`: get length of array
 * `cat bandit.json | jq '[.results [] | select(.issue_severity=="MEDIUM")]'`: filter
 * `cat bandit.json | jq '[.results [] | select(.issue_severity=="MEDIUM")]' | jq '. | length'`: filter and get length of array


## SED

**Stream Editor (Find/Replace)**

 * `-i` = in-place (i.e. save back to the original file)
 * `s` = the substitute/replace command
 * `g` = global (i.e. replace all and not just the first occurrence)

 * `sed -i -e 's/original_string/replacement_string/g' file/path/location`
 * `sed -i "/CMD/d" $DOCKERFILE`: remove line if contain substring


## REGEX

Save matched regex as a variable

```bash
# FROM python:3.8-slim
first_line=$(head -n 1 $DOCKERFILE)
subtext=$(egrep -o "python.+[0-9]" <<<$first_line)
# python:3.8
```

## CURL

**Client URL**

Sends POST request from JSON file

```bash
curl --header "Content-Type:application/json"
     --data @./facedetection/sample_json_request.json 
     --request POST http://docker:5003/api
```

Gets only HTTP status code and dump output to `/tml/curl_body`

```bash
statuscode=$(curl -s -o /tmp/curl_body -w "%{http_code}" http://localhost:5001)
echo $statuscode
```

Get HTTP status code without saving a hardcopy

```bash
content=$(curl -s -w "%{http_code}" http://localhost:$port)
statuscode="${content:(-3)}"
```

Sends Post request from JSON file, and exit if not status 200

```bash
content=$(curl -s -w "%{http_code}" \
                --header "Content-Type:application/json" \
                --data @./facedetection/sample_json_request.json \
                --request POST http://docker:5003/api)

statuscode="${content:(-3)}" # or {$content: -3}
response="${content%???}"

echo $response
echo "statuscode is $statuscode"   

if [[ $statuscode != "200" ]]
then exit 1 
fi
```

## Code Snippets

### Login SSH

```bash
#!/bin/bash
echo 
"
server-1  = 1
server-2  = 2
server-3  = 3
server-4  = 4
"
read -p 'select server code:' selection
password='yourpassword'

if [[ $selection == '1' ]]
then sshpass -p $password ssh ubuntu@18.1.70.9
elif [[ $selection == '2' ]]
then sshpass -p $password ssh ubuntu@18.1.20.75
elif [[ $selection == '3' ]]
then sshpass -p $password ssh ubuntu@52.2.19.40
elif [[ $selection == '4' ]]
then sshpass -p $password ssh ubuntu@18.1.07.14

fi
```

### Update Docker

```bash
#!/bin/bash
$module=facedetection
# remove existing container if any
docker rm -f $module
wait
# rebuild image
docker build -t $module $module
wait
# remove dangling image
docker image prune
wait
# run container
docker run -d -p 80:5003 --log-opt max-size=5m --log-opt max-file=5 --restart always --name $module $module
```
