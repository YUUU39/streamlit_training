
import streamlit as st
import pandas as pd
from PIL import Image

#title
st.title('This is the TITLE')
st.caption('This is the caption')

#header
st.header("This is the header")
st.subheader("This is the subheader")
st.text("text")
st.write("write")

#magic command

"""
# h1
## h2
### h3
#### h4

```python
import streamlit as st

#title
st.title('This is the TITLE')
st.caption('This is the caption')
```

"""

#Code
code_python="""
#Python
print('Python')
"""
st.code(code_python, language='python')

code_html="""
<!-- HTML -->
<h1>HTML</h1>
"""
st.code(code_html, language='html')

#markdown
st.markdown("This is **_italic_**")
st.markdown(":green[緑色]")
st.markdown("これは **:red[赤色で太字]** です")

"This is **_italic_**."
":green[緑色]です"
"これは **:red[赤色で太字]** です"

#DataFrame
df = pd.DataFrame([3,2,4,2],
                  ['りんご','みかん','いちご','もも'],
                  ['売上'],)
df

#textbox
textbox=st.text_input('この下はtextboxです')
textbox

#button
submit_btn=st.button("送信")
cancel_btn=st.button('キャンセル')
if submit_btn:
    st.text("送信ボタンが押されました")


#input widgets with control flow
with st.form(key='sales_form'):
    #textbox
    item=st.text_input("売れた商品名を記入してください")
    number=st.text_input("売れた数量を記入してください")
    #button
    submit_btn=st.form_submit_button('送信')
    cancel_btn=st.form_submit_button("キャンセル")
    if submit_btn:
        st.text(f"{item}が{number}個、売れました")


#問題１２　セレクトボックスで選んだ文字や数値をメッセージと一緒に表示するwidgetを作ってみましょう。

#input widgets with control flow
with st.form(key='select_form'):
    #selectbox
    item_select=st.selectbox(
        "売れた商品名を選んでください",
        ("-","いちご","もも","バナナ","りんご")
    )
    number_select=st.selectbox(
        "売れた数量を選んでください",
        ("0","1","2","3","4","5","6","7","8","9","10")
    )
    #button
    submit_btn=st.form_submit_button("送信")
    cancel_btn=st.form_submit_button("キャンセル")
    if submit_btn:
        st.text(f"{item_select}が{number_select}個、売れました")


#問題１３　ラジオボタンとセレクトボックスで選んだ文字や数値をメッセージと一緒に表示するwidgetを作ってみましょう。
with st.form(key='radio_form'):
    #radio
    item_select=st.radio(
        "売れた商品名を選んでください",
        ("-","いちご","もも","バナナ","りんご")
    )
    number_select=st.selectbox(
        "売れた数量を選んでください",
        ("0","1","2","3","4","5","6","7","8","9","10")
    )
    #button
    submit_btn=st.form_submit_button("送信")
    cancel_btn=st.form_submit_button("キャンセル")
    if submit_btn:
        st.text(f"{item_select}が{number_select}個、売れました")

#問題１４　マルチセレクト、ラジオボタン、セレクトボックスで選んだ文字や数値をメッセージと一緒に表示するwidgetを作ってみましょう。
with st.form(key='multiselect_form'):
    #multiselect
    sold_out=st.multiselect(
        "本日の売り切れ商品",
        ("-","いちご","もも","バナナ","りんご")
    )
    item_select= st.radio(
        "売れた商品名を選んでください",
        ("-","いちご","もも","バナナ","りんご")
    )
    number_select=st.selectbox(
        "売れた数量を選んでください",
        ("0","1","2","3","4","5","6","7","8","9","10")
    )
    #button
    submit_btn=st.form_submit_button("送信")
    cancel_btn=st.form_submit_button("キャンセル")
    if submit_btn:
        st.text(f"{item_select}が{number_select}個、売れました")
        st.text(f"{','.join(sold_out)}は売り切れています")

#問題１５　expanderを使って「よくあるお問い合わせ」を作ってみましょう。
#expander
st.write("よくあるお問い合わせ")
expander1=st.expander("営業時間は何時から何時までですか？")
expander1.write("営業時間は10:00から18:00までです")
expander2 = st.expander("定休日はいつですか？")
expander2.write("日曜日と祝日がお休みです")

#read_excel
st.markdown(" ### 月別売上")
sales_data=pd.read_excel("./data/sales_data.xlsx",engine="openpyxl")
sales_data

#問題１７　読み込んだexcelのデータをグラフにしてみましょう。

#line chart
st.markdown(" ### 月別売上推移")
st.line_chart(sales_data,x="営業月")

#bar_chart
st.bar_chart(sales_data,x="営業月")

#問題１８　マルチセレクトを使ってグラフをインタラクティブに比較してみましょう。

#checkbox with multiselect
if st.checkbox("マルチセレクトを使ってグラフを比較する"):
    #エクセルデータ読み込み
    sales_data=pd.read_excel("./data/sales_data.xlsx",engine="openpyxl")
    #multiselect
    selected_fruits=st.multiselect(
        "果物を選んでください",
        ["いちご","もも","バナナ","りんご"],
        ["いちご","もも","バナナ","りんご"]
    )
    if not selected_fruits:
        st.error("表示する果物が選択されていません。")
    else:
        st.line_chart(sales_data[selected_fruits])
        

#問題１９　画面を分割して選択したデータとグラフをインタラクティブに確認してみましょう。

#2columns
if st.checkbox("カラムを２つ並べてデータを表示する"):
    col_1,col_2=st.columns(2)
    with col_1:
        selected_fruits=st.selectbox("果物を選んでください",
                                     ["いちご","もも","バナナ","りんご"],
                                     key=2)
    with col_2:
        st.write(sales_data[selected_fruits])

#3columns
if st.checkbox("カラムを３つ並べてデータを表示する"):
    col_1,col_2,col_3 = st.columns(3)
    with col_1:
        select_fruits = st.selectbox("果物を選んでください",
                                     ["いちご","もも","バナナ","りんご"],
                                     key=3
                                     )
        with col_2:
            st.write(sales_data[select_fruits])
        with col_3:
            st.bar_chart(sales_data[select_fruits])

#問題２０　イメージ画像を表示してみましょう。
#image
image=Image.open("img/wave.png")
st.image(image)
st.image(image,width=500)
