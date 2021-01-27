# DVC (Data Version Control)

[Documentation](https://dvc.org/doc/start)

## Store AWS S3 Bucket Keys

 * `export AWS_ACCESS_KEY_ID=’’xxx”`
 * `export AWS_SECRET_ACCESS_KEY=”xxx”`

## Initialise DVC & add new remote link
 
 * `git init` > `dvc init`
 * `dvc remote add -d nameforbucketfolder s3://bucketname/folder_name`

## Push Images to S3

 * `dvc add data/testimages_module1`: a `.gitignore`file with the blob folder will be added so this will not be saved to the code repository. hashes for each blob will be created & stored in `.dvc/cache`
 * `dvc push`: send updates to S3 bucket
 * `dvc push -d example` or `dvc push example.dvc`: note that it will be pushed to the default remote, which might not be the remote where you initially pushed to

## Switch Remote Core

 * `dvc remote default remotename`
 * `dvc remote list`: list all remotes
 * `cat .dvc/config`: list all remotes & default

## Pull Images

 * `dvc pull`: pull all data from all remotes
 * `dvc pull -d example` or `dvc pull example.dvc`: pull from specific `example.dvc`. No need to switch to remote

## dvc list

 * `dvc remote list`: show all remote connections, could be a diff source or folder
 * `.dvc/config`: details of remote connections

## Remove DVC folder & Clear Cache
 
 * `dvc remove example`: removes example.dvc & folder from .gitignore
 * `du -sh .dvc/cache`: check cache size
 * `du gu --workspace`: clear objects in cache that are unused in workspace