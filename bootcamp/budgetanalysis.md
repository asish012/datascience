# Questions #
- How frequent I went to shopping/grocery? Number of entries per month?
-


# Schema #
- account                    object
+ category                   object
- currency                   object
+ amount                    float64
- ref_currency_amount       float64
- type                       object
- payment_type               object
- payment_type_local         object
+ note                       object
+ date                       object
- gps_latitude              float64
- gps_longitude             float64
- gps_accuracy_in_meters    float64
- warranty_in_month           int64
- transfer                     bool
+ payee                      object
+ labels                     object
+ envelope_id                 int64
- custom_category              bool

# Categories #
1. Food & Drinks
   1. Food & Drinks - Others
   2. Bar, cafe
   3. Groceries                 - 1000
   4. Restaurant, fast-food     - 1001
2. Shopping
   1. Shopping - Others
   2. Clothes & shoes           - 2000
   3. Drug-store, chemist       - 2011
   4. Electronics, accessories  - 2006
   5. Free time
   6. Gifts, joy                - 2007
   7. Health and beauty
   8. Home, garden
   9. Jewelry, accessories
   10. Pets, animals
   11. Stationery, tool
3. Housing
   1. Housing - Others
   2. Energy, utilities
   3. Maintenance, repairs
   4. Mortgage
   5. Property insurance
   6. Rent
   7. Service
4. Transportation
   1. Transportation - Others
   2. Business trips
   3. Long distance
   4. Public transport
   5. Taxi
5. Vehicle
   1. Vehicle - Others
   2. Fuel
   3. Leasing
   4. Parking
   5. Rentals
   6. Vehicle insurance
   7. Vehicle maintenance
6. Life & Entertainment
   1. Life & Entertainment - Others
   2. Active sport, fitness
   3. Alcohol, tobacco
   4. Books, audio, subscriptions
   5. Charity, gifts
   6. Culture, sport events
   7. Education, development
   8. Health care, doctor
   9. Hobbies
   10. Holidays, trips, hotels
   11. Life events
   12. Lottery, gambling
   13. TV, Streaming
   14. Wellness, beauty
7. Communication, PC
   1. Communication, PC - Others
   2. Internet
   3. Phone, cell phone
   4. Postal service
   5. Software, apps, games
8. Financial expenses
   1. Financial expenses - Others
   2. Advisory
   3. Charges, Fees
   4. Child Support
   5. Fines
   6. Insurances
   7. Loan, interests
   8. Taxes
9.  Investments
    1.  Investments - Others
    2.  Collections
    3.  Financial investments
    4.  Realty
    5.  Savings
    6.  Vehicles, chattels
10. Income
11. Others
    1.  Others - Others


| Groceries                   | 1000  |
| Restaurant, fast-food       | 1001  |
| Bar, cafe                   | 1002  |
| Clothes & shoes             | 2000  |
| Health and beauty           | 2002  |
| Home                        | 2004  |
| Electronics, accessories    | 2006  |
| Gifts, joy                  | 2007  |
| Stationery, tools           | 2008  |
| Shopping                    | 2010  |
| Drug-store, chemist         | 2011  |
| Rent                        | 3000  |
| Energy, utilities           | 3002  |
| Public transport            | 4000  |
| Fuel                        | 5000  |
| Parking                     | 5001  |
| Rentals                     | 5003  |
| Vehicle                     | 5004  |
| Health care, doctor         | 6000  |
| Wellness, beauty            | 6001  |
| Active sport, fitness       | 6002  |
| Culture, sport events       | 6003  |
| Life events                 | 6004  |
| Hobbies                     | 6005  |
| Books, audio, subscriptions | 6007  |
| TV, Streaming               | 6008  |
| Holiday, trips, hotels      | 6009  |
| Charity, gifts              | 6010  |
| Life & Entertainment        | 6013  |
| Phone, cell phone           | 7001  |
| Internet                    | 7002  |
| Software, apps, games       | 7003  |
| Skype extra                 | 7005  |
| Skype                       | 7005  |
| Insurances                  | 8001  |
| Fines                       | 8003  |
| Advisory                    | 8004  |
| Others                      | 11000 |


- VW Jahreswagen:
  - 10000 km
  - 13.12.2017 (2018)
  - 110 PS
  - Manual
  - Benzin
  - 4.8 l/100 km
  * 0.99% = _18700_
- VW Gebrauchtwagen:
  - 30990 km
  - 24.04.2017 (2017)
  - 116 PS
  - Manual
  - Diesel
  - 4.2 l/100 km
  - 2.99% = _17867_
- VW Gebrauchtwagen:
  - 18900 km
  - 30.12.2013 (2014)
  - 105 PS
  - Automatik
  - Benzin
  - 4.8 l/100 km
  - 2.99% = _15600_