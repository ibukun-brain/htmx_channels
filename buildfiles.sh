echo " BUILD START"
python3.9.10  -m pip install -r requirements.txt
python3.9.10 manage.py collectstatic  --noinput --clear
echo " BUILD END"