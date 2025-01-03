#!/bin/bash

echo "Make sure you've pasted this script correctly. The web terminal has a limited paste capacity."

if [ -z "$TMUX" ]; then
  echo "You are not inside a tmux session. Cowardly refusing to proceed. Use: apt update && apt install -y tmux && tmux new"
  echo "Later in a another shell, you can get back using: tmux attach"
  exit 1
fi

if [ -z "$1" ]; then
    echo "Pass the current pod Jupyter URL as the first parameter."
    exit 1
fi

cd /

apt update

apt install -y micro

apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev liblzma-dev libffi-dev uuid-dev
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> /root/.bashrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> /root/.bashrc
echo 'eval "$(pyenv init - bash)"' >> /root/.bashrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> /root/.profile
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> /root/.profile
echo 'eval "$(pyenv init - bash)"' >> /root/.profile
/root/.pyenv/bin/pyenv install 3.12.8
/root/.pyenv/bin/pyenv global 3.12.8

cd /workspace
git clone https://github.com/matous-volf/political-leaning-prediction

cd political-leaning-prediction
pip install -r requirements.txt

echo "Starting the Jupyter server. Transfer the data using either runpodctl or the Jupyter web interface and get to work!"

export PYTHONPATH="$PWD:$PYTHONPATH"
jupyter notebook --no-browser --ip=0.0.0.0 --port=8888 --allow-root --NotebookApp.allow_origin="$1"
