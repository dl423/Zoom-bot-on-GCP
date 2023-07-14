# Zoom-bot-on-GCP

## Overview:
- A bot that can automatically enter a specified Zoom room, share the screen, play a sequence of videos, then leave the room
- The bot design was implemented on a VM on GCP, allowing it to be scheduled to run automatically at a specified time each day

## Short Video Demo:


## Technical implementation:
- Programming language: Python
- IDE used: IDLE
- Bot was deployed on GCP (on Google Cloud)
  - A VM was created with Windows 10 image
  - Installations on the VM:
  - Pip
  - Pyautogui
  - Zoom client
  - Virtual Audio Cable
- Configurations on the VM:
  - Use Task Scheduler to set the bot program to execute on machine startup
  - Turn on automatic login
- Used Cloud Scheduler on GCP to configure the VM to startup automatically every day at a specified time. This allows the bot to play video in a Zoom room every day, in a fully automatic way

Used Python to program a bot that can automatically enter a specified Zoom room, share the screen, play a sequence of videos, then leave the room

Initially inspired by a code of Anish-Malla.
