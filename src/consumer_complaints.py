import csv
import sys
from collections import Counter


#creating a dictionary to store the products      
prod_dict = dict()

# function to add the product, year as key and company as values in the dictionary 
def add_prod(product,year,company):
        if (product,year) in prod_dict.keys():           
            prod_dict[(product,year)].append(company)            
        else:
            prod_dict[(product,year)] = [company]


# function to seperate the required input cols and calling the function add_prod to add the companies        
def add_company(file_name):    
    with open(file_name) as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            #print(row)
            product = row[1]
            product = product.lower()
            
            year = row[0][0:4]
            
            company = row[7]
            company = company.lower()
            add_prod(product,year,company)
            

    return prod_dict           



# here we do all the calculation part and created a new list from the newly created dictionary
# which contains number of companies got complaints and how many distinct companies got
# same kind of complaint for the same product and in same year
def capture_result(prod_dict):
    # new dict
    new_dict = {}
    # new list
    new_list = []
    
    #sort the product dictionary using keys
    sort_keys = sorted(prod_dict.keys())

    for key in sort_keys:        

        # we use counter to get the number of times that company got complaints
        com = Counter(prod_dict[key])

        # maximum complaints received for 'm' company 
        m = max(com)
        j = com[m]

        # how many times the complaint registered for the product in a year
        k = len(prod_dict[key])

        # how many distinct companies got the complaint 
        t = (len(set(prod_dict[key])))

        a = round(j/k*100)
        
        new_dict[key]= [k,t,a]
       

    # appending all the values into a list p
    for key,val in new_dict.items():
        new_list.append([key[0],key[1],str(val[0]),str(val[1]),str(val[2])])

    #sort the p basing on the second values in the list i.e list[1] values
    new_list.sort(key = lambda x:x[1])

    return new_list



# generating an output csv file from the list p 
def output_report(output, file_name):
    with open(file_name,'w',encoding = 'utf-8',newline = "") as reports_csv:
        wr = csv.writer(reports_csv,delimiter = ',')
        wr.writerows(output)


if __name__ == "__main__":
    inp_file_name = sys.argv[1]
    out_file_name= sys.argv[2]

    prod_records = add_company(inp_file_name)

    r = capture_result(prod_records)
    output_report(r,out_file_name)
    
    
        
