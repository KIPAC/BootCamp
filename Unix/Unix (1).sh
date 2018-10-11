# Intro to Unix
# File system
ls /
ls -la /
pwd
cd
cd specific dir
cd ..
cd -
cd ~

ls ~
mkdir newdir
cd newdir

wget https://raw.githubusercontent.com/KIPAC/BootCamp/master/Unix/files_for_practice.tar.gz
tar -xzf files_for_practice.tar.gz

cd files_for_practice/random_files
mkdir mp3
mv *.mp3 mp3
mkdir est
cp est.* est
mv architecto.mp3 consequuntur.html
rm -i molestias.css

# Read text files
tail -n 2 users.txt
head -n 3 clients.txt

# Where are these programs?
which tar
which wget
which which

# The PATH environment variable stores the directories the shell searches when it is told a command
echo $PATH

# File permissions
cd ../executables
./wget
./tar

chmod u+x tar
./tar

chmod u-r alphabet.txt
cat alphabet.txt
chmod u+r alphabet.txt
cat alphabet.txt

# I/O redirection
command < input_file
command > output_file
command < input_file > output_file

# append
command >> output_file

# use stdout from command1 as stdin of command2
command1 | command2

# for example if we want to pass in alphabet.txt to reverse we use
chmod u+x reverse
./reverse < alphabet.txt

# how many files are in a directory?
# use one program to list the files
# use another program to count
cd ../random_files
ls -l | wc -l
ls -l *.png | wc -l

cd
# grep
grep ^d users.txt
grep ^d *.txt
ls -l | grep -E i.\.mp3

# search grepdata.txt for all lines that do not begin with a capital letter
grep '^[^A-Z]' grepdata.txt

# sed
# sed 's/phrase/replacement/' filename
sed 's/\./SPAM/' users.txt
sed -i.bak 's/\./SPAM/' users.txt

# awk
ls -l | awk '{print $1}'

# ps and kill
ps
kill

# Editing your .bashrc
alias ll="ls -larth"
alias farmshare="ssh rice.stanford.edu"
cdls() { cd "$@" && ls; }

# Screen and Notebook
# Useful for daily workflow like keeping a kernel running, but not intended to run long jobs.
screen -S jupyter
jupyter notebook --port=1738 --no-browser
ssh -t -L 1738:localhost:1738 rice.stanford.edu
screen -X -S myscreen quit

