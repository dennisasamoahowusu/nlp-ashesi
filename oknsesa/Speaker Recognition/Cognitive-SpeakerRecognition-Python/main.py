
# Imports
import speech_recognition as sr
import pyaudio
import wave
import os

#!/usr/bin/python
import sqlite3

conn = sqlite3.connect('/Users/admin/Desktop/Courses/CS Applied Capstone Project/Project Folder/capstone-final/Interface/TestPage/test2.db')
print("Opened database successfully")


# Reset Files

outProfile = open("profile.txt", "w")
outProfile.write(" ")

outVerify = open("verify.txt", "w")
outVerify.write(" ")


###############################################################################
######              Initalize Profile IDs and Their Names               #######
###############################################################################
# IDENTIFICATION
error = "00000000-0000-0000-0000-000000000000"
Jojoe = "0610dd36-3fe7-44a1-83ab-9327b499cd72" 
Julianne = "380b5a3f-8a2b-4099-aede-b664e1a5c19c"
Kwame = "3ab419dc-d1f1-44d5-9bb9-9707f2f7240e"
# Sasu = "e3871ba8-801c-44e7-91dd-6029133a74dd"
Joseph = "726dd798-3991-49c8-ba37-b47dcb7303cf"


# VERIFICATION

# List of ALl Profiles In a single String
profilesString = "0610dd36-3fe7-44a1-83ab-9327b499cd72,380b5a3f-8a2b-4099-aede-b664e1a5c19c,3ab419dc-d1f1-44d5-9bb9-9707f2f7240e,726dd798-3991-49c8-ba37-b47dcb7303cf"


# Profile Dictionary

profileDict =	{
	"error" : "00000000-0000-0000-0000-000000000000",
  	"Jojoe": "0610dd36-3fe7-44a1-83ab-9327b499cd72",
  	"Julianne": "380b5a3f-8a2b-4099-aede-b664e1a5c19c",
  	"Kwame": "3ab419dc-d1f1-44d5-9bb9-9707f2f7240e",
  	"Joseph":"726dd798-3991-49c8-ba37-b47dcb7303cf"

}


profileVerify =	{

  	"Jojoe": "480e71f2-7dbc-4bf8-b7db-3225a91f7925"
  

}



###############################################################################
######              Function Definitions for Main Python Script         #######
###############################################################################



########################       getAudio() Function Start    #################################

# getAudio() Function to Record Audio form External Microphone and Save as an Audio File
def getAudio(filename,FORMAT = pyaudio.paInt16, CHANNELS = 1, RATE = 8000,
                    CHUNK = 1024, RECORD_SECONDS=5):
    
    audio = pyaudio.PyAudio() #PyAudio Object To Collect Audio Data

    # start Recording
    print("Start Recording Speech (Say Something): ")
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # stop Recording
    print("Done Recording Speech")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    #Convert to Wave File 
    waveFile = wave.open(filename, "w")
    waveFile.setnchannels(CHANNELS) # Channel = Mono
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE) # Sampling Rate is 16K
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

 ########################       getAudio() Function End  #################################



########################  recognizeSpeech() Function Start #################################

# recognizeSpeech() Function to Transcribe Recorded Audio and Get Speech as a String
def recognizeSpeech(filename):
	
	speech = ''
	r = sr.Recognizer() # SpeechRecognition Object

	# Extract Audio File As Source
	with sr.AudioFile(filename) as source:
	    audio = r.record(source) 

	print("=========== Recognizing Speech ============")

	# Using Google Speech Recognizer to Transcribe Audio to Text
	try:
	    # print("Speech: " + r.recognize_google(audio))
	    speech = r.recognize_google(audio)
	except sr.UnknownValueError:
	    print("Speech Recognition System could not understand audio, Please Speak Again")
	except sr.RequestError as e:
	    print("Could not request results from Speech Recognition service; {0}".format(e))
	
	return speech


 

########################  recognizeSpeech() Function END #################################




########################  recognizeSpeaker() Function START #################################

# recognizeSpeaker() Function to Get Speaker from Audio
def recognizeSpeaker(filename,profileId):
	print("========== Recognizing Speaker ===========")
	cmdRecog2 = "python3 Identification/IdentifyFile.py 3b1ec42c30884c2eadaec6f1975ec0f6" + " " + filename + " " + "True" + " " + profileId # Format for Running Library In Command Line
	os.system(cmdRecog2) # Run Command Line Arg to Call Speaker Recognition Library


########################  recognizeSpeaker() Function END #################################


########################  verifySpeaker() Function START #################################
def verifySpeaker(filename,profileId,speaker):
	print("========== Verifying " + speaker + " ===========")
	cmdVerify = "python3 Verification/VerifyFile.py 3b1ec42c30884c2eadaec6f1975ec0f6" + " " + filename + " " + " " + profileId # Format for Running Library In Command Line
	os.system(cmdVerify)

########################  verifySpeaker() Function END #################################


########################  compareProfiles() Function START #################################
def compareProfiles(filename,profileDict):
	f = open(filename)
	line = f.readline()

	speaker = ""

	# Loop through Profile Dictionary Values and Find the Actual Key
	for profile in profileDict:
		# print(profile)
		if(profileDict[profile] == line):
			# print(profileDict[profile])
			speaker = profile
			break
	
	return speaker

########################  compareProfiles() Function END #################################

########################  compareVerifyProfiles() Function START #################################

def verifyProfile(speaker,profileVerify):
	for profile in profileVerify:
		if(profile == speaker):
			# print(profileVerify[profile])
			return profileVerify[profile]


########################  compareVerifyProfiles() Function END #################################



########################  verifyResponse() Function START #################################

def verifyResponse(filename):
	f = open(filename)
	line = f.readline()
	return line

########################  verifyResponse() Function END #################################





########################  extractCommand() Function START #################################

# sample = add 20 cedis to my account
# sample = add 0.50 cedis to my acoount
# sample = remove 20 cedis from my account 

def extractCommand(speech):
	speechArr = []
	# command = "" 
	# amount = 0.0

	for word in speech.split():
		if(word.lower() == "add" or word.lower() == "remove"):
			speechArr.append(word)
# 
		if(word.isdigit() == True):
			speechArr.append(float(word))
		

	# if(speechArr[0].lower() == "add" or speechArr[0].lower() == "remove"){
	# 	command = "Please Start Phrase with Add or Remove to Update Account"
	# 	amount = 0.0
	# # # The word is Add
	# # 	extract.append(speechArr[0])
	# }

	# command = speechArr[0]
	# amount = float(speechArr[1])

	return speechArr



def databaseHandler(arr,speaker):
	newQuery = conn.execute("SELECT NEWAMOUNT FROM Users WHERE NAME='"+speaker+"'")
	newAmount = 0
	currentNewAmount = 0

	if(arr[0].lower() == "add"):

		for row in newQuery:
			print("Extracted New Amount: ",row[0])
			newAmount = row[0]

		currentNewAmount =  arr[1] + newAmount
		print("Current New Amount: ",currentNewAmount)

		currentNewAmount = str(currentNewAmount)
		oldAmount = str(newAmount)

		conn.execute("UPDATE Users set NEWAMOUNT='"+currentNewAmount+"'WHERE NAME ='"+speaker+"'")
		conn.execute("UPDATE Users set OLDAMOUNT='"+oldAmount+"'WHERE NAME ='"+speaker+"'")


		conn.commit()

	elif(arr[0].lower() == "remove"):
		
		for row in newQuery:
			print("Extracted New Amount: ",row[0])
			newAmount = row[0]

		currentNewAmount =  newAmount - arr[1]
		print("Current New Amount: ",currentNewAmount)

		currentNewAmount = str(currentNewAmount)
		oldAmount = str(newAmount)

		conn.execute("UPDATE Users set NEWAMOUNT='"+currentNewAmount+"'WHERE NAME ='"+speaker+"'")
		conn.execute("UPDATE Users set OLDAMOUNT='"+oldAmount+"'WHERE NAME ='"+speaker+"'")

		conn.commit()

	else:
		print("There's an error reading command, Please Try Again")


# arr = ['remove',20.0]
# speaker = "Jojoe"


# Calling Functions To Test

getAudio("test.wav",FORMAT = pyaudio.paInt16, CHANNELS = 1, RATE = 16000,
                    CHUNK = 1024, RECORD_SECONDS=5)
#

filename2 = 'test.wav'
recognizeSpeaker(filename2,profilesString)


filename = "test.wav"
speech = recognizeSpeech(filename)


filename3 = 'profile.txt'
speaker = compareProfiles(filename3,profileDict)

if(speaker == "error"):
	print("System was not able to Recognize who the Speaker was, Please Try Again")
else:
	print("Speaker: " + speaker)
	print(" ")

	print("Please say the Phrase below as a Verification Step: ")
	print("My Voice Is My Passport Verify Me ")
	print(" ")

	# Record Again
	getAudio("test.wav",FORMAT = pyaudio.paInt16, CHANNELS = 1, RATE = 16000,
                    CHUNK = 1024, RECORD_SECONDS=8)

	# Use Recorded file to Run command Line Command for Speaker Verification
	profileVer = verifyProfile(speaker,profileVerify)
	verifySpeaker('test.wav',str(profileVer),speaker)
	# Do Comparision if command is accept

	response = verifyResponse('verify.txt')
	if(response == "Accept"):
		print(" ")
		print("System has Verified the Speaker: " + speaker)

		print("=========== Extracting Commands from Speech ============")

		print("Speech: " + speech)
		print(" ")

		command = extractCommand(speech)
		print(command)
		print(" ")

		if not command:
			print("Commands Were not Clearly Extracted, Please Try Again")
		elif(len(command) < 2):
			print("Commands Were not Clearly Extracted, Please Try Again")
		else:
			print("=========== Database Account Updates ============")
			databaseHandler(command,speaker)
			print("Successfully Updated Database")
	else:
		print("Sorry, The System Could Not Verify " + speaker)
		print("Please Try Again")



	



# databaseHandler(arr,speaker)
# cursor = conn.execute("SELECT ID, NAME, NEWAMOUNT, OLDAMOUNT from Users")
# for row in cursor:
#    print("ID = ", row[0])
#    print ("NAME = ", row[1])
#    print ("NEW = ", row[2])
#    print ("OLD= ", row[3], "\n")


# DATABASE INSERTION PART

# First check which User it is, if it is 
# Now check what value digit is 
# Check what the first command is if add or remove
# If add, add to old amount, set that to new amount
# if remove, subtract from old amount, set that to new amount





