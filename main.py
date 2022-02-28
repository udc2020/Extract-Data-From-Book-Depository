from bs4 import BeautifulSoup
import requests 

#Store All Data 
book_data = []

# Pages in WebSite 
pages = 1


# Access into pages 
for page in range(pages):
   # Url must have Query increament 
   URL = f'https://www.bookdepository.com/search?searchTerm=programming&page={page}'
   
   # Use Requests & BeautifulSoup  
   page_data = requests.get(URL).text
   soup = BeautifulSoup(page_data,"lxml")
   
   all_books = soup.find("div",class_="tab search")
   books  = all_books.find_all('div',class_="book-item")

   for book in books : 
      #Extarct Combain Data 
      book_title = book.find("h3","title").text.strip()
      book_link = "https://www.bookdepository.com/" + book.find("h3","title").a.attrs['href']
      book_author = book.find("p","author").text.strip()
      book_published = book.find("p","published").text.strip()
      book_price = book.find("p","price").text.strip()
      

      all_data = requests.get(book_link).text
      soup2 = BeautifulSoup(all_data,"lxml")
      discription = soup2.find("div",class_="item-excerpt trunc").text.strip()

      # Make Structure for data 
      store_book = {
         "title":book_title,
         "link":book_link,
         "author":book_author,
         "publiched":book_published,
         "price":book_price,
         "discription":discription[:300].replace("\n","").replace("  ","") + "..."
      }
      # Add All data 
      book_data.append(store_book)

   

# Use data with stored him in text file 
for index , data in enumerate(book_data):
   
   
   with open('./data.txt',"a") as data_file:
      data_file.write(book_data[index]["title"]+"\n")
      data_file.write(book_data[index]["author"] +"\n")
      data_file.write(book_data[index]["price"]+"\n")
      data_file.write("==="*10)
      data_file.write("\n")
      
      print("save data" + str(index))
      
   
   


