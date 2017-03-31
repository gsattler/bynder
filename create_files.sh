#!/bin/sh

OUTPUT_DIR=$1
AMOUNT=$2
PERCENTAGE=$3
COPIES=`echo "$AMOUNT / 100 * $PERCENTAGE" | bc -l`
COPIES=`printf '%.*f\n' 0 $COPIES`


cd $OUTPUT_DIR
for name in $(seq 1 $AMOUNT); do
    dd if=/dev/urandom of=$RANDOM bs=$(((RANDOM%2000+1000)*1000)) count=1;
    echo $RANDOM;
done

ls | tail -$COPIES |while read file; do cp $file $RANDOM; done
cd -