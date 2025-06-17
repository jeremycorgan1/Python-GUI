project_runner_gui.py is a python program codebase for a lightweight GUI that can run a python program from a list populated from a folder of your choosing. 

I created a folder at /home/oem/   named ""pyprojects"" to store my py projects and is how it is linked in the code.

needs myvenv to run
python3 -m venv ~/myenv
source ~/myenv/bin/activate

pip install --upgrade pip
# Install future GUI dependencies here

tkinter is used in the code for GUI so,
sudo apt install python3-tk

PyGUI.desktop should be in the desktop folder with the directory in the code tied back to PyGUI.png for icon.
This will allow you to click and open program from desktop.

---------------
To make desktop icon executable and trusted
chmod +x ~/Desktop/PyGUI.desktop
gio set ~/Desktop/PyGUI.desktop "metadata::trusted" yes
---------------
If you ever update project_runner_gui.py to depend on other libraries (e.g., requests, matplotlib, etc.), just install them into your venv:

source ~/myenv/bin/activate
pip install <package-name>



