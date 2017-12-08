#!/bin/expect
# Usage:
# sudo apt install expect
# expect ssh.sh

set timeout 30
spawn ssh hpccsg@202.120.58.231
expect "Password:"
send "971016\r"
interact
