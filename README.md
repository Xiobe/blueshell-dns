# DNS info

# Cloning the repository (Linux environment)

The first step in using this software is to get your local copy. That is done by cloning the repository, first position yourself on your hard drive where you want to have your copy of the software.
Then run the following command to get your local copy.

```shell
git clone https://github.com/Xiobe/dnsinfo.git 
```

Once you have your local copy we need to create the venv (virtual environment). The venv allows you to isolate the project from the rest of the system so that you don't end up in dependency hell.
That is done like this:
```shell
cd dnsinfo
python -m venv venv
```

To activate your venv you run
```shell
source venv venv/bin/activate
```

The next step is to bring pip up-to-date
```shell
python -m pip install --upgrade pip
```
