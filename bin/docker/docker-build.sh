#!/usr/bin/env bash
s=$BASH_SOURCE; s=$(dirname "$s"); s=$(cd "$s" && pwd); a="$s/../..";   a=$(cd "$a" && pwd); APP_HOME=$a

# rm image
docker image rm -f 'sonvt8/falcon_intern'

# do build
cd $APP_HOME
    docker build -t 'sonvt8/falcon_intern' .
cd - 1>/dev/null

# aftermath check
check_img=`docker image ls | grep -c sonvt8/falcon_intern`
if [[ $check_img == 0 ]]; then echo 'image not found'; exit; fi
