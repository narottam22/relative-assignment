#!/usr/bin/env python

import sys
import yaml
from yaml2object import YAMLObject
from subprocess import run


# Load the configuration file

with open("./config.yaml", "r") as f: 
    cfg = yaml.safe_load(f)
config=YAMLObject('Config', (object,), \
  {'source': cfg, 'namespace': 'Config'})

arg_list=sys.argv
num_args=len(arg_list)
mode=arg_list[num_args-1].strip()

built_image=config.fastapi_app.built_image
container_name=config.fastapi_app.app_container_name

if(mode=="start"): 
    run_cmd = 'docker run -d --network int_net -p 8989:8000 --name '+container_name+' '+built_image

    docker_run=run(run_cmd, shell=True)

if(mode=="clean"):
    stop_cmd = 'docker stop '+container_name

    docker_stop=run(stop_cmd, shell=True)

    remove_cmd = 'docker rm '+container_name

    docker_remove=run(remove_cmd, shell=True)