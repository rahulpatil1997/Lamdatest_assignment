#input file
file = open("input.txt","r")

#string to store each character
string=""

#lists 
brand=[]
product=[]
price=[]

state=1
#state define where the string need to be added
# if state=1 ==> Brand 
# if state=2 ==> Product
# if state=3 ==> Price

#indies of lists 
brand_index=0
product_index=0
price_index=0

#sorting funtion
def sortng(brand,product,price):
    

    for i in range(len(price)):
        for j in range(len(price)-1):
            if(price[j]>price[j+1]):
                
                #changing position of price
                temp=price[j]
                price[j]=price[j+1]
                price[j+1]=temp

                #changeing position of brands
                temp=brand[j]
                brand[j]=brand[j+1]
                brand[j+1]=temp
                
                #changing position of products
                temp=product[j]
                product[j]=product[j+1]
                product[j+1]=temp


    #print all the sorted product list
    for v in range(len(price)):
      print(brand[v] +  "," + product[v] + "," +  price[v])
      print


col=0
for line in file:
    for character in line:
        
        #loop runs only when state is set to 1
        if state == 1:
            if character != ",":
                string+=character
            elif character == ",":
                brand.append(string)
                brand_index=brand_index+1
                string=""
                state=2
            continue


        #loop runs only when state is set to 2
        if state == 2:
            if character == "'":
                if character != ",":
                    col+=1
            if col == 2 and character==",":
                state=3
                product.append(string)
                string=""    
                product_index+=1
                col=0
    
            if character != ",":
                string+=character
            continue
            

        #loop runs only when state is set to 3
        if state == 3:
            if character != "," and character != "":
                string+=character
            
                pass
            elif character == "," or character == "":
                price.append(string)
                price_index=price_index+1
                string=""
                state=1
            continue
    price.append(string)
    break


#calling the sorting function.
sortng(brand,product,price)



