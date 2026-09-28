import json
from django.shortcuts import render,redirect
from .forms import userform,lendform

# Create your views here.

def home(request):
    return render(request,'home.html')
# ========================  ADD BOOK =================================================

def form(request):
    
    if request.method== 'POST':
        form1 = userform(request.POST)
        if form1.is_valid():
            
            bid=form1.cleaned_data["bookId"]
            bname=form1.cleaned_data["bookname"]
            author=form1.cleaned_data["author"]
            publish=form1.cleaned_data["publisher"]
            pubyear=form1.cleaned_data["publicationYear"]
            quantity=form1.cleaned_data["quantity"]
          

            dic={
               'bid':bid,
               'bname':bname,
               'author':author,
               'pub':publish,
               'pubyear':pubyear,
               'quantity':quantity,
             
            }

            try:
                with open("library.json","r") as file:
                  lists=json.load(file)
            except:
                lists=[]
            lists.append(dic)

            with open("library.json","w") as file:
                  json.dump(lists,file,indent=4)  
        return redirect('form')
                   
    else:
     form1 = userform()
    return render(request,'form.html',{'form':form1})
# ========================= SHOW BOOK=================================================
def showbooks(request):
    with open("library.json","r") as file:
        lists=json.load(file)

    return render(request,'showbooks.html',{'lists':lists})

# ========================== LEND BOOK================================================
def lend_book(request):
    with open("library.json","r")as file:
        books=json.load(file)
        

    if request.method=='POST':
        form2 =lendform(request.POST)

        if form2.is_valid():
    
            personId=form2.cleaned_data["personId"]
            pname=form2.cleaned_data["pname"]
            lname=form2.cleaned_data["lname"]
            book_id=form2.cleaned_data["book_id"]
            book_name=form2.cleaned_data["book_name"]
            issue_date = form2.cleaned_data["issue_date"].strftime("%d/%m/%Y")
            return_date = form2.cleaned_data["return_date"].strftime("%d/%m/%Y")
            quant=form2.cleaned_data["quant"]

            dic2={
            'pid':personId,
            'pname':pname,
            'lname':lname,
            'book_id':book_id,
            'book_name':book_name,
            'issue_date':issue_date,
            'return_date':return_date,
            'quant':quant, 
            }

            for i in books:
              if int(i["bid"]) == book_id:
                if int(i["quantity"]) >= quant:
                   i["quantity"] = int(i["quantity"]) - quant

                else:   
                   return render(request, 'lend.html', {
                  'form': form2,
                   'error': f'We have  "{i["quantity"]}" of id "{i["bid"]}"!'})   

            with open("library.json","w")as file:
                json.dump(books,file,indent=4)            
            
            try:          
                with open("lend.json","r") as file:
                    list2=json.load(file)
            except:
                list2=[]
            list2.append(dic2)


            with open ("lend.json","w")as file:
                list2=json.dump(list2,file,indent=4)
            return redirect('lend')    
    else:
        form2=lendform()

      
        return render(request,'lend.html',{'form':form2} ) 

# ==============================Delete book ===========================================

def delete(request, book_id):

    with open("library.json", "r") as file:
        books = json.load(file)

    for i in books:
        if str(i["bid"]) == str(book_id):
            books.remove(i)
            break

    with open("library.json", "w") as file:
        json.dump(books, file, indent=4)

    return redirect("showbooks")
# ========================== Show Lend book  ==============================================
def showlend_books(request):
    with open("lend.json", "r") as file:
        books = json.load(file)

    return render(request, "lendbooks.html", {"books": books})

# ===============================Edit book ============================================
def edit(request,book_id):
    with open("library.json","r")as file:
        books=json.load(file)

    for i in books:
        if int(i["bid"])== int(book_id) :
            if request.method=="POST":
                i["bname"]=request.POST.get("name")
                i["aouthor"]=request.POST.get("aouthor")
                i["pub"]=request.POST.get("pub")
                i["pubyear"]=request.POST.get("pubyear")
                i["quantity"]=request.POST.get("quantity")


                with open("library.json","w")as file:
                   json.dump(books,file,indent=4)

                return redirect("showbooks")    

            return render(request,'edit.html',{'book':i})

# ======================================= ADD MEMBER ==================================
def addMember(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phon = request.POST.get('phon')

        dic = {
            'id': id,
            'name': name,
            'email': email,
            'phon':phon
        }

        try:
            with open("addMembers.json", "r") as file:
                members = json.load(file)
        except:
            members = []

        members.append(dic)

        with open("addMembers.json", "w") as file:
            json.dump(members, file, indent=4)

    return render(request, 'add_member.html')

# ================================ SHOW MEMBER =========================================

def show_member(request):
    with open("addMembers.json" ,"r")as file:
        members=json.load(file)
    return render(request,'show_member.html',{'members':members})

# ================================ EDITE MEMBER ========================================

def editMember(request,book_id):
    with open("addMembers.json","r")as file:
        members=json.load(file)

    for i in members:
        if int(i["id"]) == book_id:
        
        
            if request.method=="POST":
                i["id"]=request.POST.get("id")
                i["name"]=request.POST.get("name")
                i["email"]=request.POST.get("email")
                i["phon"]=request.POST.get("phon")
                with open("addMembers.json","w")as file:
                    json.dump(members,file,indent=4)  
                return redirect(show_member)    
         

            return render(request,'edit_member.html',{'member':i})
# ================================ DELETE MEMBER =======================================

def deletMember(request,book_id):
    with open("addMembers.json","r")as file:
        members=json.load(file)

    for i in members:
        if int(i["id"])==book_id:
            members.remove(i)  
            break 
    with open("addMembers.json","w")as file:
            json.dump(members,file,indent=4)  

    return redirect( show_member)   
# ==============================return search===========================================

def return_Search(request):
    lists=[]
    with open("library.json","r")as file:
        books=json.load(file)
        if request.method== 'POST':
            search= request.POST.get('searchValue')
            for i in books:
                if i['bid'] == search:

                    lists.append(i)

    return render(request,'return-search.html',{'lists':lists}) 

# ======================================== Return Form ================================
def return_form(request):
    lists=[]
    if request.method=='POST':
        bookId=int(request.POST.get("bookid"))
        # quant=int(request.POST.get("quantity"))

        with open("lend.json","r")as file:
           lend=json.load(file) 

           for l in lend:
               if l["book_id"]==bookId :
                   lists.append(l)

        return render(
            request,
            "show_return_book.html",
            {"lend_book": lists}
        )
    # this "lend_book"is from schow_return_book def

    return render(request,'return_form.html') 


# ========================== Show Return Book =========================================
def show_return_book(request):
    with open("lend.json","r")as file:
        lend_book=json.load(file)
    return render(request,'show_return_book.html',{'lend_book':lend_book})

# ================================== Return Books ======================================

def return_book(request,books_id):
        with open("library.json","r")as file:
           books=json.load(file)
 
        with open("lend.json","r")as file:
           lend=json.load(file) 

        for i in lend:
            if "book_id" in i:
                if int(i["book_id"]) == books_id:
                    quant =i["quant"]
                    i["quant"] -= quant

                    if i["quant"] == 0:
                        lend.remove(i)
                        break
                    
        for b in books:
            if int(b["bid"])== books_id:
                b["quantity"] +=quant 
                break     

        with open("library.json","w")as file:
            json.dump(books,file,indent=4) 

        with open("lend.json","w")as file:
            json.dump(lend,file,indent=4) 

        return redirect("show_return_book")




# get id and quantity from user 
# search in to borrwed books 
# remov from borrowed book 
# add to avilabel books










         



       




           













