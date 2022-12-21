# The Unity Codenamer
### This is meant for showing Unity versions and names, etc from 2017.1.0f1 to 2022.2.1f1.

# Documentation
The documentation might not be simple.
All you need to edit is the config.json, which basically is the Unity version.
Here's an example for if I wanted to do Unity 2017.1.1f1:
```json
{
  "editorVer": {
    "major": "2017",
    "minor": "1",
    "ln": "1",
    "patch": "f1"
  }
}
```
As you can see, the major version is 2017 (the year), the minor version is 1, and the considered other number is also 1. The patch is f1, and the f in f1 means final.
You can use a for Alpha, b for Beta, rc for Release Candidate, and of course, f for Final. An example of doing that would've been 2017.4.3a1 for alpha,
so you would've done 2017 for the major, 4 for the minor, and 3 for that weird other number, and a1 for the patch.
Then, run the Python File and it will tell you your build and "codename!"
How does it generate codenames?
Easy. It grabs the version and takes it away from the latest version. Whatever's remaining is rounded, and there you have it! That's the cool little number behind
everything!

Now what do we do with this number? This number shows which codename it will use.
0.0 through 0.9 will use Goblin (newest),
1.0 through 1.9 will use Rabbit,
2.0 through 2.9 will use Cyber,
3.0 through 3.9 will use Neo,
4.0 through 4.9 will use Turtle,
and 5.0 is the Grandfather Unity which will use Grand (oldest.)
Negative numbers are newer than the latest (2022.2.1f1.)

That's nice! We got a little codename going on!

# Codename Table

| Numbers   |   Codename       |
|-----------|:----------------:|
| 0.0 - 0.9 |  Goblin (Newest) |
| 1.0 - 1.9 |    Rabbit        |
| 2.0 - 2.9 | Cyber            |
| 3.0 - 3.9 | Neo              |
| 4.0 - 4.9 | Turtle           |
|    5.0    | Grand (Oldest)   |
