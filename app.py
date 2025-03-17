from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load Excel
file_path = "MennekesPL.xlsx"
df = pd.read_excel(file_path)
df.columns = df.columns.str.strip()
df['Product Code'] = df['Product Code'].astype(str)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

@app.route("/get_price", methods=["GET"])
def get_price():
    product_code = request.args.get("product_code")
    result = df.loc[df['Product Code'] == str(product_code), 'Price']
    price = result.iloc[0] if not result.empty else "Product not found."
    return jsonify({"Product Code": product_code, "Price": price})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
