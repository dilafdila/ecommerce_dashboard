import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca dataset
orders_df = pd.read_csv('orders_dataset.csv')
order_items_df = pd.read_csv('order_items_dataset.csv')
products_df = pd.read_csv('products_dataset.csv')
order_reviews_df = pd.read_csv('order_reviews_dataset.csv')

# Menggabungkan data untuk analisis
order_items_products = pd.merge(order_items_df, products_df, on='product_id', how='inner')
category_sales = order_items_products.groupby('product_category_name')['order_item_id'].sum().reset_index()

# Menyiapkan visualisasi kategori produk terlaris
category_sales = category_sales.sort_values('order_item_id', ascending=False)

# Visualisasi 1: Kategori Produk Terlaris
def plot_category_sales():
    plt.figure(figsize=(12, 6))
    sns.barplot(data=category_sales.head(10), x='product_category_name', y='order_item_id')
    plt.title('Top 10 Kategori Produk Terlaris')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Kategori Produk')
    plt.ylabel('Jumlah Barang Terjual')
    st.pyplot()

# Visualisasi 2: Sebaran Ulasan Pelanggan
def plot_review_ratings():
    plt.figure(figsize=(10, 6))
    sns.countplot(data=order_reviews_df, x='review_score', palette='viridis')
    plt.title('Sebaran Ulasan Pelanggan Berdasarkan Rating')
    plt.xlabel('Rating Ulasan')
    plt.ylabel('Jumlah Ulasan')
    st.pyplot()

# Streamlit Layout
def main():
    st.title('Dashboard E-Commerce Analysis')
    
    st.sidebar.header('Pilih Visualisasi')
    options = ['Kategori Produk Terlaris', 'Sebaran Ulasan Pelanggan']
    selected_option = st.sidebar.selectbox('Pilih topik visualisasi:', options)
    
    if selected_option == 'Kategori Produk Terlaris':
        st.subheader('Kategori Produk Terlaris Berdasarkan Jumlah Barang yang Terjual')
        plot_category_sales()
    elif selected_option == 'Sebaran Ulasan Pelanggan':
        st.subheader('Sebaran Ulasan Pelanggan Berdasarkan Rating')
        plot_review_ratings()

# Jalankan aplikasi
if __name__ == "__main__":
    main()
