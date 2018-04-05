#!/bin/bash

instance=$1
constraints=$2


for csvFile in $(eval ls "$HOME/Documents/MINOBS-anc/data/${instance}_*.csv"); do

	for constraintFile in $(eval ls "$HOME/Documents/MINOBS-anc/data/constraints/$constraints/*"); do

		eval "./run-one-test.sh $csvFile $constraintFile $instance"

	done
done
