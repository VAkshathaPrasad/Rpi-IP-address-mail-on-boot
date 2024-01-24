# Rpi-IP-address-mail-on-boot
Steps to execute the program on boot
1. Download the .py file.
2. Copy to Rpi (copy the path where the .py file is copied).
3. On the Rpi terminal type the below command
   crontab -e
4. Add the below line at the end of the file
   @reboot sleep 60 && python <path_of_the_.py_script_where_it_is_copied>.py
5. open .py file, and update to,from and password.
6. save and close the file.
7. Reboot the system, an email will be triggered automatically with the IP address of Rpi.
