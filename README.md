# cld.sh api
runs on pypy v7.3.5

to build
```sh
docker build -t "kaz2.sh-api" .
docker run -d --net="host" --name="api.kaz2.sh" "kaz2.sh-api/latest"
```
