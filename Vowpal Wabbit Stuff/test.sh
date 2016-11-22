#test.sh
vw -i reddit.model -t -p ./predictions.txt < test.vw
python3 accuracy.py