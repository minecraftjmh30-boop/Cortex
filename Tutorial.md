# How To Install Cortex!

## Step 1:
Open Terminal and find where you want the program to stay
```bash
cd {location}
```

## Step 2:
Clone the Git Repo
```bash
git clone {URL}
```
Then Open its folder
```bash
cd Cortex
```

## Step 3:
Create The Python Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 4:
Make Sure PIP is Installed
```bash
pip install --upgrade pip
pip install .
```

## Step 5:
Install Dependencies 
```bash
pip install -e .
```

## Step 6:
Run It!
```bash
python main.py
```