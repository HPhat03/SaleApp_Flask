from flask import  Flask, render_template, request
import dao
app = Flask(__name__)
@app.route("/")
def index():
    kw = request.args.get("kw")
    return render_template("index.html",Cates = dao.get_categories(), Prod = dao.get_product(kw))


if __name__ == "__main__":#kiểm tra tế khi chạy có phải là main hay ko
    app.run(debug=True) #Khi làm nên bật cờ này lên để phát hiện lỗi, khi ra sản phẩm cho khách hàng thì nên tắt