#! /bin/bash 

pip freeze > requirements.txt

sed -i 's/==/>=/' requirements.txt

pip install --upgrade -r requirements.txt

rm requirements.txt
