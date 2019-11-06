#!/bin/sh
set -e

function join_by { local IFS="$1"; shift; echo "$*"; }

# Find VUE_APP_ vars
vars=$(env | grep VUE_APP_ | awk -F = '{print "$"$1}')
vars=$(join_by ' ' $vars)
echo "Found variables $vars"

for file in /usr/share/nginx/html/js/app.*;
do
  echo "Processing $file ...";

  # Use the existing JS file as template
  cp $file $file.template
  envsubst "$vars" < $file.template > $file
  rm $file.template
done

envsubst < /etc/nginx/conf.d/default.template > /etc/nginx/conf.d/default.conf

exec nginx -g 'daemon off;'
