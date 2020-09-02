from pytube import YouTube
from os import path
import string
import random

url = input("Enter youtube video URL : ")
print('\nSearching video, please wait...\n')
try:

	yt = YouTube(url)

	print('\n Video found !, Title : ', yt.title, '\n')
	print('Options :')
	print('1.  Download Best Quality')
	print('2.  Download Audio Only')
	print('99. Exit\n')
	opt = input('Chose options : ')	

	randomTitle = ''
	if (path.exists(yt.title + ".mp4")):
		randomTitle = ''.join(random.sample(string.ascii_lowercase, 5))
		randomTitle = ' - ' + randomTitle
		
	print()

	if opt == "1":
		try:
			print('Downloading ...');						
			filters = yt.streams.filter(progressive=True, file_extension='mp4');
			filters.get_highest_resolution().download(filename=yt.title + randomTitle);
		except Exception as e:
			print(e)	
		finally:
			print('Download successfuly !')

	elif opt == "2":
		try:
			print('Downloading ...');
			filters = yt.streams.get_audio_only().download(filename=yt.title + randomTitle);
		except Exception as e:
			print(e)	
		finally:
			print('Download successfuly !')

	elif opt == "99":
		print('Close the program !')

	else :
		print('Command not found !')
		print('Close the program !')

except Exception as e:
	print("Video not found, plase input correct url !")