[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/vijaiaeroastro/irccloud.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/vijaiaeroastro/irccloud/context:python)

# IRC Cloud Keep Alive Utility
A simple heroku application to keep your irccloud connection alive always (without paying :dollar:)!

Let me start this by saying *None of this is illegal*  
IRC Cloud has publicly documented their api and different RPC calls they make.  
Its publicly listed on github and you can read it here [IRC Cloud Wiki](https://github.com/irccloud/irccloud-tools/wiki).

**IMPORTANT :** In order to get going, please read this blog article which details the usage of this application.
https://vijaikumar.in/keeping-your-irccloud-client-always-connected-for-free-82db71b3cff3

## Requirements
### Heroku
* A Free heroku account
* Python 3.7
  * Requests library
  
### For use in your own VPS
- Be sure to have `python-dev` installed in your machine.  
- Clone the repository with `git clone https://github.com/vijaiaeroastro/irccloud.git`  
- Enter into the cloned repository with `cd irccloud`  
- Install the requirements with `python -m pip install -r requirements.txt`  
- If the above command fails, install `python-pip`  
- Use the bash script `irccloud_cronjob` provided for ease of use  
- You can also specify everything on a `crontab` entry instead. Just type `crontab -e`, choose your favourite text editor  
and add this to it (this will  be executed every hour):  
`0 * * * * IRCCLOUD_USERNAME="your@email.address" IRCCLOUD_PASSWORD="your_password" python3 /home/irccloud/irccloud/irccloud.py >/dev/null 2>&1`
  
## License
UNLICENSE
