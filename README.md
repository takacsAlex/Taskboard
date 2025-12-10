# Taskboard

**Taskboard** is a simple drag and drop task-management application built with Kivy. It helps you organize your work using a clean, board-style interface. The app is designed to be in your project's folder and developers can pull tasks from it and also push new ones with notes.

---

## Features

* **Create, edit, and delete tasks**
* **Drag and drop interface**

---

## Getting started

### 1. Install Kivy

```bash
pip install kivy
```

### 2. Clone the repository

```bash
git clone https://github.com/takacsAlex/Taskboard
```

### 3. Run the application

```bash
python run.py
```

---

## Project Structure

```
taskboard/

** run.py                 #Starting file
** main.py                #The core of the application
** components/            #Custom modules 

```

---

## For developers

* **Create a new branch aged from dev and name it feature/Yourname.**
* **Always pull from dev.**
    ```bash
    git pull origin dev
    ```
* **If you are doing more tasks, please do it in another branch, which will be called: feature/Yourtask.**
* **Always push to theese branches!**
    ```bash
    git add .
    git commit -m "your completed action"
    git push -u origin feature/Yourname
    ```          
* **If you are done with a task, please create a pull request to dev from your branch.**
* **Your task will be analyzed by the author and if he approves, your branch can be merged to dev.**

---

## Tasks
* **The tasks are in TASK.md. If you complete a task, give it a striketrough style**
    ```
    ~~**Completed task**~~
    ```

---
