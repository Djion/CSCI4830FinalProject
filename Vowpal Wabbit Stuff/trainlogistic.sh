#trainlogistic.sh
rm reddit.model
vw -f reddit.model --passes=10 --cache_file=reddit.cache --kill_cache --ngram 2 --loss_function=logistic < train.vw