## spell-check-go
The project is used to check word typo or spelled incorrectly for Go repository

## Prerequisites
python 3

## How to Use?
Git clone this repo[spell-check](https://github.com/DasyDong/spell-check-go.git)

```
virtualenv -p python3 ~/venv3 && source ~/venv3/bin/activate

pip3 install -r requirement.txt

python spell_check.py project
```

## Results
Spell checking result is in spell_check_wrong.txt

Words In spell_check_ignore.txt is skipped to check