import json
import locale
import sys
import reports
import emails
from reports import generate as report


def load_data(filename):
     with open(filename) as json_file:
         data = json.load(json_file)
     return data

def format_car(car):
    return "{} {} ({})".format(
        car["car_make"], car["car_model"], car["car_year"])

def process_data(data):
    locale.setlocale(locale.LC_ALL, '')
    max_revenue = {"revenue": 0}
    max_sales = {"total_sales": 0, "car_model": ""}
    pop_car_yr = {}
    for item in data:
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item
        
        if item["total_sales"] > max_sales["total_sales"]:
            max_sales["total_sales"] = item["total_sales"]
            max_sales["car_model"] = item["car"]["car_model"]

        pop_car_yr[item["car"]["car_year"]] = pop_car_yr.get(item["car"]["car_year"], 0) +  item["total_sales"]

        pop_car_yr_sorted = sorted(pop_car_yr.items(), key=lambda a: a[1], reverse=True)
    
    summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(max_sales['car_model'], max_sales['total_sales']),
    "The most popular year was {} with {} sales.".format(pop_car_yr_sorted[0][0], pop_car_yr_sorted[0][1]),
  ]

    return summary

def cars_dict_to_table(car_data):
  
  table_cols = [["ID", "Car", "Price", "Total Sales"]]
  cars_list = []
  for item in car_data:
    cars_list.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
    cars_list.sort(key=lambda a: int(a[3]), reverse=True)
  return table_cols + cars_list

def main(argv):
    data = load_data("D:/notes/real_world_task/Qwiklabs_week_3/car_sales.json")
    summary = process_data(data)
    new_summary = ''.join(summary)
    print(summary)

    car_data = cars_dict_to_table(data)
    report("cars.pdf", "Sales summary for last month",new_summary, car_data)


    message = emails.generate("automation@example.com", "<studentID>@example.com", "Sales summary for last month", "\n".join(summary), "cars.pdf")
    emails.send(message)
  


if __name__ == "__main__":
       main(sys.argv)



  

    

















           