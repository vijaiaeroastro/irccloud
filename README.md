# IRC Cloud Keep Alive Utility
A simple heroku application to keep your irccloud connection alive always (without paying :dollar:)!

Let me start this by saying *None of this is illegal*  
IRC Cloud has publicly documented their api and different RPC calls they make.  
Its publicly listed on github and you can read it here [IRC Cloud Wiki](https://github.com/irccloud/irccloud-tools/wiki).

**IMPORTANT :** In order to get going, please read this blog article which details the usage of this application.
https://vijaikumar.in/keeping-your-irccloud-client-always-connected-for-free-82db71b3cff3

Requirements
============
* A Free heroku account
* Python 2.7
  * Requests library
  
### For use in your own VPS
This script also works with python 3  
Be sure to have `python3-dev` installed in your machine.  
Clone the repository with `git clone https://github.com/vijaiaeroastro/irccloud.git`  
Enter into the cloned repository with `cd irccloud`  
Install the requirements with `python3 -m pip install -r requirements.txt`  
If the above command fails, install `python3-pip`  
Use the bash script `irccloud_cronjob` provided for ease of use
  
License
=======
UNLICENSE
