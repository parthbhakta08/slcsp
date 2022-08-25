import csv

def main():
    
    # opening the files in read mode
    slcsp_file = open('slcsp.csv') 
    plans = open('plans.csv')
    zips = open('zips.csv')
    
    # reading the file contents using csv module
    slcsp_reader = csv.reader(slcsp_file, delimiter=',')
    plans_reader = csv.reader(plans, delimiter=',')
    zips_reader = csv.reader(zips, delimiter=',') 
    
    new_rows = []
    
    # iterating through all the zipcodes in slcsp.csv
    for index, slcsp_row in enumerate(slcsp_reader):
        if index == 0:
            print(f'{", ".join(slcsp_row)}')
        else:
            # retrieving an individual zipcode
            zipcode = slcsp_row[0]
            zips.seek(0)
            plans.seek(0)
            
            # retrieving the corresponding rate area of the current zipcode
            rate_area = next((zip_row[4] for zip_row in zips_reader if zip_row[0] == zipcode), None)
            
            # retrieving all the silver rates of the current rate area of the current zipcode
            silver_rates = [plan_row[3] for plan_row in plans_reader if plan_row[4] == rate_area and plan_row[2] == 'Silver']
            
            # computing the the second lowest cost silver price
            slcsp = sorted(set(silver_rates))[1] if len(set(silver_rates)) > 1 else ''
            
            print(f'{zipcode}, {slcsp}')
            new_rows.append((zipcode, slcsp))
            
    # closing the files opened in read mode
    slcsp_file.close()
    plans.close()
    zips.close()
    
    # updating slcsp.csv file with slcsp rates
    write_slcsp_file = open('slcsp.csv', 'w+', newline='')
    slcsp_writer = csv.writer(write_slcsp_file)    
    slcsp_writer.writerow(('zipcode', 'rate'))
    slcsp_writer.writerows(new_rows)
    write_slcsp_file.close()

if __name__ == '__main__':
    main()