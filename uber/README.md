# This is UBER APPLICATION

## Accounts
- Drivers *
- Clients *

## Orders
- Orders *
- Payments *

## Others
- Cars

## Score system
- Rate


## Features
- Order car and driver for ride *
- Pay for a ride *
- Rate a driver for a ride

## Endpoint 
URL = http://api.app.com

POST /login
GET /logout
GET /orders/ = get list
POST /orders/ = create
GET /orders/12 = get one item
POST /orders/12 = update one item
DELETE /orders/12 = delete one item

GET /new_orders/ = get list orders without assigned driver
GET /new_orders/<id> = assigned this order to me

GET /nearby_drivers = get available drivers list