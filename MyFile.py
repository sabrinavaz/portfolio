import pandas as pd
import win32com.client as win32
# import view the database
sales_table = pd.read_excel('Vendas.xlsx')

# view the database
pd.set_option('display.max_columns', None)
print(sales_table)

# revenue by store
revenue = sales_table[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(revenue)

# number of products sold per store
quantity = sales_table[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantity)

print('-' * 50)

# average price per product in each store
average_price = (revenue['Valor Final'] / quantity['Quantidade']).to_frame()
# will transform in a table
average_price = average_price.rename(columns={0: 'Average Price'})
print(average_price)
# send an email with the report using Outlook
#import in line 2
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'sabrinavalevaz@gmail.com'
mail.Subject = 'Sales Report by Store'
mail.HTMLBody = f'''
<p>Hello team,</p>

<p>Follow the sales report for each store.</p>

<p>Revenue:</p>
{revenue.to_html(formatters={'Valor Final': '${:,.2f}'.format})}

<p>Quantity Sold:</p>
{quantity.to_html()}

<p>Average price per product in each store:</p>
{average_price.to_html(formatters={'Average Price': '${:,.2f}'.format})}

<p>If you have any questions, please feel free to contact me.</p>

<p>Best,</p>
<p>Sabrina Vaz</p>
'''

mail.Send()

print('Email Sent')