## GNU/LINUX BASIC COMMAND INTRODUCTION
1. Handling files and directories
2. Handling file contents
3. Job control
4. User management & file access rights
5. Compressing and archiving

---
1. **Handling files and directories**
    > cd ls mkdir rmdir cp mv rm 
2. Handling file contents
3. Job control
4. User management & file access rights
5. Compressing and archiving

--
change directory
```bash
cd <dir> # change the current directory to <dir>

cd ./  # current directory
cd ../ # parent directory
cd ~/  # home dir, /home/$USER/, $HOME
cd -   # go back to the previous current directory
pwd    # print working directory 
```
![cd](./images/bash_cd.svg)

--
listing files
```bash
ls [opt] <file_name/directory_name>

ls -a    # list all files
ls -l    # list files in long format
ls -ltr  # long list, most recent files at the end
ls *html # list all files end with "html"
ls c*    # list all files/directories start with "c"
ls -d c* # list only directories start with "c"
```
--
![ls](./images/bash_ls.svg)

--
Directory manipulation
```bash
mkdir [opt] <directory_name>
rmdir [opt] <dir>

mkdir dir1 dir2 dir3
mkdir -p parent_dir/child_dir/sub_dir # make parents
rmdir dir1 dir2 dir3 # only works when directories empty
```
![mkdir](./images/bash_dir.svg)

--
copy file
```sh
cp [opt] <source_file> <target_file>

cp file1 file2 file3 ... dir    # copy the files to target directory
cp -r <source_dir> <target_dir> # copy the whole directory
mv <old_name> <new_name>        # rename the given file/directory
```
![bash ls](./images/bash_cp.svg)

--
create & remove file
```sh
touch <file>
rm [opt] file1 file2 file3 ...

rm file1 file2 file3
rm -r dir_a dir_b dir_c # recursively remove directories
rm -rf dir_b            # force remove directories
```
![bash ls](./images/bash_file.svg)

---
1. Handling files and directories
2. **Handling file contents**
    > cat more less find grep
3. Job control
4. User management & file access rights
5. Compressing and archiving

--
concatenate and print files
```bash
cat <file>
more <file>     # displaying the contents of file by page
less <file>     # does more than more with less
head -n <file>  # first n lines
tail -n <file>  # last n lines
tail -f <file>  # continues to display new lines
```
![bash cat](./images/bash_cat.svg)

--
Searching for files
```bash
find path [opt] [expression]
    -name # find by name
    -iname # find by name with insensitive mode
```
![bash find](./images/bash_find.svg)

--
Searching within files
```bash
grep [opt] <patern> <files>
    -c display the number of matched lines
    -i case insensitivity
    -l display the filenames
    -n display the line numbers
    -w match whole word
    -r recursively    
```
![bash grep](./images/bash_grep.svg)

--
wildcards
*?

--
reglar expression



---
1. Handling files and directories
2. Handling file contents
3. **Job control**
    > ps top kill bg fg jobs
4. User management & file access rights
5. Compressing and archiving

--

```bash
ps -f # full list
ps -e # all processes
ps ux
ps aux
```

--

```
ctrl + c # kill current running process
ctrl + z # stop current running process
```

--

```
jobs # background or suspended processes
fg   # Move job to the foreground
bg   # Move jobs to the background
```
--

```
kill <signal> <process-id>
killall <process-name>
```

--

![bash jobs](./images/bash_jobs.svg)

---
1. Handling files and directories
2. Handling file contents
3. Job control
4. **User management & file access rights**
    > chmod sudo
5. Compressing and archiving

--
```bash
chmod <permissions> <files>

chmod +w    # add write permissions to user/group/other
chmod u-w   # remove write permissions from user
chmod a-x   # remove execute permission from all
chmod g-w file # deny write acess for group
chmod a+rx file # add read and execute for all
chmod -R a+rw # add read/write to all recursively
```
![bash chmod](./images/bash_chmod.svg)

--
getfacl/setfacl

--
sudo

```bash
sudo [opt] [user] command
```
![bash sudo](./images/bash_sudo.svg)

---
1. Handling files and directories
2. Handling file contents
3. Job control
4. User management & file access rights
5. **Compressing and archiving**
    > gzip/gunzip bzip2/bunzip2 tar

--
gzip
```bash
g[un]zip <file>
b[un]zip2 <file>
tar cvf <archive> <file or directories>

tar czvf temp.tar.gz dir_a dir_b file1 file2
tar zxvf temp.tar.gz
```
![bash zip](./images/bash_zip.svg)

---
miscellaneous

```
$LS_COLORS
$PS1
```
--

```
- printenv
- set/export/setenv
```

--

```bash
bash as a login shell
    - /etc/profile
    - ~/.bash_profile # loaded when you login. It is read only once.
    - ~/.bash_login   
    - ~/.profile      
    - ~/.bashrc       # loaded everytime you start a shell(e.g. starting terminal)
```

--

```
tcsh as a login shell
    - /etc/csh.cshrc
    - /etc/csh.login
    - ~/.tcshrc
    - ~/.cshrc
    - ~/.login
```

--

- rsync
- diff
- who
- id
- wget
- curl
- which
- $PATH
- sort
- wc
- sleep

--

## Special Parameters
* ($?)
>Expands to the exit status of the most recently executed foreground pipeline. 
* ($$) 
>Expands to the process ID of the shell. In a () subshell, it expands to the process ID of the invoking shell, not the subshell. 
* ($#) 
>Expands to the number of positional parameters in decimal. 


[Bash: Special-Parameters](https://www.gnu.org/software/bash/manual/bash.html#Special-Parameters)

--
device | description
----|----
/dev/stdin  | File descriptor 0 is duplicated.
/dev/stdout | File descriptor 1 is duplicated.
/dev/stderr | File descriptor 2 is duplicated.
/dev/null | 
/dev/zero | 

---
reference 

* [TLDP(The Linux Documents Project)](http://www.tldp.org/)
* [GNU Bash manual](https://www.gnu.org/software/bash/manual/bash.html)

