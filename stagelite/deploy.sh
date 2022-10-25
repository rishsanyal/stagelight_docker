# $SHELL
# /bin/bash
# # source /Users/rsanyal/.bash_profile
# export WORKON_HOME='/Users/rsanyal/.virtualenvs'
# export VIRTUALENVWRAPPER_PYTHON='/usr/loca/bin/python3'
# export VIRTUALENVWRAPPER_VIRTUALENV='/usr/local/bin/virtualenv'
# source /usr/local/bin/virtualenvwrapper.sh

# source $WORKON_HOME/stagelite_side/bin/activate

# tmux new-session -d -s hello
# tmux send -t hello "source $WORKON_HOME/stagelite_side/bin/activate" ENTER

#pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start

tmux kill-session -t stagelite


tmux new-session -d -s stagelite
tmux send -t stagelite "workon stagelite_side" ENTER
tmux send -t stagelite "source $WORKON_HOME/stagelite_side/bin/activate" ENTER
tmux send -t stagelite "cd /Users/rsanyal/code/Projects/stagelite_side/stagelite" ENTER

# Command to create superuser
## python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')"
tmux send -t stagelite "python3 manage.py runserver" ENTER