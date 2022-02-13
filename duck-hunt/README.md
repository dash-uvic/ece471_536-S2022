2022-02-12:  

*  Updated to version 1.2 with bug fix for relative move_type and platform-independent versions with optimizations removed added. 
* Updated duck_hunt_main.py that didn't have env.render() inside the main loop.
* Updated requirements.txt to include package sometimes not installed that is required.

To create a virtual environment with virtenv and python 3.7 in the current directory:

$ bash setup_venv.sh <name of your environment>

To run a checksum to verify the wheel:

$ ./checksum ece471_duckhunt-1.2.0-cp37-cp37m-linux_x86_64.whl 314e43a5753f75710a114dd9d8f8973bde3d82944e0610e7fe631dcbd589e948 
$ ./checksum ece471_duckhunt-1.2.0-py3-none-any.whl 76e91ded64faf39deb63d4c9822531ffdf5ddea54bdfb118379409e91000549f 


Sometimes, Pygame will freeze when running +200 levels sequentially with quiet=False.  To avoid this, run each level independently.  An example of this can be found in run_test.sh 
