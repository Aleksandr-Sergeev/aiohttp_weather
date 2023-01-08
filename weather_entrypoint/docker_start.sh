#!/bin/sh

#!/bin/sh
# Exit immediately if a command exits with a non-zero status.
# http://stackoverflow.com/questions/19622198/what-does-set-e-mean-in-a-bash-script
set -e

case "$1" in
    "$@")
        supervisord -n -c -l /etc/supervisor/supervisord.conf
    ;;

esac