file = open("input.txt","r")

string=""

brand=[]
product=[]
price=[]

state=1
#state define where the string need to be added
# if state=1 ==> Brand 
# if state=2 ==> Product
# if state=3 ==> Price

brand_index=0
product_index=0
price_index=0

def sortng(brand,product,price):
    

    for i in range(len(price)):
        for j in range(len(price)-1):
            if(price[j]>price[j+1]):
                temp=price[j]
                price[j]=price[j+1]
                price[j+1]=temp

                temp=brand[j]
                brand[j]=brand[j+1]
                brand[j+1]=temp

                temp=product[j]
                product[j]=product[j+1]
                product[j+1]=temp



    for v in range(len(price)):
      print(brand[v] +  "," + product[v] + "," +  price[v])


col=0
for line in file:
    for character in line:
        #print(character)

        if state == 1:
            if character != ",":
               string+=character
            elif character == ",":
                brand.append(string)
                print("brand:", brand[brand_index])
                brand_index=brand_index+1
                string=""
                state=2
            continue

        if state == 2:
            if character == "'":
                if character != ",":
                    col+=1
            if col == 2 and character==",":
                state=3
                product.append(string)
                print("product:", product[product_index])
                string=""    
                product_index+=1
                col=0
    
            if character != ",":
                if character != " ":
                    string+=character
            continue
            
        if state == 3:
            if character != "," and character != "":
                string+=character
            
                pass
            elif character == "," or character == "":
                price.append(string)
                print("price:", price[price_index])
                price_index=price_index+1
                string=""
                state=1
            continue
    price.append(string)
    break


for v in range(len(price)):
    print(price[v])

sortng(brand,product,price)



