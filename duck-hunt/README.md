To create a virtual environment with virtenv and python 3.7 in the current directory:

$ bash setup_venv.sh <name of your environment>

To run a checksum to verify the wheel:

$ ./checksum ece471_duckhunt-1.1.0-cp37-cp37m-linux_x86_64.whl 3af370bf48c1f2b81f460c59e4f18af05abceee11f227c4d3deb80bd18c000d5


Sometimes, Pygame will freeze when running +200 levels sequentially with quiet=False.  To avoid this, run each level independently.  An example of this can be found in run_test.sh 
