#region ubuntu 16.04 with python ref. https://gist.github.com/monkut/c4c07059444fd06f3f8661e13ccac619
FROM ubuntu:16.04

# install python 3.6.x
RUN apt-get update && \
  apt-get install -y software-properties-common && \
  add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update
RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv

# make binary python linked to python3.6
RUN ln -s /usr/bin/python3.6 /usr/bin/python

# update pip
RUN python -m pip install pip --upgrade
RUN python -m pip install wheel

#endregion ubuntu 16.04 with python ref. https://gist.github.com/monkut/c4c07059444fd06f3f8661e13ccac619


# create THIS_APP folder
WORKDIR /app

# install pipenv
RUN python -m pip install pipenv

# copy pip packages
COPY ./Pipfile      .
COPY ./Pipfile.lock .

# force-rebuild tag - change _x to new value to invalidate .venv/ and force a rerun
RUN echo 191020_x

# set utf8 to fix error > Click will abort further execution because Python 3 was configured to use ASCII as encoding for the environment  # ref. https://github.com/docker-library/python/issues/13#ref-pullrequest-164133459
ENV LANG=C.UTF-8

# bundle app source
COPY . .

# copy .env used for dockerized mode - NOTE this .env is in folder bin/docker/ and to link the api container with the postgres container
COPY ./bin/docker/config.py .

# for documentation on port
EXPOSE 8000

# Default command when running container
# Run the api at 8000
CMD cd /app; \
    pipenv --rm; \
    pipenv sync; \
    pipenv run  gunicorn  Customer.app:api                    -b "0.0.0.0:8000"        --reload
                          #path to falcon api instance   #bind to address:port    #auto reload api if code changed
