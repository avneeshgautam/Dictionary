import time
from csv import DictReader,DictWriter

word=[]   # empty list for word
meaning=[]   # empty list for meaning
dict={
    
}

f1=open('dictionary_list.csv','a')
f1.close()

######## file reader from dictonary file 
with open('dictionary_list.csv','r') as rf:
    csv_reader = DictReader(rf)
    for row in csv_reader:
        dict[row['word']]=row['meaning']

## normal list
list=dict.keys()
# sort words from dic to list
dict_list=sorted(list)
yes=['yes','YES','Yes']
no=['no','No','NO']

##### welcome scrren #######

print("\n\tWELCOME TO AVNEESH DICTIONARY")
print("-------------------------------------------------------")
print("\t# 1. ADMIN \n \t# 2. USER \t\t|")
print("-------------------------------------------------------")

ad_user=input("You are Admin or User: ")
print("-------------------------------------------------------")
##################  ADMIN SECTION ################3

if ad_user == 'admin' :
    print("LOGIN..........\n")
    time.sleep(0.6)
    username=input("Enter username: ") 
    password=input("Enter the password: ") 
    print("-------------------------------------------------------")

    ############# login password #######333333
    if username == 'avneesh' and password =='12345':
        print("\n\t\tWELCOME ADMIN")
        print("-------------------------------------------------------")

        ############# word show or add ############   
        val= input("Words Show OR ADD: ")
        print("-------------------------------------------------------")
        if val=='show':
            if dict_list ==[]:  
                print("Dictionary is empty: \n Add word in dictionary:")
                print("Exiting..\n")
                time.sleep(0.5)
                print("\t\tGOODBYE")
                print("-------------------------------------------------------")

            # if dictionary list is not empty ##    
            else:
                for i in dict_list:
                    print(i)
                print("-------------------------------------------------------")

        ############## ADDING Word/meaing in dictnary List #############    
        elif val =='add':
            print(dict_list)
            print("-------------------------------------------------------")

            # ############# WRITNG in Dictionat_list.csv file #######
            with open('dictionary_list.csv','a') as f:
                csv_writer = DictWriter(f,fieldnames=['word','meaning'])
                csv_writer.writeheader()

                ######### adding word ################
                while(1):
                    more=input("Do you want add more (Press 1): ")
                    if more == '1':
                        word=input("\nEnter the word: ")
                        meaning=input("Enter the meaning: ")
                        print("\n")

                        csv_writer.writerow({
                        'word':word,'meaning':meaning
                        })
                    ############# dont want more adding word ##########    
                    else:
                        print("-------------------------------------------------------")
                        print("\n")
                        exit()
                    
    else:
        print("-------------------------------------------------------")
        print("Username or Password is incorrect")
        exit()

#######################  USER SECTION #####################

elif ad_user == 'user':
    print("-------------------------------------------------------")
    ####### finding words ##############
    print("\nFinding All Word in dictionary:")
    print("\tFinding........\n")
    time.sleep(1.2)

        ################   check dictionary ############## 
    if dict_list ==[]:
        print("Dictionary is empty:")       
        print("\t Try Again later....")
        print("------------------------------------")
        exit()
    else:
        print(dict_list)
        print("------------------------------------")


    ################  FINDING MEANING OF WORD BY LETTER
    find=input("\nDo you want to Find word by First Letter (Yes/no): ")
    
    ###############  YES ################
    if find in yes:
        enter=input("\nEnter first letter: ")
        print("\tFinding........")
        time.sleep(0.7)
        print("\nWord:\t\tMeaning")
        print("------------------------------------")
        for i in dict_list:
            if enter == i[0]:
                # print(i)
                print(i+"\t\t"+str(dict[i]))
    
    ###########  NO ############
    elif find in no:
        print("-------------------------------------------------------")
        ########### finding by full word name ###############
        full=input("\nDo you want to find meaning by full Word:(Yes/no) ")
        print("-------------------------------------------------------")
        if full in yes:
            word=input("\nEnter the Word: ")
            print("\tFinding........")

            if word in dict.keys():
                print("\nWord:\t\tMeaning")
                print("------------------------------------")
                print(word+"\t\t"+str(dict[word]))
                print("\n")
            else:
                print("\nNot found:\n")
        else:
            print("\nOK")
            print("\tExiting..........")
            time.sleep(0.4)
            print("\t\tGOODBYE")
            print("-------------------------------------------------------")
            exit()

    else:
        print("\nINVALID CHOICE")
        print("Exiting..........")
        time.sleep(0.4)
        print("\t\tGOODBYE")
        print("-------------------------------------------------------")
        exit()
