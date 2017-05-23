#### Today, like yesterday I was really just working on getting a better understanding of git and how to use it outside of the github website. Yesterday I covered the basics of file management, local git repository and branching and merging. Today I did a little more, but again this was several hours of "tinkering" to see what would happen, troubleshooting and googling for help, so again, there's no code here. Unfortunately I was at this a little too long to have time to creat a little example of using the git real world style so I;ll just type out some commands here that I used today:


git remote add origin https://github.com....

git push origin master

git clone https://github.com/Pominaus/practice.git git\ practice

git status

git fetch

git fetch -p

git pull

git push -u origin master

git push

git tag v0.1a

git tag -d v0.1a

git tag -a v0.1a -m "early alpha build"

git show v0.1a

git reset 5cb2ed0 --mixed

git reset v0.1a --soft

git reset head --hard

git pull --force

git branch -d

git checkout branchname

git checkout -b branchname

git push --force

git push origin :branchname

git log --oneline --graph

git reflog

git stash

git stash list

git stash show

git stash pop

git stash branch edit-stash

git stash clear


