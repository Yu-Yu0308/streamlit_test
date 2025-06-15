import streamlit as st
import datetime

with st.form(key='my_form'):
        
    # テキストボックス
    # 戻り値に値が入るタイミング
    ## 画面が更新されるとき
    ## テキストボックスからカーソルが離れると自動で更新
    name = st.text_input('Enter your name')
    address = st.text_input('Enter your address')
    
    # セレクトボックス
    options = ['子供（18歳未満）', '大人（18歳以上）', '高齢者（65歳以上）']
    age_category = st.selectbox('年齢層', options)   
    
    # 複数選択
    hobbies = st.multiselect(
        '趣味を選択してください', 
        ['読書', 'スポーツ', '音楽', '旅行'])
    
    # チェックボックス
    mail_subscribe = st.checkbox('メールマガジンを購読する')
    
    # スライダー
    height = st.slider('身長', min_value=100, max_value=250) 
    
    # 日付
    start_date = st.date_input('開始日', datetime.date(2023, 1, 1))   

    # カラーピッカー
    color = st.color_picker('テーマカラー', '#00f900') 

    # ボタン
    submit_button = st.form_submit_button('Submit')
    cancel_button = st.form_submit_button('Cancel')

    if submit_button:
        st.text(f'ようこそ！{name}さん!{address}に書籍を送りました!')
        st.text(f'年齢層: {age_category}')
        st.text(f'趣味: {", ".join(hobbies)}')
        st.text(f'メールマガジン購読: {"はい" if mail_subscribe else "いいえ"}')
        st.text(f'身長: {height} cm')
        st.text(f'開始日: {start_date}')
        st.text(f'選択したカラー: {color}')