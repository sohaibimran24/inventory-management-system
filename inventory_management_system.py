# ============================================
# Inventory Management System
# Author: Muhammad Sohaib Imran
# FAST-NUCES, Lahore | FinTech
# ============================================

class Product:
    """Represents a single product in the inventory."""

    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (f"ID: {self.product_id} | Name: {self.name} | Category: {self.category} "
                f"| Price: Rs.{self.price:.2f} | Stock: {self.quantity}")

    def get_total_value(self):
        """Returns total value of this product in stock."""
        return self.price * self.quantity


class Inventory:
    """Manages all products in the inventory."""

    def __init__(self):
        self.products = {}  # product_id -> Product
        self._next_id = 1

    def add_product(self, name, category, price, quantity):
        """Add a new product to inventory."""
        product_id = f"P{self._next_id:03d}"
        product = Product(product_id, name, category, price, quantity)
        self.products[product_id] = product
        self._next_id += 1
        print(f"\n✅ Product added successfully! Assigned ID: {product_id}")
        return product_id

    def remove_product(self, product_id):
        """Remove a product from inventory."""
        if product_id in self.products:
            name = self.products[product_id].name
            del self.products[product_id]
            print(f"\n✅ '{name}' removed from inventory.")
        else:
            print(f"\n❌ Product ID '{product_id}' not found.")

    def update_stock(self, product_id, quantity):
        """Update the stock quantity of a product."""
        if product_id in self.products:
            self.products[product_id].quantity = quantity
            print(f"\n✅ Stock updated for '{self.products[product_id].name}'. New quantity: {quantity}")
        else:
            print(f"\n❌ Product ID '{product_id}' not found.")

    def update_price(self, product_id, price):
        """Update the price of a product."""
        if product_id in self.products:
            self.products[product_id].price = price
            print(f"\n✅ Price updated for '{self.products[product_id].name}'. New price: Rs.{price:.2f}")
        else:
            print(f"\n❌ Product ID '{product_id}' not found.")

    def search_by_name(self, keyword):
        """Search products by name keyword."""
        results = [p for p in self.products.values() if keyword.lower() in p.name.lower()]
        if results:
            print(f"\n🔍 Search results for '{keyword}':")
            for p in results:
                print(f"  {p}")
        else:
            print(f"\n❌ No products found matching '{keyword}'.")
        return results

    def search_by_category(self, category):
        """Search products by category."""
        results = [p for p in self.products.values() if category.lower() in p.category.lower()]
        if results:
            print(f"\n🔍 Products in category '{category}':")
            for p in results:
                print(f"  {p}")
        else:
            print(f"\n❌ No products found in category '{category}'.")
        return results

    def display_all(self):
        """Display all products in inventory."""
        if not self.products:
            print("\n📦 Inventory is empty.")
            return
        print("\n" + "=" * 70)
        print("📦  FULL INVENTORY")
        print("=" * 70)
        for p in self.products.values():
            print(f"  {p}")
        print("=" * 70)

    def low_stock_alert(self, threshold=5):
        """Show products with stock below threshold."""
        low = [p for p in self.products.values() if p.quantity <= threshold]
        if low:
            print(f"\n⚠️  LOW STOCK ALERT (quantity <= {threshold}):")
            for p in low:
                print(f"  {p}")
        else:
            print(f"\n✅ All products have sufficient stock (above {threshold} units).")

    def total_inventory_value(self):
        """Calculate and display total value of entire inventory."""
        total = sum(p.get_total_value() for p in self.products.values())
        print(f"\n💰 Total Inventory Value: Rs.{total:,.2f}")
        return total

    def display_summary(self):
        """Display a summary of the inventory."""
        total_products = len(self.products)
        total_items = sum(p.quantity for p in self.products.values())
        total_value = sum(p.get_total_value() for p in self.products.values())
        categories = set(p.category for p in self.products.values())

        print("\n" + "=" * 40)
        print("📊  INVENTORY SUMMARY")
        print("=" * 40)
        print(f"  Total Products   : {total_products}")
        print(f"  Total Items      : {total_items}")
        print(f"  Total Value      : Rs.{total_value:,.2f}")
        print(f"  Categories       : {', '.join(categories) if categories else 'None'}")
        print("=" * 40)


def main_menu():
    """Display main menu."""
    print("\n" + "=" * 40)
    print("   INVENTORY MANAGEMENT SYSTEM")
    print("   Muhammad Sohaib Imran | FAST")
    print("=" * 40)
    print("  1. Add Product")
    print("  2. Remove Product")
    print("  3. Update Stock")
    print("  4. Update Price")
    print("  5. View All Products")
    print("  6. Search by Name")
    print("  7. Search by Category")
    print("  8. Low Stock Alert")
    print("  9. Total Inventory Value")
    print(" 10. Inventory Summary")
    print("  0. Exit")
    print("=" * 40)


def run():
    """Main program loop."""
    inventory = Inventory()

    # Add some sample data
    inventory.add_product("Laptop", "Electronics", 150000, 10)
    inventory.add_product("Mouse", "Electronics", 1500, 50)
    inventory.add_product("Notebook", "Stationery", 200, 3)
    inventory.add_product("Office Chair", "Furniture", 25000, 8)
    inventory.add_product("Pen Pack", "Stationery", 150, 2)

    while True:
        main_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            name = input("Product Name: ").strip()
            category = input("Category: ").strip()
            try:
                price = float(input("Price (Rs.): "))
                quantity = int(input("Quantity: "))
                inventory.add_product(name, category, price, quantity)
            except ValueError:
                print("❌ Invalid price or quantity. Please enter numbers.")

        elif choice == "2":
            product_id = input("Enter Product ID to remove: ").strip().upper()
            inventory.remove_product(product_id)

        elif choice == "3":
            product_id = input("Enter Product ID: ").strip().upper()
            try:
                quantity = int(input("New Quantity: "))
                inventory.update_stock(product_id, quantity)
            except ValueError:
                print("❌ Invalid quantity.")

        elif choice == "4":
            product_id = input("Enter Product ID: ").strip().upper()
            try:
                price = float(input("New Price (Rs.): "))
                inventory.update_price(product_id, price)
            except ValueError:
                print("❌ Invalid price.")

        elif choice == "5":
            inventory.display_all()

        elif choice == "6":
            keyword = input("Enter product name to search: ").strip()
            inventory.search_by_name(keyword)

        elif choice == "7":
            category = input("Enter category to search: ").strip()
            inventory.search_by_category(category)

        elif choice == "8":
            try:
                threshold = int(input("Enter low stock threshold (default 5): ") or "5")
            except ValueError:
                threshold = 5
            inventory.low_stock_alert(threshold)

        elif choice == "9":
            inventory.total_inventory_value()

        elif choice == "10":
            inventory.display_summary()

        elif choice == "0":
            print("\n👋 Goodbye! - Muhammad Sohaib Imran\n")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    run()
