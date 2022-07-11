# Git Status

## a.txt 파일을 만든 직후

> 빨간 글씨 => 1통

```bash
$ git status
On branch master

# 트래킹이 되고 있지 않은 파일?
# => 1통 (working directory)
# => 한번도 git으로 관리 되고 있지 않은 파일!
Untracked files:
# git add 사용해봐 ...
# 포함시키기 위해서 / 커밋이 될 것 => 2통에 넣으려면
  (use "git add <file>..." to include in what will be committed)
        Git bash.md
        a.txt
# 커밋할 것은 없어 =>2통이 비어있어
# 하지만(but) 트래킹 되지않은 파일은 존재한다.
#(git add 사용해서 트래킹해)
nothing added to commit but untracked files present (use "git add" to track)
```

## b.txt 파일을 만들고 add 한 이후

> 초록 글씨 => 2통

```bash
$ git status
On branch master
# (커밋될) 변경사항들 => 2통
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        # 새로운 파일: b.txt
        new file:   b.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Git bash.md
        a.txt
```

# a.txt 파일과 b.txt 파일을 모두 add한 이후 커밋가지

```bash
이준엽@Lee-JunYeop MINGW64 ~/Desktop/GIT수업 (master)
$ git add a.txt

이준엽@Lee-JunYeop MINGW64 ~/Desktop/GIT수업 (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   a.txt
        new file:   b.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Git bash.md


이준엽@Lee-JunYeop MINGW64 ~/Desktop/GIT수업 (master)
$ git commit -m 'a.txt b.txt 만들었음'
[master a77fb18] a.txt b.txt 만들었음
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.txt
 create mode 100644 b.txt

이준엽@Lee-JunYeop MINGW64 ~/Desktop/GIT수업 (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Git bash.md

nothing added to commit but untracked files present (use "git add" to track)   

이준엽@Lee-JunYeop MINGW64 ~/Desktop/GIT수업 (master)
$ git add Git\ bash.md

이준엽@Lee-JunYeop MINGW64 ~/Desktop/GIT수업 (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   Git bash.md


이준엽@Lee-JunYeop MINGW64 ~/Desktop/GIT수업 (master)
$ git log
commit a77fb185c3aab9ff742a7ae9988ac37cd27abb64 (HEAD -> master)
Author: JunLee <dortkthf@gmail.com>
Date:   Tue Jul 5 15:47:37 2022 +0900

    a.txt b.txt 만들었음

commit 55190e3c52bce06b51155c0e2d51fe07cb4ac4d7
Author: JunLee <dortkthf@gmail.com>
Date:   Tue Jul 5 15:33:48 2022 +0900

    git 정리

commit 8404e86fe3f24d3c0ffef83df54a6dec5ba2f234
Author: JunLee <dortkthf@gmail.com>
Date:   Tue Jul 5 14:56:42 2022 +0900

    1.txt and 2.txt

```

