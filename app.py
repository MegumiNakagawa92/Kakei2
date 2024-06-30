import streamlit as st
import numpy as np

st.title("家計診断アプリ")
st.write("あなたの家計を診断します！")
st.sidebar.title("費目別入力欄") 
month = st.sidebar.selectbox("何月の家計ですか？",
 ["１月", "２月", "３月","４月","５月","６月","７月","８月","９月","１０月","１１月","１２月"],
 index = 0, placeholder = "月を選択する")
st.sidebar.write(f"{month}の収支内訳を入力してください")

number1 = st.sidebar.number_input("収入１",0)
number2 = st.sidebar.number_input("収入２",0)
number3 = st.sidebar.number_input("その他収入",0)
if st.sidebar.button("収入合計"):
  total1 = number1 + number2 + number3
  st.write(f"収入合計:{total1}円")

st.sidebar.write("支出")
st.sidebar.write("カテゴリー１：毎月発生／固定費")
number4 = st.sidebar.number_input("住宅関連費",0)
number5 = st.sidebar.number_input("通信費",0)
number6 = st.sidebar.number_input("保険（月払い）",0)
number7 = st.sidebar.number_input("習い事",0)
number8 = st.sidebar.number_input("学校関連費",0)
number9 = st.sidebar.number_input("サブスク（月払い）",0)
number10 = st.sidebar.number_input("その他１",0)
if st.sidebar.button("支出１合計"):
  total2 = number4 + number5 + number6 + number7 + number8 + number9 + number10
  st.write(f"支出１合計:{total2}円")

st.sidebar.write("カテゴリー２：毎月発生／変動費")
number11 = st.sidebar.number_input("食費",0)
number12 = st.sidebar.number_input("日用消耗品費",0)
number13 = st.sidebar.number_input("水道光熱費",0)
number14 = st.sidebar.number_input("被服費",0)
number15 = st.sidebar.number_input("医療費",0)
number16 = st.sidebar.number_input("車関連費",0)
number17 = st.sidebar.number_input("美容",0)
number18 = st.sidebar.number_input("その他２",0)
if st.sidebar.button("支出２合計"):
  total3 = number11 + number12 + number13 + number14 + number15 + number16 + number17 + number18
  st.write(f"支出１合計:{total3}円")
 
st.sidebar.write("カテゴリー３：毎年発生／固定費")
number19 = st.sidebar.number_input("保険（年払い）",0)
number20 = st.sidebar.number_input("税金",0)
number21 = st.sidebar.number_input("ＮＨＫ",0)
number22 = st.sidebar.number_input("サブスク（年払い）",0)
number23 = st.sidebar.number_input("車検(2年)",0)
number24 = st.sidebar.number_input("その他３",0)
if st.sidebar.button("支出３合計"):
  total4 = (number19 + number20 + number21 + number22 + number24) / 12 + number23 / 24 
  st.write(f"支出３合計:{total4}円")

st.sidebar.write("カテゴリー４：不定期／変動費")
number25 = st.sidebar.number_input("家具・家電",0)
number26 = st.sidebar.number_input("レジャー",0)
number27 = st.sidebar.number_input("病気",0)
number28 = st.sidebar.number_input("交際",0)
number29 = st.sidebar.number_input("卒業・入学",0)
number30 = st.sidebar.number_input("その他４",0)
if st.sidebar.button("支出４合計"):
  total5 = number25 + number26 + number27 + number28 + number29 + number30 
  st.write(f"支出４合計:{total5}円")

st.write(f"{month}の家計は・・・？")

if st.sidebar.button("総合計を表示"):
    total_income = number1 + number2 + number3
    total_fixed_monthly = number4 + number5 + number6 + number7 + number8 + number9 + number10
    total_variable_monthly = number11 + number12 + number13 + number14 + number15 + number16 + number17 + number18
    total_fixed_yearly = (number19 + number20 + number21 + number22 + number24) / 12 + number23 / 24
    total_variable_irregular = (number25 + number26 + number27 + number28 + number29 + number30) / 12

    total_expenses = total_fixed_monthly + total_variable_monthly + total_fixed_yearly + total_variable_irregular
    balance = total_income - total_expenses
    ratio = total_expenses / total_income * 100
    saving = 100 - ratio

    st.write(f"収入合計: {total_income}円")
    st.write(f"支出１合計: {total_fixed_monthly}円")
    st.write(f"支出２合計: {total_variable_monthly}円")
    st.write(f"支出３合計: {total_fixed_yearly}円")
    st.write(f"支出４合計: {total_variable_irregular}円")
    st.write(f"支出総合計: {total_expenses}円")
    
    st.write(f"収支差額: {balance}円")
    st.write(f"貯蓄率: {saving}%")

    if saving >= 20:
      st.write("素晴らしい。その調子！")
    elif saving >=10:
      st.write("いい感じ。理想の家計はすぐそこ！")
    elif saving >= 0:
      st.write("ぎりぎりセーフ")
    else:
      st.write("赤字！見直しが必要です！！")
