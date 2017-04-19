# dead-command
DEAD Command - Django Easy Applications Development

`Command line interface`


**Usage:**

* Install package:
    ```bash
    pip install -U git+https://github.com/000dead000/dead-command.git
    ```
  
* Start a new project:
    ```bash
    # -n Name of the project (default: deadproject)
    # -b Project parent directory (default: current)
    # -o Overwrite directory if exists
    # -e Run extra tasks like migrations and create system users
     
    dead-command.py startproject [-n PROJECT-NAME] [-b PROJECT-BASE-DIR] [-o] [-e]
    ```
    
    Example:
    
    ```bash
    useraricalso@000rayuela000:~$ cd ~/instances
    aricalso@000rayuela000:/home/aricalso/instances$ mkvirtualenv deadvenv
    (deadvenv) aricalso@000rayuela000:/home/aricalso/instances$ pip install -U https://github.com/000dead000/dead-command.git
    (deadvenv) aricalso@000rayuela000:/home/aricalso/instances$ dead-command.py startproject -n deadtest -b ~/instances
    ```

* Install/Update bower dependencies:
    ```bash
    dead-command.py bower_dependencies
    ```

* Install/Update Operating System dependencies:
    ```bash
    dead-command.py os_dependencies
    ```

* Install/Update pip dependencies:
    ```bash
    dead-command.py pip_dependencies
    ```

* Update dead-command package:
    ```bash
    dead-command.py update
    ```
    
* Run migrations:
    ```bash
    # This runs makemigrations and migrate
     
    dead-command.py migrate
    ```

* Run live server port 9500:
    ```bash
    # This runs liverserver at port 9500
     
    dead-command.py liveserver
    ```

* Create if not exists system users:
    ```bash
    # This command create system users
    # admin/admin, superuser, is_staff
    # support/admin, superuser, is_staff
    # system/?, normal user
     
    dead-command.py system_users
    ```
