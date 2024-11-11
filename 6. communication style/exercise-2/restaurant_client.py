import grpc
import sys
from proto import restaurant_pb2
from proto import restaurant_pb2_grpc

def test_food_order(stub, order_id, items):
    request = restaurant_pb2.RestaurantRequest(orderID=order_id, items=items)
    response = stub.FoodOrder(request)
    print(f"FoodOrder Response: orderID={response.orderID}, status={restaurant_pb2.RestaurantResponse.Status.Name(response.status)}, itemMessage={[item.itemName for item in response.itemMessage]}")

def test_drink_order(stub, order_id, items):
    request = restaurant_pb2.RestaurantRequest(orderID=order_id, items=items)
    response = stub.DrinkOrder(request)
    print(f"DrinkOrder Response: orderID={response.orderID}, status={restaurant_pb2.RestaurantResponse.Status.Name(response.status)}, itemMessage={[item.itemName for item in response.itemMessage]}")

def test_dessert_order(stub, order_id, items):
    request = restaurant_pb2.RestaurantRequest(orderID=order_id, items=items)
    response = stub.DessertOrder(request)
    print(f"DessertOrder Response: orderID={response.orderID}, status={restaurant_pb2.RestaurantResponse.Status.Name(response.status)}, itemMessage={[item.itemName for item in response.itemMessage]}")

def test_meal_order(stub, order_id, items):
    request = restaurant_pb2.RestaurantRequest(orderID=order_id, items=items)
    response = stub.MealOrder(request)
    print(f"MealOrder Response: orderID={response.orderID}, status={restaurant_pb2.RestaurantResponse.Status.Name(response.status)}, itemMessage={[item.itemName for item in response.itemMessage]}")

def run():
    server_port = sys.argv[1] if len(sys.argv) > 1 else "50051"
    with grpc.insecure_channel(f'localhost:{server_port}') as channel:
        stub = restaurant_pb2_grpc.RestaurantStub(channel)
        
        # Test cases
        print("\n--- Testing FoodOrder ---")
        test_food_order(stub, "order1", ["chips", "burger"])

        print("\n--- Testing DrinkOrder ---")
        test_drink_order(stub, "order2", ["water", "juice", "beer"])

        print("\n--- Testing DessertOrder ---")
        test_dessert_order(stub, "order3", ["ice cream", "brownie"])

        print("\n--- Testing MealOrder (correct order) ---")
        test_meal_order(stub, "order4", ["pizza", "coffee", "pancakes"])

        print("\n--- Testing MealOrder (incorrect order) ---")
        test_meal_order(stub, "order5", ["pasta", "pancakes", "water"])  # incorrect order

if __name__ == "__main__":
    run()
