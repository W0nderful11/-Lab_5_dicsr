# Mini-MapReduce Lab

## Dataset
Wikipedia text dump (small sample).

## Run Command
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
 -files mapper.py,reducer.py \
 -mapper mapper.py \
 -reducer reducer.py \
 -input /user/hadoop/input/corpus.txt \
 -output /user/hadoop/output
