#! /bin/sh
source /root/anaconda3/bin/activate couplet 
chmod 777 /root/Couplet/get_dataset_from_sqlite.py
python /root/Couplet/get_dataset_from_sqlite.py
if [ $? -ne 0]; then
	chmod 777 /root/Couplet/preprocess.py
	echo "preprocess start"
	python /root/Couplet/preprocess.py
	if [ $? -ne 0]; then
		echo "preprocess failed"
	else
		echo "train start"
		chmod 777 /root/Couplet/main.py
		python /root/Couplet/main.py --epochs 30
		echo "train done"
	fi
else
	echo "get_dataset_from_sqlite failed"
fi