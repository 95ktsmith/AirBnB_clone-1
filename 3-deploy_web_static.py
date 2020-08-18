#!/usr/bin/python3
""" Full Deploy """
from datetime import datetime
from fabric.api import *
import os

env.hosts = ['104.196.50.109', '34.75.56.79']


def deploy():
    """ Full deploy """
    pack = do_pack()
    if pack is None:
        return False
    return do_deploy(pack)


def do_pack():
    """ Generates a .tgz archive from web_static directory """
    # Generate filename
    time = datetime.now().timetuple()
    time_str = ""
    for index in range(0, 6):
        time_str = time_str + str(time[index])
    filename = "versions/web_static_" + time_str + ".tgz"

    # Create destination directory if it doesn't exist
    if not os.path.exists("versions"):
        local("mkdir versions")

    # Compress directory
    local("tar -cvzf " + filename + " web_static")

    # Test if successful
    if os.path.exists(filename):
        return filename
    else:
        return None


def do_deploy(archive_path):
    """ Deploys an archive to web servers """
    if os.path.exists(archive_path):
        try:
            filename = archive_path[archive_path.find('/') + 1:
                                    archive_path.find('.')]
            ext = archive_path[archive_path.find('.') + 1:]
            put(archive_path, "/tmp/")
            run("sudo mkdir /data/web_static/releases/{}".format(filename))
            run("sudo tar -zxf /tmp/{}.tgz -C /data/web_static/releases/{}".
                format(filename, filename))
            run("sudo rm /tmp/{}.tgz".format(filename))
            run("sudo mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}".format(filename, filename))
            run("sudo rmdir /data/web_static/releases/{}/web_static".
                format(filename))
            run("sudo rm /data/web_static/current")
            run("sudo ln -s /data/web_static/releases/{}\
                 /data/web_static/current".format(filename))
            return True
        except:
            return False
    else:
        return False
