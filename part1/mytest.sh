#!/bin/bash
# mytest.sh — щохвилини дописує рядок у /tmp/test.log
while true; do
  line="$(date '+%Y-%m-%d %H:%M:%S') mytest: привіт від systemd, робоча папка $(pwd)"
  echo "$line" >> /tmp/test.log
  echo "$line"
  sleep 60
done
