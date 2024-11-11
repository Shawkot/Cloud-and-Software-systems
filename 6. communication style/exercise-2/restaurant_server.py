from concurrent import futures
import grpc
import sys
from proto import restaurant_pb2
from proto import restaurant_pb2_grpc

RESTAURANT_ITEMS_FOOD = ["chips", "fish", "burger", "pizza", "pasta", "salad"]
RESTAURANT_ITEMS_DRINK = ["water", "fizzy drink", "juice", "smoothie", "coffee", "beer"]
RESTAURANT_ITEMS_DESSERT = ["ice cream", "chocolate cake", "cheese cake", "brownie", "pancakes", "waffles"]

class Restaurant(restaurant_pb2_grpc.RestaurantServicer):
    def FoodOrder(self, request, context):
        return self._process_order(request, RESTAURANT_ITEMS_FOOD)

    def DrinkOrder(self, request, context):
        return self._process_order(request, RESTAURANT_ITEMS_DRINK)

    def DessertOrder(self, request, context):
        return self._process_order(request, RESTAURANT_ITEMS_DESSERT)

    def MealOrder(self, request, context):
        # Check if exactly 3 items are ordered
        if len(request.items) != 3:
            return self._create_response(request.orderID, restaurant_pb2.RestaurantResponse.Status.REJECTED, request.items)
        
        # Validate order structure: [Food, Drink, Dessert]
        food, drink, dessert = request.items
        if food in RESTAURANT_ITEMS_FOOD and drink in RESTAURANT_ITEMS_DRINK and dessert in RESTAURANT_ITEMS_DESSERT:
            return self._create_response(request.orderID, restaurant_pb2.RestaurantResponse.Status.ACCEPTED, request.items)
        else:
            return self._create_response(request.orderID, restaurant_pb2.RestaurantResponse.Status.REJECTED, request.items)

    def _process_order(self, request, valid_items):
        # Check if all items are in the valid category list
        if all(item in valid_items for item in request.items):
            return self._create_response(request.orderID, restaurant_pb2.RestaurantResponse.Status.ACCEPTED, request.items)
        else:
            return self._create_response(request.orderID, restaurant_pb2.RestaurantResponse.Status.REJECTED, request.items)

    def _create_response(self, orderID, status, items):
        # Prepare itemsMessage with item names
        itemsMessage = [restaurant_pb2.items(itemName=item) for item in items]
        return restaurant_pb2.RestaurantResponse(orderID=orderID, status=status, itemMessage=itemsMessage)

def serve():
    # Retrieve port number from command line arguments
    port = sys.argv[1] if len(sys.argv) > 1 else '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    restaurant_pb2_grpc.add_RestaurantServicer_to_server(Restaurant(), server)
    server.add_insecure_port(f'localhost:{port}')
    server.start()
    print(f"Server started on port {port}")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
