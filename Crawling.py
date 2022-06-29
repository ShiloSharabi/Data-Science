import asyncio
import pandas as pd
import math
import csv
from time import sleep
from playwright.async_api import async_playwright


async def getValofBoxCategories(element, xpath_str, message):
    print(f"############################-{message}-############################")
    val = float("NAN")
    try:
        if(await element.locator(xpath_str).is_visible()):
            val = await element.locator(xpath_str).inner_text()
    except:
        val = float("NAN")
    return val
 
async def getBoolValofBoxCategories(element, xpath_str, message):
    print(f"############################-{message}-############################")
    val = float("NAN")
    try:
        if(await element.locator(xpath_str).is_visible()):
            class_res = await element.locator(xpath_str).get_attribute("class")
            val = 0 if class_res.find('delete') != -1 else 1
    except:
        val = float("NAN")
    return val

async def syncLists(list, length):
    while len(list) <= length:
        list.append(float("NAN"))
    return list

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.yad2.co.il/realestate/forsale?topArea=19&area=17&city=7400&propertyGroup=apartments,houses");
        flag = False #True
        try :
            page_count = await page.locator("//button[@class='page-num']").inner_text()
            cur_page_count = 0
        except Exception as e:
            print("Can't locate element with the following locator: //button[@class='page-num'] \n'error message: '\n")
            print(e)
        price = []
        rooms = []
        floor = []
        square_meter = []
        property_status = []
        floors = []
        balcony = []
        parking = []
        typ = []
        neighborhood = []
        city = []
        propertyRe = []
        air_conditioning = []
        bars = []
        elevators = []
        kosher_kitchen = []
        boiler = []
        disabled_access = []
        shelter = []
        renovated = []
        storage = []
        air_conditioning_tadiran = []
        furniture = []
        flexible = []

        for i in range(0,int(page_count)):
            j = 0
            while(await page.locator(f"//*[@id='feed_item_{j}']").is_visible()):
                try:
                    element = page.locator(f"//*[@id='feed_item_{j}']")
                    xpath_str = f"//div[@class='rows']" if j != 21 else "//div[@class='right_col']"
                    await element.locator(xpath_str).click()
                    sleep(3)
                except:
                    price = await syncLists(price, j)
                    rooms = await syncLists(rooms, j)
                    floor = await syncLists(floor, j)
                    square_meter = await syncLists(square_meter, j)
                    property_status = await syncLists(property_status, j)
                    floors = await syncLists(floors, j)
                    balcony = await syncLists(balcony, j)
                    parking = await syncLists(parking, j)
                    typ = await syncLists(typ, j)
                    neighborhood = await syncLists(neighborhood, j)
                    city = await syncLists(city, j)
                    propertyRe = await syncLists(propertyRe, j)
                    air_conditioning = await syncLists(air_conditioning, j)
                    bars = await syncLists(bars, j)
                    elevators = await syncLists(elevators, j)
                    kosher_kitchen = await syncLists(kosher_kitchen, j)
                    boiler = await syncLists(boiler, j)
                    disabled_access = await syncLists(disabled_access, j)
                    shelter = await syncLists(shelter, j)
                    renovated = await syncLists(renovated, j)
                    storage = await syncLists(storage, j)
                    air_conditioning_tadiran = await syncLists(air_conditioning_tadiran, j)
                    furniture = await syncLists(furniture, j)
                    flexible = await syncLists(flexible, j)
                    j = j + 1
                    continue
                
                xpath_str = "//div[@class='left_col with_new_tab']/div[1]" if j != 21 else "//div[@id='feed_item_21_price']/span"
                price.append(await getValofBoxCategories(element, xpath_str, "Price"))
                print(price)
                print(j)
                print(f"Price for element {j}", price[j])

                xpath_str = "//div[@class='middle_col']"
                xpath_str += f"//span[@id='data_rooms_{j}']" if j != 21 else "//dt[@id='data_rooms_21']"
                rooms.append(await getValofBoxCategories(element, xpath_str, "Rooms"))
                print(f"Rooms for element {j}", rooms[j])
                
                xpath_str = "//div[@class='middle_col']"
                xpath_str += f"//span[@id='data_floor_{j}']" if j != 21 else "//dt[@id='data_floor_21']"
                floor.append(await getValofBoxCategories(element, xpath_str, "Floor"))
                print(f"Floor for element {j}", floor[j])
                
                xpath_str = "//div[@class='middle_col']"
                xpath_str += f"//span[@id='data_SquareMeter_{j}']" if j != 21 else "//dt[@id='data_SquareMeter_21']"
                square_meter.append(await getValofBoxCategories(element, xpath_str, "Square Meter"))
                print(f"Square Meter for element {j}", square_meter[j])
                
                xpath_str = f"//dl[@class='info_item']"
                xpath_str = "//dl[@class='info_item']/dt[text()='מצב הנכס']/../dd"
                property_status.append(await getValofBoxCategories(element, xpath_str, "Property Status"))
                print(f"Property Status for element {j}", property_status[j])
                
                xpath_str = "//dl[@class='info_item']/dt[text()='קומות בבנין']/../dd"
                floors.append(await getValofBoxCategories(element, xpath_str, "Floors"))
                print(f"Floors for element {j}", floors[j])
                
                xpath_str = "//dl[@class='info_item']/dt[text()='מרפסות']/../dd"
                balcony.append(await getValofBoxCategories(element, xpath_str, "Balcony"))
                print(f"Balcony for element {j}", balcony[j])
                
                xpath_str = "//dl[@class='info_item']/dt[text()='חניות']/../dd"
                parking.append(await getValofBoxCategories(element, xpath_str, "Parking"))
                print(f"Parking for element {j}", parking[j])
                
                if j != 21:
                    print("############################-TYP_NEIGBH_CITY-############################")
                    xpath_str = "//span[@class='subtitle']"
                    try:
                        typ_neighborhood_city = await element.locator(xpath_str).inner_text()
                        lst = typ_neighborhood_city.split(",")
                        typ.append(lst[0])
                        neighborhood.append(lst[1])
                        city.append(lst[-1])
                    except:
                        typ.append(float("NAN"))
                        neighborhood.append(float("NAN"))
                        city.append(float("NAN"))
                else:
                    typ.append(await getValofBoxCategories(element,"//span[@class='neighborhood']//preceding-sibling::span", "TYP"))
                    temp_neighborhood = await getValofBoxCategories(element,"//span[@class='neighborhood']", "NEIGBH")
                    try:
                        temp_neighborhood = float("NAN") if math.isnan(temp_neighborhood) == True else temp_neighborhood.replace(',','')
                    except:
                        temp_neighborhood = float("NAN")
                    neighborhood.append(temp_neighborhood)
                    city.append(await getValofBoxCategories(element,"//span[@class='neighborhood']//following-sibling::span", "CITY"))
                print(f"{typ[j]}, {neighborhood[j]}, {city[j]}", "Typ-Neighborhood-City")
                
                xpath_str = "//span[text()='נכס בבלעדיות']/.."
                propertyRe.append(await getBoolValofBoxCategories(element, xpath_str, "PropertyRe"))
                print(f"PropertyRe for element {j}", propertyRe[j])
                
                xpath_str = "//span[text()='מיזוג']/.."
                air_conditioning.append(await getBoolValofBoxCategories(element, xpath_str, "AirConditioning"))
                print(f"AirConditioning for element {j}", air_conditioning[j])
                
                xpath_str = "//span[text()='סורגים']/.."
                bars.append(await getBoolValofBoxCategories(element, xpath_str, "Bars"))
                print(f"Bars for element {j}", bars[j])
                
                xpath_str = "//span[text()='מעלית']/.."
                elevators.append(await getBoolValofBoxCategories(element, xpath_str, "Elevators"))
                print(f"Elevators for element {j}", elevators[j])
                
                xpath_str = "//span[text()='מטבח כשר']/.."
                kosher_kitchen.append(await getBoolValofBoxCategories(element, xpath_str, "KosherKitchen"))
                print(f"KosherKitchen for element {j}", kosher_kitchen[j])
                
                xpath_str = "//span[text()='דוד שמש']/.."
                boiler.append(await getBoolValofBoxCategories(element, xpath_str, "Boiler"))
                print(f"Boiler for element {j}", boiler[j])
                
                xpath_str = "//span[text()='גישה לנכים']/.."
                disabled_access.append(await getBoolValofBoxCategories(element, xpath_str, "DisabledAccess"))
                print(f"DisabledAccess for element {j}", disabled_access[j])
                
                xpath_str = """//span[text()='ממ"ד']/.."""
                shelter.append(await getBoolValofBoxCategories(element, xpath_str, "Shelter"))
                print(f"Shelter for element {j}", shelter[j])
                
                xpath_str = "//span[text()='משופצת']/.."
                renovated.append(await getBoolValofBoxCategories(element, xpath_str, "Renovated"))
                print(f"Renovated for element {j}", renovated[j])
                
                xpath_str = "//span[text()='מחסן']/.."
                storage.append(await getBoolValofBoxCategories(element, xpath_str, "Storage"))
                print(f"Storage for element {j}", storage[j])
                
                xpath_str = "//span[text()='מזגן תדיראן']/.."
                air_conditioning_tadiran.append(await getBoolValofBoxCategories(element, xpath_str, "AirConditioningTadiran"))
                print(f"AirConditioningTadiran for element {j}", air_conditioning_tadiran[j])
                
                xpath_str = "//span[text()='ריהוט']/.."
                furniture.append(await getBoolValofBoxCategories(element, xpath_str, "Furniture"))
                print(f"Furniture for element {j}", furniture[j])
                
                xpath_str = "//span[text()='ריהוט']/.."
                flexible.append(await getBoolValofBoxCategories(element, xpath_str, "Flexible"))
                print(f"Flexible for element {j}", flexible[j])
                print("--------------------------------------")
                print(f"|        element number: {j}         |")
                print("--------------------------------------")
                print("==============================================================================================")
                j = j + 1
            print(f"page number: {i}")
            await page.locator("//span[@class='navigation-button-text next-text' and text()='הבא']").click()
            sleep(3.0)

        await browser.close()
        df = pd.DataFrame(
            {
                'חדרים': rooms,
                'קומה': floor,
                'מ"ר': square_meter,
                'מצב הנכס': property_status,
                'קומות בבנין': floors,
                'מרפסות': balcony,
                'חניות': parking,
                'סוג נכס': typ,
                'שכונה': neighborhood,
                'עיר': city,
                'תיווך': propertyRe,
                'מיזוג': air_conditioning,
                'סורגים': bars,
                'מעלית': elevators,
                'מטבח כשר': kosher_kitchen,
                'דוד שמש': boiler,
                'גישה לנכים': disabled_access,
                'ממ"ד': shelter,
                'משופצת': renovated,
                'מחסן': storage,
                'מזגן תדיראן': air_conditioning_tadiran,
                'ריהוט': furniture,
                'גמיש': flexible,
                'מחיר': price,
            }
        )
        print(df)
        if flag:
            df.to_csv('C:/Users/shilo.sharabi/OneDrive - Sapiens/Desktop/Hit/Data Science/Final Project/DataSet.csv', mode='w', header=True, encoding='utf-8-sig')
        else:
            df.to_csv('C:/Users/shilo.sharabi/OneDrive - Sapiens/Desktop/Hit/Data Science/Final Project/DataSet.csv', mode='a', header=False, encoding='utf-8-sig')
asyncio.run(main())

#to run this file use the following command: "python Crawling.py"