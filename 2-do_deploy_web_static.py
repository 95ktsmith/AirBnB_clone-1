#!/usr/bin/python3
""" Deploy web static """
from fabric.api import *
import os

env.hosts = ['104.196.50.109', '34.75.56.79']


def do_deploy(archive_path):
    """ Deploys an archive to web servers """
    if os.path.exists(archive_path):
        try:
            filename = archive_path[archive_path.find('/') + 1:
                                    archive_path.find('.')]
            put(archive_path, "/tmp/")
            run("sudo mkdir /data/web_static/releases/{}".format(filename))
            run("sudo tar -zxf /tmp/{}.tgz -C /data/web_static/releases/{}".
                format(filename, filename))
            run("sudo rm /tmp/{}.tgz".format(filename))
            run("sudo rm /data/web_static/current")
            run("sudo ln -s /data/web_static/releases/{}\
                 /data/web_static/current".format(filename))
            return True
        except:
            return False
    else:
        return False
