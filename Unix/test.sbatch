#!/bin/bash
#SBATCH --job-name=test
#SBATCH --time=00:00:05
#SBATCH -p iric 
#SBATCH -o /home/users/swmclau2/Git/BootCamp/Unix/test.out
#SBATCH --ntasks=2

python test.py 
