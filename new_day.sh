#!/bin/bash
set -euxo pipefail

day_num="$1"
task_name="$2"

day_folder="day$day_num"

cp -rv template "$day_folder"
jinja2 "$day_folder/solution.py.j2" -o "$day_folder/solution.py" -D "day_num=$day_num" -D "task_name=$task_name"
jinja2 "$day_folder/test.py.j2" -o "$day_folder/test.py" -D "day_num=$day_num" -D "task_name=$task_name"
rm -fv "$day_folder/solution.py.j2" "$day_folder/test.py.j2"