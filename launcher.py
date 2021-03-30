# LICENSE MIT
# BY : KILLIAN PEREZ
# DATE: 2021, March 29th

#  ██████╗ ██╗     ███████╗ █████╗ ███████╗███████╗    ██████╗ ███████╗ █████╗ ██████╗ 
#  ██╔══██╗██║     ██╔════╝██╔══██╗██╔════╝██╔════╝    ██╔══██╗██╔════╝██╔══██╗██╔══██╗
#  ██████╔╝██║     █████╗  ███████║███████╗█████╗      ██████╔╝█████╗  ███████║██║  ██║
#  ██╔═══╝ ██║     ██╔══╝  ██╔══██║╚════██║██╔══╝      ██╔══██╗██╔══╝  ██╔══██║██║  ██║
#  ██║     ███████╗███████╗██║  ██║███████║███████╗    ██║  ██║███████╗██║  ██║██████╔╝
#  ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ 
#                                                                                      
#  ██████╗ ███████╗ █████╗ ██████╗ ███╗   ███╗███████╗   ███╗   ███╗██████╗     ██╗    
#  ██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝   ████╗ ████║██╔══██╗    ██║    
#  ██████╔╝█████╗  ███████║██║  ██║██╔████╔██║█████╗     ██╔████╔██║██║  ██║    ██║    
#  ██╔══██╗██╔══╝  ██╔══██║██║  ██║██║╚██╔╝██║██╔══╝     ██║╚██╔╝██║██║  ██║    ╚═╝    
#  ██║  ██║███████╗██║  ██║██████╔╝██║ ╚═╝ ██║███████╗██╗██║ ╚═╝ ██║██████╔╝    ██╗    
#  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝╚═╝     ╚═╝╚═════╝     ╚═╝    
#                                                                                      

import time, logger, os, random, telegram, telegram.ext as te
halt = False
logger.log(2, "Bot started successfully")

folder = "<IMAGE FOLDER HERE>" # FILE PATH use "\\" for windows and "/" for linux
token = "<YOUR TOKEN HERE>"
chatid = "-100<CHANNEL ID WITHOUT c>"
tempsEnSeconde = 54000 # Time in second
fichierLock = "lock.txt" # Path where the lock.txt is by default it's the same folder as the launcher.py

while halt != True:
    try:
        logger.log(9, "Sending...")
        list_of_files, final_list, locked_list, readonly_list = set([]), list(), open(fichierLock, "r+"), str(open(fichierLock, "r").readlines())
        amntline = len(locked_list.readlines())
        if (amntline >= len(os.listdir(folder))):
            logger.log(4, "No more file found...")
            exit()
        while len(list_of_files) != 3:
            tmp = [str(os.listdir(folder)[random.randint(0, len(os.listdir(folder)) - 1)])]
            if str(tmp).replace("\\n", "") not in str(readonly_list).replace("\\n", ""):
                list_of_files.update(tmp)
                amntline += 1
                locked_list.write(str(tmp) + "\n")
            if(amntline >= len(os.listdir(folder))):
                logger.log(6, "No more file found...")
                halt = True
        for file in list_of_files:
           final_list.append(telegram.InputMediaPhoto(open(folder + file, "rb")))
        logger.log(9, "Envoie des fichiers suivants: " + str(list_of_files))
        te.Updater(token).bot.send_media_group(chat_id=chatid, media=final_list)
        time.sleep(tempsEnSeconde)
    except Exception as err:
        exception_type = type(err).__name__
        print(exception_type)
        logger.log(4, str(exception_type) + "--- ERROR Details: " + str(err))
