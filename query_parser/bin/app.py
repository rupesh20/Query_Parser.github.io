import web
import os
from apiclient.errors import HttpError

import youtube_parser 
from web import form

urls=(
    '/','index'
)

app=web.application(urls,globals())

TEMPLATES=os.path.join(os.path.dirname(__file__),'templates')

render=web.template.render('TEMPLATES/')

myform=form.Form(
    form.Textbox("query"),
    
        )

class index:
    def GET(self):
        form=myform()
        return render.formtest(form)
    def POST(self):
        form=myform()
        if  not form.validates():
            return render.formtest(form)
        else:    
            var =str(form['query'].value)
            #obj=youtube_parser.Youtube_query_search()
            #data=obj.SearchQuery(str(form.d.query))
            
            try:
                data=youtube_parser.youtube_search(var,1)
                H_link=' <a href="https://www.youtube.com/watch?v={link}">{text}</a> '
                return H_link.format(link=data[0],text='link of video ')
            except HttpError, e:
                print "%d err:\n %s"%(e.resp.status,e.content)
           

if __name__ == '__main__':
    web.internalerror=web.debugerror
    app.run()       
