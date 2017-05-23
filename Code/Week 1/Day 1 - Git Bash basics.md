#### As today was just learning git bash, there's no code per se, just terminal commands. Here is a sample of what I learned today (I use echo here to show what's in the files):

$git config --global user.name "Jon"
git config --global user.email "jon@mail.none"
$git init practice-dir
$cd practice-dir
$touch README.md LICENSE.md testfile.txt output.log .gitignore
$ls -a
$echo *.log >> .gitignore
$echo This is a test Repo, discard >> README.md
$echo No restrictions >> LICENSE.md
$echo ipsum lorem... >> testfile.txt
$echo No crashes here >> output.log
$git status
$git add .
$git status
$git commit -m "Added basic file structure to master"
$git ls-files
$mv testfile.txt Example.txt
$git status 
$git add -A
$git status
$git commit -m "Renamed testfile to Exmaple"
$git rm LICENCE.md
$git status
$git reset HEAD LICENSE.md
$git status
$git checkout -- LICENSE.md
$git status
$ls -a
$git checkout -b editing
$echo Just some plane old text, but in english > Example.txt
$git commit -a -m "Updated text in Example.txt"
$git status
$less Example.txt
$git checkout master
$less Exmaple.txt
$git status
$git merge editing
$less Example.txt
$git branch -d editing
$git branch
$git checkout -b tweaking
$echo Goodbye >> Example.txt
$git commit -a -m "added a sign off to Example.txt"
$git status
$git checkout master
$git checkout add-line
$echo Fairwell >> Example.txt
$git commit -a -m "Added a sign off to Example.txt"
$git status
$git checkout master
$git status
$git merge tweaking
$git status
$less Example.txt
$git merge add-line
$git status
$git merge --abort
$git checkout add-line
$vi Examaple.txt
$less Example.txt
$git commit -a -m "resolve merge conflict with master"
$git checkout master
$git status
$git log
$git merge add-line
$git status
$less Example.txt
$git branch
$git branch -d add-line tweaking


