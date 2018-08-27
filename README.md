# Keras introduction

Picking up keras library with Tensorflow backend.

All projects focus on deep learning specifically to supplement my work.

Mainly example datasets.

## Don't forget!

Windows linux subsystem (this project doesn't work on linux subsystem)

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6

#change to directory
cd /mnt/d/Users/Tom/Documents/
mkdir keras

#activate using python3.6
python3.6 -m venv venv

source venv/bin/activate

python --version 
[Console]: Python 3.6.6
```

## Doesn't work on Windows linux subsystem

Project doesn't look like it can be completed using plaidML without using powershell. WLS won't recognise graphics card currently.

Switched to MINGW64, command key difference in installing on Windows is this line!!! Because MINGW64 is superficial the files created are windows files so activation is Scripts in venv and not bin.

source venv/Scripts/activate

## Hardware

- R280x (2048 cores)