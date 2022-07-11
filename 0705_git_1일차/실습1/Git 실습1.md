# Git 실습 가이드

## 0. 사전 설정 (PC최초 한번)

```bash
$ git config --global user.name 'dortkthf'
$ git config --global user.email 'dortkthf@gmail.com'
```

## 1. 바탕화면에 TIL 폴더를 만든다.

- TIL 폴더를 열어서 마크다운 정리 파일을 옮긴다.

- VS Code를 해당 폴더에서 우클릭하여 연다.

## 2. TIL 폴더에 git 저장소를 만들어준다

```bash

$ git init
Initialized empty Git repository in C:/Users/이준엽/Desktop/GIT수업2/.git/

```

## 3. 커밋을 만든다.

```bash
이준엽@Lee-JunYeop MINGW64 ~/Desktop/TIL
$ git init
Initialized empty Git repository in C:/Users/이준엽/Desktop/TIL/.git/

이준엽@Lee-JunYeop MINGW64 ~/Desktop/TIL (master)
$ git add .

이준엽@Lee-JunYeop MINGW64 ~/Desktop/TIL (master)
$ git commit -m 'markdown commit'
[master (root-commit) 655a0d8] markdown commit
 2 files changed, 41 insertions(+)
 create mode 100644 "markdown_practice_LeeJunYeop.assets/\353\213\244\354\232\264\353\241\234\353\223\234.jpg"
 create mode 100644 markdown_practice_LeeJunYeop.md

이준엽@Lee-JunYeop MINGW64 ~/Desktop/TIL (master)
$ git status
On branch master
nothing to commit, working tree clean

이준엽@Lee-JunYeop MINGW64 ~/Desktop/TIL (master)
$ git log
commit 655a0d80345065d2646d1d5ae3f89c08d0886626 (HEAD -> master)
Author: dortkthf <dortkthf@gmail.com>
Date:   Tue Jul 5 16:38:00 2022 +0900

    markdown commit
```

