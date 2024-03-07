#!/usr/bin/python3
from fabric.api import local, lcd
from time import strftime

def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        with lcd("web_static"):
            local("tar -czvf ../versions/web_static_{}.tgz *".format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None
