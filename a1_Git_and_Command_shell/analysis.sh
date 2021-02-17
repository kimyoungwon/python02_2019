#!/usr/bin/env bash 
## analysis.sh

cd sonnets

#Clean up old files
rm sonnet*
rm cleaned*
rm lengths.txt
rm truth.txt
rm love.txt

# Download the sonnets
curl -s http://www.gutenberg.org/files/1041/1041.txt > sonnets.txt

# Trim introduction and concluding lines and Remove leading blank characters 
tail -n 2986 sonnets.txt | head -n 2618 | cut -c 3-56 > cleaned-sonnets.txt

# Split sonnets into individual files. This will involve *many* commands.
head -n 1666 cleaned-sonnets.txt > sonnet-1
split -l 17 sonnet-1 sonnet-1-

tail -n 951 sonnets.txt | head -n 18 > sonnet-2-aa

tail -n 933 sonnets.txt | head -n 459 > sonnet-3
split -l 17 sonnet-3 sonnet-3-

tail -n 491 sonnets.txt | head -n 14 > sonnet-4-aa

tail -n 476 sonnets.txt > sonnet-5
split -l 17 sonnet-5 sonnet-5-

rm sonnet-1
rm sonnet-3
rm sonnet-5

# Find the longest sonnet (most words)
wc -m sonnet-* | sort -r > lengths.txt

# Search for specific words in  the sonnets
grep -F truth sonnet-* > truth.txt
grep -F love sonnet-*-*a > love.txt

#Add my shell script and analysis result files
git add ../analysis.sh
git add lengths.txt
git add truth.txt
git add love.txt

# Commit my change to git (with a descriptive message)
git commit -m "Add sonnet analysis"

