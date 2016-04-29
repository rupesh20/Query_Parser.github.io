#!/usr/bin/python
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import sys
import json

reload(sys) # system unicode and encoding checking k liye hai 

sys.setdefaultencoding('utf8') # unicode encode codec error ko durr krdiya hai  isne

api_key='-XXXXXX-'# meta data ko access krne k liye

# function to search on the list of data of videos and print the results of the query passed as a arguments
def youtube_search(var, n):

	service= build('youtube','v3',developerKey=api_key)# object service of class build 

	search_response = service.search().list(
			q=var,#options m s query nikal li gai hai	
			part="id,snippet", #part mtlb kya milega hame,id/snippet
			maxResults=n #no of results of search  
		).execute()
	
	videos= [ ] #list of videos 
	#print sys.getdefaultencoding()
	
	#json data dumping i the text file for thinking purpose
	with open('1.txt','w') as outfile:
		json.dump(search_response,outfile)

	for search_res in search_response.get("items",[]):
		if search_res["id"]["kind"]== "youtube#video":
			videos.append(" %s "%(search_res["id"]["videoId"]))

	return videos		

"""if __name__ == '__main__':
	argparser.add_argument("--q",help="Search term", default="Google")
	argparser.add_argument("--max-results",help="Max results",default=25)
	args=argparser.parse_args()

	try:
		youtube_search(args)
	except HttpError, e:
		print "%d err:\n %s"%(e.resp.status,e.content)"""
