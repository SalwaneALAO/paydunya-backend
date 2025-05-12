from flask import Flask, jsonify
import paydunya

app = Flask(__name__)

paydunya.setup(
    master_key="EDDEX5Mr-WSQl-c6jb-TMmQ-UwQTc1yv7ckr",
    private_key="test_private_yNP04l6bqx5uCGSxonSJxGb8Xf7",
    public_key="test_public_4JAELm9Ui79oErZUOEuncCDT8jy",
    token="5MDrHlaPvNfahMbQaBPZ",
    mode="test"  # ou "test" selon l’environnement
)

@app.route("/payment/paydunya", methods=["POST"])
def generate_invoice():
    invoice = paydunya.Invoice()
    invoice.add_item("Commande GARMONT", 1, 45000, "Parfum de luxe")
    if invoice.create():
        return jsonify({"url": invoice.url})
    else:
        return jsonify({"error": invoice.response_text}), 400

if __name__ == "__main__":
    app.run()
