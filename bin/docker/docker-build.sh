docker build -t 'sonvt8/falcon_intern' .
check_img=`docker image ls | grep -c sonvt8/falcon_intern`
if [[ $check_img == 0 ]]; then echo 'image not found'; exit; fi
