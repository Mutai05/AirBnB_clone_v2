#!/usr/bin/python3
from fabric.api import task, env
from datetime import datetime
from pathlib import Path

# Import your do_pack and do_deploy functions from the previous scripts
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'
env.key_filename = '/path/to/your/private/key.pem'


@task
def deploy():
    """
    Deploy the web_static project on both web servers.

    Returns:
        bool: True if successful, False otherwise.
    """
    # Call do_pack and store the path of the created archive
    archive_path = do_pack()

    if not archive_path:
        print('No archive created. Deployment failed.')
        return False

    try:
        # Call do_deploy using the new path of the new archive
        return do_deploy(archive_path)

    except Exception as e:
        print('Deployment failed:', str(e))
        return False


# Usage example:
# fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu
