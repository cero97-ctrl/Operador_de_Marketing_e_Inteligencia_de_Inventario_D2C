import os
import shopify
import json
import argparse
from dotenv import load_dotenv

def get_inventory(threshold):
    load_dotenv()
    shop_url = os.getenv("SHOPIFY_SHOP_URL")
    api_version = '2024-01'
    access_token = os.getenv("SHOPIFY_ACCESS_TOKEN")

    if not all([shop_url, access_token]):
        print(json.dumps({"error": "Faltan credenciales en el archivo .env"}))
        return

    session = shopify.Session(shop_url, api_version, access_token)
    shopify.ShopifyResource.activate_session(session)

    inventory_report = {
        "out_of_stock": [],
        "low_stock": [],
        "summary": {"total_checked": 0}
    }

    try:
        # Usamos iterador para no cargar miles de productos a la vez en RAM
        products = shopify.Product.find()
        for product in products:
            for variant in product.variants:
                inventory_report["summary"]["total_checked"] += 1
                stock = variant.inventory_quantity
                
                item_data = {
                    "id": variant.id,
                    "title": f"{product.title} - {variant.title}",
                    "sku": variant.sku,
                    "stock": stock
                }

                if stock <= 0:
                    inventory_report["out_of_stock"].append(item_data)
                elif stock <= threshold:
                    inventory_report["low_stock"].append(item_data)

        os.makedirs('.tmp', exist_ok=True)
        output_path = '.tmp/inventory_report.json'
        with open(output_path, 'w') as f:
            json.dump(inventory_report, f, indent=4)
        
        print(json.dumps({"status": "success", "file": output_path, "counts": {
            "out_of_stock": len(inventory_report["out_of_stock"]),
            "low_stock": len(inventory_report["low_stock"])
        }}))

    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--threshold", type=int, default=5)
    args = parser.parse_args()
    get_inventory(args.threshold)