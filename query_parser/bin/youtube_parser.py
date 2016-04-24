import gdata.youtube
import gdata.youtube.service

#youtube api key=AIzaSyDhIco9O-WQkKanqV-9N3gf1c-7EfkWcdA

#hard code for query search
	
def SearchQuery(searc_q):

	obj_youtube=gdata.youtube.service.YouTubeService()
	obj_youtube.developer_key='AIzaSyDhIco9O-WQkKanqV-9N3gf1c-7EfkWcdA'
	query=gdata.youtube.service.YouTubeVideoQuery()
	query.vq=searc_q
	
	feed=obj_youtube.YouTubeQuery(query)
	return PrintVideoFeed(feed)


SearchQuery('babay')
