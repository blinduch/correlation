#!/bin/bash

csvFile=$1
constraintFile=$2
instance=$3

baseCSV=$(basename ${csvFile})
baseCSVExt="${baseCSV##*.}"
baseCSV="${baseCSV%.*}"

baseConstraint=$(basename ${constraintFile})


echo "./camml.sh --priors ${constraintFile} --speed 1 ${csvFile}"
eval "{ command time -f "%U" timeout 12h ./camml.sh --priors ${constraintFile} --speed 1 --rand-seed 0 ${csvFile} results/${baseCSV}_${baseConstraint} ;} 2>> results/results_final_${baseCSV}_${baseConstraint}.txt"
eval "egrep \"(node | *parents)\" results/${baseCSV}_${baseConstraint}.dne > results_parsed_${baseCSV}_${baseConstraint}.txt"

eval "echo ${baseCSV} >> results/results_final_${baseCSV}_${baseConstraint}.txt"
eval "echo ${baseConstraint} >> results/results_final_${baseCSV}_${baseConstraint}.txt"


eval "python3 parse_bn_log.py results_parsed_${baseCSV}_${baseConstraint}.txt results/results_final_${baseCSV}_${baseConstraint}.txt"

rm results/"${baseCSV}_${baseConstraint}.dne"
eval "rm results_parsed_${baseCSV}_${baseConstraint}.txt" 