import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    validate_side(args.side)
    validate_order_type(args.type)

    client = get_client()

    print("\nOrder Request Summary")
    print("----------------------")
    print("Symbol:", args.symbol)
    print("Side:", args.side)
    print("Type:", args.type)
    print("Quantity:", args.quantity)
    print("Price:", args.price)

    order = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\nOrder Response")
    print("----------------------")
    print("Order ID:", order["orderId"])
    print("Status:", order["status"])
    print("Executed Quantity:", order["executedQty"])

except Exception as e:

    print("Error:", e)