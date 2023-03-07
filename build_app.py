#!/usr/bin/env python

import sys
import yaml
import os
import shutil
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


base_image=config.fastapi_app.base_image
built_image=config.fastapi_app.built_image

if(mode=="create"):
    mk_src = run("rm -rf app; mkdir app", shell=True)

    copy_src = run("cp ./main.py ./prestart.sh app/", shell=True)

    copy_src = run("cp ./req.txt ./database.py ./models.py app/", shell=True)

    docker_build_cmd="docker build -t "+built_image+ \
        " --build-arg base_image="+base_image+ " ."

    docker_build=run(docker_build_cmd, shell=True)

if(mode=="clean"):
    docker_cmd = 'docker rmi -f $(docker images '+built_image+' -q)'
    docker_rmi=run(docker_cmd, shell=True)
    abspath_app=os.path.join(os.getcwd(),'app')
    shutil.rmtree(abspath_app)