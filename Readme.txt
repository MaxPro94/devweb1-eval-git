stagiaire@DESKTOP-QEHV0Q2 MINGW64 ~/Desktop/Eval/devweb1-eval-git (master)
$ git checkout -b 'dev'
Switched to a new branch 'dev'

stagiaire@DESKTOP-QEHV0Q2 MINGW64 ~/Desktop/Eval/devweb1-eval-git (dev)
$ git commit -m "first commit"
On branch dev
nothing to commit, working tree clean

stagiaire@DESKTOP-QEHV0Q2 MINGW64 ~/Desktop/Eval/devweb1-eval-git (dev)
$ git add .

stagiaire@DESKTOP-QEHV0Q2 MINGW64 ~/Desktop/Eval/devweb1-eval-git (dev)
$ git commit -m "Second commit"
[dev 2ad04ea] Second commit
 2 files changed, 18 insertions(+)
 create mode 100644 Readme.txt
 create mode 100644 index.html

stagiaire@DESKTOP-QEHV0Q2 MINGW64 ~/Desktop/Eval/devweb1-eval-git (dev)
$ git add .
warning: in the working copy of 'villes.db.sql', LF will be replaced by CRLF the next time Git touches it

stagiaire@DESKTOP-QEHV0Q2 MINGW64 ~/Desktop/Eval/devweb1-eval-git (dev)
$ git commit -m "db villes"
[dev 861ef14] db villes
 3 files changed, 36990 insertions(+), 4 deletions(-)
 create mode 100644 app.py
 create mode 100644 villes.db.sql

stagiaire@DESKTOP-QEHV0Q2 MINGW64 ~/Desktop/Eval/devweb1-eval-git (dev)
$ ^C
