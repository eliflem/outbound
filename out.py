import streamlit as st
import requests as r
import pandas as pd
import time

st.title("Banabikurye Outbound Deal Yaratma Aracı")
st.subheader("Aşağıdaki formda yer alan tüm bilgileri doldurtuktan sonra 'Create Deal' butonuna basınız.")



with st.form(key='my_form'):
    org_name = st.text_input('Organization name')
    org_region = st.text_input('Region')
    org_email = st.text_input('Email')
    org_phone = st.text_input('Phone')
    org_phone2 = st.text_input('Other Phone')
    legal_type = st.radio("Legal type", ("Business", "Individual", "No answer"))
    del_est = st.radio("Delivery estimation", ("5'den fazla", "5'den az", "Individual"))
    industry = st.selectbox("Industry", ('Autos / Parts & Services', 'Beauty & Fitness', 'Bevarages', 'Cakes & Bakeries', 'Consumer Electronics / Accessories', 'Courier Lead', 'Dental Products', 'Documents', 'E-Commerce', 'Fashion & Lifestyle', 'Flowers', 'Food - Fresh Products', 'Food - Restaurant', 'Gifts & Souvenir', 'Grocery', 'Grocery - Pet Products', 'Healthcare / Pharmacy', 'Individuals', 'Laundry Services', 'Media & Communication', 'No Answer/ No Response', 'Optics', 'Others', 'Supermarket'))
    notes = st.text_input("Notes")
    submit_button = st.form_submit_button(label='Create Deal')
if not org_name:
    st.write("Deal yaratmak için formu doldurunuz")
else:        
    if submit_button:
       st.subheader("Teşekkürler")

    #create organization func
   
    organization = {'owner_id':11539544,
            "name": org_name,
           "b1faf8cf25454aa8690d7b761def5b29be2c9b07": org_email,
           "d3ace2189605037b38016a44957b190f45a924b9": org_phone,
           "208c219904faba22afb629d63d1c9b89c516cd13": org_region,
           "visible_to": '5'}
    org = r.post('https://api.pipedrive.com/v1/organizations?api_token=st.secrets["token"]', json=organization)
    result_1 = org.json()
    st.write('https://api.pipedrive.com/v1/organizations?api_token='+'st.secrets["token"]')

    
