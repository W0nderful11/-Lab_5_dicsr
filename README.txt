# Mini-MapReduce on Amazon EMR

This repository contains the Python MapReduce code for Lab 5 (IT-2305).

## Files
- `mapper.py`: Processes input text and outputs (word, 1).
- `reducer.py`: Aggregates word counts.

## Dataset
Wikipedia text dump (small sample) downloaded from:
https://github.com/LGDoor/Dump-of-Simple-English-Wiki

## Run Command (Hadoop Streaming)
```bash
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
 -files mapper.py,reducer.py \
 -mapper mapper.py \
 -reducer reducer.py \
 -input /user/hadoop/input/corpus.txt \
 -output /user/hadoop/output
