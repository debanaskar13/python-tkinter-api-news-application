from tkinter import *
import requests
from PIL import ImageTk,Image



class newsapp:
	def __init__(self):
		self.root=Tk()

		self.root.title("News Application")
		self.root.minsize(400,600)
		self.root.maxsize(400,600)
		self.root.resizable(0,0)
		self.root.configure(background="#7D0552")

		self.label2=Label(self.root,text="ApnaNEWZ 24*7",font=("Times",25,"bold"),fg="#fff",bg="#7D0552")
		self.label2.pack(pady=(5,20))

		self.label3=Label(self.root,text="Enter your topic :",font=("Times",20,"italic"),fg="#fff",bg="#7D0552")
		self.label3.pack(pady=(5,20))

		self.topicVar=StringVar()

		self.topic=Entry(self.root,bg="#fff",textvariable=self.topicVar)
		self.topic.pack(pady=(10,20),ipady=3)
		self.topic.focus()
		self.topic.bind("<Return>",lambda event:self.fetch())

		self.search_btn=Button(self.root,text="Search",fg="#fff",bg="#7D0552",command=lambda:self.fetch())
		self.search_btn.pack(pady=(10,10))


		self.root.mainloop()

	def clear(self):
		for i in self.root.pack_slaves():
			i.destroy()

	def fetch(self):
		self.term=self.topicVar.get()
		url=f"https://newsapi.org/v2/everything?q={self.term}&apiKey=df2228b649e14c3e836627362b93df70"
		self.response=requests.get(url).json()
		self.num=len(self.response['articles'])
		

		self.details()

	def details(self,mode=0,index=0):

		self.title=self.response['articles'][index]['title']
		self.name=self.response['articles'][index]['source']['name']
		self.author=self.response['articles'][index]['author']
		self.description=self.response['articles'][index]['description']
		self.publisheddate=self.response['articles'][index]['publishedAt']
		self.url=self.response['articles'][index]['url']
		self.image=self.response['articles'][index]['urlToImage']

		self.clear()

		self.root.configure(background="#7D0552")

		

		# self.label0=Label(self.root,self.image,bg="#7D0552")
		# self.label0.pack(pady=(5,10))

		self.label1=Label(self.root,text=self.title,font=("Times",15,"bold",'underline' ),fg="white",bg="#7D0552")
		self.label1.configure(width=300,wraplength=300)
		self.label1.pack(pady=(5,10))

		self.frame1=Frame(self.root)
		self.frame1.configure(background='#7D0552')
		self.frame1.pack(pady=(5,10))

		self.label2=Label(self.frame1,text=self.name,font=("Times",12,"bold"),fg="white",bg="#7D0552")
		self.label2.configure(width=300,wraplength=300)
		self.label2.pack(side='left',pady=(5,10))

		self.frame2=Frame(self.root)
		self.frame2.configure(background='#7D0552')
		self.frame2.pack(pady=(5,10))

		self.label4=Label(self.frame2,text=self.description,font=("Times",12,"roman"),fg="white",bg="#7D0552")
		self.label4.configure(width=300,wraplength=300,justify=LEFT)
		self.label4.pack(pady=(5,10))

		if self.author!=None:
			self.label3=Label(self.frame2,text="\t\tAuthor : "+self.author,font=("Times",12,"bold"),fg="white",bg="#7D0552")
			self.label3.configure(width=400,wraplength=400,justify=RIGHT)
			self.label3.pack(side='right',pady=(5,10))

		self.frame=Frame(self.root)
		self.frame.configure(background='#7D0552')
		self.frame.pack(side=BOTTOM,pady=(5,10))

		if index!=0:
			self.search_btn=Button(self.frame,text="Previous",bg="#fff",command=lambda:self.details(index=index-1))
			self.search_btn.pack(side="left",pady=(10,10))

		if index!=self.num-1:
			self.search_btn=Button(self.frame,text="Next",bg="#fff",command=lambda:self.details(index=index+1))
			self.search_btn.pack(side="right",pady=(10,10))

		
		


obj=newsapp()