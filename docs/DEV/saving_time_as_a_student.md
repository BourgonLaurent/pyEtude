# Saving Time as a Student: Create Custom Documents in 10 seconds

*#octograd2020* *#githubsdp* *#student* *#productivity*

[](https://images.unsplash.com/photo-1514474959185-1472d4c4e0d4?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&dl=matt-ragland-8OVDzMGB_kw-unsplash.jpg)

---

#### How I used my free time to speed up my school tasks

---

## 🧐 Problem Statement

Throughout my years at school, I've found that its **biggest challenge is _time_**.  A lot of tasks are *repetitive*, they can be *troublesome* and they shorten the time you dedicated for something. As a student learning programming ― and also wanting to go in this field ― I wondered how I could help. It is possible to see your friends and have good grades, while still being a human; you don't need *more* time, you just need to use it *efficiently*.

> Aren't you wasting time by inventing, coding, debugging and sharing your tool instead of just doing it?

When I tell someone about my projects, this is sometimes the reaction I have. Let's be honest, I'm *using* time by making all these tools. Another thing I've learned is that you have *free time*: the normal student would use it to go on social media, binge watch a TV show, play games or read a book ― yes, there are still people reading books for fun in 2020. It is not abnormal to have a day with almost nothing to do, and the next you'll need to work all day.

So did I *waste* time? Absolutely not! I've learned so much and had fun while making these tools. Productivity isn't maximizing all the time, it is maximizing it **when you need it**.

## 💡 Why this project

While I have made a few tools to boost my productivity, going from simple flashcards to a [Telegram bot](https://github.com/BourgonLaurent/TelegramSuttonForecast), the project I chose to write about is **pyÉtude**. *I'm not good with names, and since it is made with `python`and made for studying, `étude` in French, my native language, I decided to call it that way.*

This project really improved my coding skills: it started with almost no use of functions, to something using classes and libraries, and it is only the beginning. I plan on improving this tool as long as I'm using it. When I use it, I often write down some features I would like to have ― or polish ― and then add them on another day. Being able to be your own tester is one of the best feelings.

## 🎈 pyÉtude

{% github BourgonLaurent/pyEtude no-readme %}

pyÉtude is a tool that I've made to create Microsoft Word `.docx` documents. I use them extensively to study and rewrite my notes, write essays, outline a presentation and all the other things a student could do. To keep everything organized, I always use the same style for my notes (the fonts, colors, tables, headings are the same). Before pyÉtude, I had a template `.dotx`, a solution that Microsoft *believes* solves this problem, but it was *painful*. Bugs everywhere, inconsistent style, problem while working on iPad ― main device when not at home.

### How it works

I first thought that I should use a library to create my document, it would be quick and future proof ― and most importantly reinforcing the stereotype of importing things in `python`. However, the current libraries weren't extensive enough to let me create styles with good formatting. I then decided to use another way: modify a current word document with values. This meant I had to have a general idea of how a Word document works ― how to unpack it, modify it and repack it.

## How it looks

I've tried to make pyÉtude as simple as possible, while still keeping all the features I wanted to have.

![pyÉtude](https://dev-to-uploads.s3.amazonaws.com/i/mh8evlcofte6snydmpdl.png)

As for the document in itself, this is the template that I use the most.

![Example Document](https://dev-to-uploads.s3.amazonaws.com/i/e9cqpjeag55a1i2lj5xt.png)

## Features

As said before, I've made pyÉtude while using it. This means that during the multiple refactors I've made, I included some nice-to-have. Here are some of my favorites:

- Store your name and grade so you only need to write it the first time you use the software
- Create personalized classes with their own full name, short name and folder path
- Automatically create the file in the class folder and name it accordingly (if `ART-CHP1.docx` already exists, it suggest to use `ART-CHP2.docx`)
- Use multiple file templates depending on your need (study notes, essay, oral presentation...)
- Cross platform support on desktop (Windows, Linux, macOS) ― with a web version in development

## 🚀 Progress

pyÉtude is one of my proudest project since I learned so much and when I learned a new thing elsewhere, I used it on pyÉtude.

### Command Line Interface

pyÉtude started as a simple command line interface, it was ugly, and some of my favorites features weren't there, but it was still a huge time saver.

![CLI](https://dev-to-uploads.s3.amazonaws.com/i/2if2chc2lnnqm0pc673u.png)

### First GUI

This was the first graphical interface I've seriously made. It was made with `tkinter` and used some hacky ways to get features like placeholders in entries.

![tkinter](https://dev-to-uploads.s3.amazonaws.com/i/e4r8elcs9xikgqezzq3l.png)

### PyQt5

The current version of the software. It contains some nice extra features like tabs, calendar, easy file management and also a lot more eye appealing than the previous one.

### Future

I'm currently planning on making pyÉtude a small website (making it private however) so I can quickly make documents when I'm not in front of my computer. Meanwhile, I've created a `Jupyter` notebook that I can access everywhere. It is rough and not as complete as the desktop version, but good enough.

![jupyter](https://dev-to-uploads.s3.amazonaws.com/i/ltxgroomqgroffxjdso0.gif)

## ⛏️ Built With

- [Visual Studio Code](https://code.visualstudio.com/) to write, modify and debug
- [λ cmder Console Emulator](https://cmder.net/) as a terminal, but also to test snippets and ideas in REPL
- [Microsoft Word 365](https://products.office.com/fr-ca/word) to create the templates included
- [Python 3](https://www.python.org/) to compile and run the software
  - [Qt Designer](https://build-system.fman.io/qt-designer-download) to create the software UI
  - [PyQt5](https://www.riverbankcomputing.com/software/pyqt/intro) to bind the UI with code, providing interaction
  - [Pythonista](https://omz-software.com/pythonista/) as a full Python IDE on iOS, great when I wanted to make quick modifications while in transit
- [Git](https://git-scm.com/) as a version control tool
  - [GitHub](https://github.com/) to organize, publish and save this project
  - [Working Copy](https://workingcopyapp.com/) to quickly push modifications and ideas to GitHub using my iPad when I was in transit
  - [Termius](https://www.termius.com/) as a great cross platform SSH terminal

{% github BourgonLaurent/pyEtude no-readme %}
