# best-practices
## Description
The program, get_column_stats.py calculates the mean and stadard deviation of a specified 
column in a supplied input file.
This repository also contains a bash script for functional testing called
basics_test.sh

## Usage
to run get_column_stats.py, you must pass a file with x number of columns
and y rows. additionally you must pass a column number that is an integer
less than or equal to x. The program will calculate the mean and stdev of
the specified column number

## Installation
To install python, we first have to install homebrew
'''
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
export PATH="/usr/local/opt/python/libexec/bin:$PATH"
'''
Next, install python3 using homebrew
'''
brew install python
'''
Now we can install conda 
'''
cd $HOME
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b
. $HOME/miniconda3/etc/profile.d/conda.sh
conda update --yes conda
conda config --add channels bioconda
echo ". $HOME/miniconda3/etc/profile.d/conda.sh" >> $HOME/.bashrc
'''
create an environment and activate it
'''
conda create --yes -n my_env
conda activate my_env
'''
install argparse and pycodestyle using conda
'''
conda install pycodestyle
conda install argparse
'''
after cloning the repository, test to see whether any errors are thrown
'''
bash basics_test.sh
'''
This sould exit with no Failures
Next you can try running get_col_stats.py on your own data
'''
python get_col_stats.py --file_name your_file_here.txt --col_num 1
'''

